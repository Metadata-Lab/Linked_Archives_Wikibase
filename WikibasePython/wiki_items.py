import pywikibot, json

def search_for_q(label):
    site = pywikibot.Site("en", "wikipedia")

    try:
        #search wikibase for item with label
        page = pywikibot.Page(site, label)
        item = pywikibot.ItemPage.fromPage(page)

        #if found, do some magic to turn item into proper string
        magic = {}
        magic["Q"] = str(item)
        q = magic["Q"]
        #make sure we only get the Q### part
        magic["Q"] = q[11:-2]
        return magic["Q"]

    except:
        return None

def json_to_dict(file):
    with open(file) as json_file:
        data = json.load(json_file)
        return data

def main():
    objects = json_to_dict("../data/entities/objects_edited.json")
    for obj in objects.keys():
        if search_for_q(obj) is not None:
            print(obj)

if __name__ == '__main__':
    main()