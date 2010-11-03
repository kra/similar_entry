# import unittest
# import calais_util


# class TestCalaisUtil(unittest.TestCase):

#     def test_relevant_entities_empty(self):
#         self.assertEqual(calais_util.relevant_entities([]), [])

#     def test_relevant_entities_one(self):
#         self.assertEqual(calais_util.relevant_entities(
#             [{'offset':0, 'length':5}]), [{'offset':0, 'length':5}])

#     def test_relevant_entities_length(self):
#         self.assertEqual(
#             calais_util.relevant_entities(
#                 [{'offset':0, 'length':5}, {'offset':0, 'length':4}]),
#             [{'offset':0, 'length':4}])

#     def test_relevant_entities_same(self):
#         self.assertEqual(
#             calais_util.relevant_entities(
#                 [{'offset':0, 'length':5}, {'offset':0, 'length':5}]),
#             [{'offset':0, 'length':5}])
        

# if __name__ == '__main__':
#     unittest.main()
