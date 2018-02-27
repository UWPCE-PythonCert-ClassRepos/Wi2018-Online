import unittest
import mailroom4

# known results
k1 = ("Tony Stark", "Captain America", "Daisy Johnson", "Melinda May",
           "Phil Coulson")
v1 = (906.04, 4500.00, 14.97, 555.02, 9999.99)
v2 = (2, 2, 3, 2, 1)
d = {k1[i]: [v1[i], v2[i]] for i in range(len(k1))}

class MyTest(unittest.TestCase):
    def test_data_sort(self):
        # run the sort function on mailroom4 to process the raw data_sort
        # since data_sort() is within the __main__, by importing, it doesnt get called
        mailroom4.data_sort()
        self.assertEqual(mailroom4.dict_data, d)

if __name__ == "__main__":
    unittest.main()
