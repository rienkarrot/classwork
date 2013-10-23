import unittest
import binarysearch

class TestSearch(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(1, binarysearch.search([0,1,2], 1))

    def test_five(self):
        self.assertEqual(2, binarysearch.search([0,1,2,3,4], 2))
    	
    def test_one(self):
        self.assertEqual(0, binarysearch.search([0], 0))
    
    def test_none(self):
        self.assertEqual(None, binarysearch.search([], 1))
    	
    def test_words(self):
        self.assertEqual(0, binarysearch.search(["zebra", "horse"], "zebra"))
    
    def test_lots(self):
        self.assertEqual(4, binarysearch.search([0,5,10,15,20,25,30,35], 20))
	
if __name__ == '__main__':
    unittest.main()
