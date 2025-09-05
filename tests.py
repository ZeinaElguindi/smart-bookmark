# import unittest

# from api.app import split, searchKeys

# class TestSearchSplit(unittest.TestCase):

#     def test_google_search(self):
#         query = "g cats"
#         result = split(query)
#         expected = searchKeys["g"] + "cats"
#         self.assertEqual(result, expected)
        
#     def test_google_multiword_search(self):
#         query = "g how to cook eggs"
#         result = split(query)
#         expected = searchKeys["g"] + "how to cook eggs"
#         self.assertEqual(result, expected)

#     def test_youtube_search(self):
#         query = "yt lo-fi"
#         result = split(query)
#         expected = searchKeys["yt"] + "lo-fi"
#         self.assertEqual(result, expected)

#     def test_unknown_command(self):
#         query = "xyz hello"
#         result = split(query)
#         # should just return the raw query since xyz not in searchKeys
#         self.assertEqual(result, query)

#     def test_missing_search_term(self):
#         query = "g"
#         # should not crash even if there's no second word
#         with self.assertRaises(IndexError):
#             split(query)

# if __name__ == "__main__":
#     unittest.main()
