# requires http://code.google.com/p/python-calais/
import calais
import operator

def relevant_entities(entities):
    """ Return non-overlapping entities. """
    if not entities:
        return entities
    entities_out = []
    entities = sorted(entities, key=lambda e: e['instances'][0]['offset'])
    entities_out.append(entities.pop(0))    
    while entities:
        entity = entities.pop(0)
        instance = entity['instances'][0]
        last_instance = entities_out[-1]['instances'][0]
        if (instance['offset'] >=
            last_instance['offset'] + last_instance['length']):
            entities_out.append(entity)
    return entities_out

def normalize_entity(entity):
    """
    Return entity, if relevant, or None.
    """
    if entity['name'].lower() == 'rt':
        return None
    return entity

def get_entities(text, api_key):
    response = calais.Calais(api_key, submitter="foo").analyze(
        text)
    try:
        return [
            entity['name'] for entity in relevant_entities(response.entities)
            if normalize_entity(entity)]
    except AttributeError:
        # if no entities found, this attribute is not set
        return []


if __name__ == '__main__':
    import config
    print get_entities(
        'Hello, Barack Obama is the President of the United States, '
        'a.k.a. the United States of America.',
        config.calais_key)
