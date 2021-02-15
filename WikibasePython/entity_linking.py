import spacy
from spacyEntityLinker import EntityLinker

def link():

    #Initialize Entity Linker
    entityLinker = EntityLinker()

    #initialize language model
    nlp = spacy.load("en_core_web_sm")

    #add pipeline
    nlp.add_pipe(entityLinker, last=True, name="entityLinker")

    doc = nlp("I watched the Pirates of the Carribean last silvester")

    #returns all entities in the whole document
    all_linked_entities=doc._.linkedEntities
    #iterates over sentences and prints linked entities
    for sent in doc.sents:
        sent._.linkedEntities.pretty_print()


if __name__ == '__main__':
    link()