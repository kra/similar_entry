# requires http://code.google.com/p/python-calais/
import calais

# # This would be helpful to avoid double-entities from overlapping text, like
# # "United States" and "United States of America".  Without it, we'll be
# # doing extra searches.
# def relevant_entities(entities):
#     """
#     Return non-overlapping entities.  Choose shorter entities when overlapping.
#     """
#     entities_out = []
#     for e in entities:
#         for e_out in entities_out:
#             if e['offset'] >= e_out['offset']:
#                 if e['offset'] < e_out['offset'] + e_out['length']:
#                     if e['length'] < e_out['length']:
#                         entities_out.remove(e_out)
#                         entities_out.append(e)
#                 else:
#                     entities_out.append(e)
#             elif e_out['offset'] < e['offset'] + e['length']:
#                     if e['length'] < e_out['length']:
#                         entities_out.remove(e_out)
#                         entities_out.append(e)
#             else:
#                 entities_out.append(e)                
#     return entities_out

def get_entities(text, api_key):
    response = calais.Calais(api_key, submitter="foo").analyze(
        text)
    try:
        return [entity['name'] for entity in response.entities]
    except AttributeError:
        # if no entities found, this attribute is not set
        return []


if __name__ == '__main__':
    import config
    print get_entities(
        'Hello, Barack Obama is the President of the United States, '
        'a.k.a. the United States of America.',
        config.calais_key)
