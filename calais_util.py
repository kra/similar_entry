# requires http://code.google.com/p/python-calais/
import calais
import operator
import time

import util


class CalaisGetter(object):
    # XXX generalize this, prob. into a HTTP client
    sleep_secs = 0.0625
    @classmethod
    def get(cls, text, api_key):
        while True:
            # Q&d backing off in response to throttling.
            # This works if there's one single-threaded CalaisGetter.
            time.sleep(cls.sleep_secs)
            try:
                out = calais.Calais(api_key, submitter="foo").analyze(
                    text.encode('ascii', 'replace'))
                cls.sleep_secs = max(cls.sleep_secs / 2, 0.0625)
                return out
            except ValueError, exc:
                # XXX httplib.BadStatusLine
                # Q&D error messaage non-parsing
                if (exc.message.find(
                    'does not yet support your submitted content') != -1):
                    util.log('calais did not like text: %s' % (exc.message))
                    return []
                cls.sleep_secs *= 2
                util.log('calais sleeping: %s (%s)' % (cls.sleep_secs, text))


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
    response = CalaisGetter.get(text, api_key)
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
