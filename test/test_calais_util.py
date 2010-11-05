import unittest
import calais_util


class TestCalaisUtil(unittest.TestCase):

    def test_relevant_entities_empty(self):
        self.assertEqual(calais_util.relevant_entities([]), [])

    def test_relevant_entities_one(self):
        entity = {'instances':[{'offset':0, 'length':5}]}
        self.assertEqual(calais_util.relevant_entities(
            [entity]), [entity])

    def test_relevant_entities_no_overlap(self):
        entities = [{'instances':[{'offset':0, 'length':5}]},
                    {'instances':[{'offset':5, 'length':5}]}]
        self.assertEqual(calais_util.relevant_entities(entities), entities)

    def test_relevant_entities_overlap_same(self):
        entities = [{'instances':[{'offset':0, 'length':5}]},
                    {'instances':[{'offset':0, 'length':5}]}]
        self.assertEqual(
            calais_util.relevant_entities(entities), [entities[0]])

    def test_relevant_entities_overlap_first(self):
        entities = [{'instances':[{'offset':0, 'length':5}]},
                    {'instances':[{'offset':4, 'length':5}]}]
        self.assertEqual(
            calais_util.relevant_entities(entities), [entities[0]])

    def test_relevant_entities_overlap_second(self):
        entities = [{'instances':[{'offset':4, 'length':5}]},
                    {'instances':[{'offset':0, 'length':5}]}]
        self.assertEqual(
            calais_util.relevant_entities(entities), [entities[1]])
        

if __name__ == '__main__':
    unittest.main()
