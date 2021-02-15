from SPARQLWrapper import SPARQLWrapper, JSON
import os, ssl, json

def get_matches(label):
    # set up sparql wrapper with proper permissions
    if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
            getattr(ssl, '_create_unverified_context', None)):
        ssl._create_default_https_context = ssl._create_unverified_context

    sparql = SPARQLWrapper("https://query.wikidata.org/sparql",
                           agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')

    # query to get all properties based on q value
    query = 'SELECT DISTINCT ?item ?itemLabel WHERE {{ \
            ?item ?label "{label}"@en . \
            SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en". }} \
            }}'.format(label=label)

    sparql.setQuery(query)

    try:
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()

        q_ids = []

        # parse through query results
        for result in results["results"]["bindings"]:

            # property url
            item = result['item']['value']
            # property label text
            itemLabel = result['itemLabel']['value']

            qnum = item[item.rfind("/") + 1:]

            if itemLabel == label:
                q_ids.append(qnum)

        return q_ids

    except Exception as e:
        print(e)


def get_statements(q_string):

    #set up sparql wrapper with proper permissions
    if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
            getattr(ssl, '_create_unverified_context', None)):
        ssl._create_default_https_context = ssl._create_unverified_context

    sparql = SPARQLWrapper("https://query.wikidata.org/sparql", agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')

    #query to get all properties based on q value
    query = 'SELECT ?property ?propLabel ?value ?valueLabel WHERE {{ ' \
            'wd:{q} ?property ?value.' \
            'SERVICE wikibase:label {{bd:serviceParam wikibase:language "en".}}' \
            '?prop wikibase:directClaim ?property.' \
            '?prop rdfs:label ?propLabel.filter(lang(?propLabel) = "en"). }}'.format(q=q_string)

    sparql.setQuery(query)

    try :
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()

        dict = {}

        #parse through query resuults
        for result in results["results"]["bindings"]:

            #property url
            prop = result['property']['value']
            #property label text
            propLabel = result['propLabel']['value']
            #value of property
            val = result['value']['value']
            #value type - url or literal
            valType = result['value']['type']
            #text label for url value
            valLabel = result['valueLabel']['value']

            if "ID" in propLabel or "username" in propLabel or "image" in propLabel:
                continue

            pnum = prop[prop.rfind("/")+1:]

            if valType == 'literal':
                value = {valLabel: None}
            elif valType == 'uri':
                if 'wikidata.org/entity' in val:
                    value = {valLabel: val[val.rfind('/')+1:]}
                else:
                    value = {valLabel: None}
            else:
                print(valType) #let me know if there is another type there

            dict[propLabel] = [pnum, value]

        #print(dict)
        return dict

    except Exception as e:
        print(e)


def main():

    with open("people.json") as json_file:
        data = json.load(json_file)

    labels = data.keys()
    i = 1

    main_dict = {}
    for label in labels:
        qs = get_matches(label)
        list = []
        if qs is not None:
            for id in qs:
                dict = get_statements(id)
                list.append(dict)
        main_dict[label] = list
        print(str(i)+label)
        i+=1

    with open("matches.json", 'w') as outfile:
        json.dump(main_dict, outfile)

    print(main_dict)

if __name__ == '__main__':
    main()