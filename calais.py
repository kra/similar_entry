# http://code.google.com/p/python-calais/
import calais

def get_entities(text, api_key):
    return [
        entity['name']
        for entity in calais.Calais(api_key, submitter="foo").analyze(text)]

