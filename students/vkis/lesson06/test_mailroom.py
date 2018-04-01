import unittest
import mailroom4
import os.path

# known results
k1 = ("Tony Stark", "Captain America", "Daisy Johnson", "Melinda May",
           "Phil Coulson")
v1 = (906.04, 4500.00, 14.97, 555.02, 9999.99)
v2 = (2, 2, 3, 2, 1)
dict_data = {k1[i]: [v1[i], v2[i]] for i in range(len(k1))}

class MyTest(unittest.TestCase):
    def test_existing_name(self):
        mailroom4.email_thx_op2("Tony Stark")

    def test_new_nameNdonation(self):
        # bypass next user input with a unittest defined input in replacement
        mailroom4.input = lambda _: "1"
        mailroom4.email_thx_op2("vik")
        self.assertIn("vik", mailroom4.dict_data)
        self.assertEqual(1., mailroom4.dict_data["vik"][0])
    def test_filecreation(self):
        mailroom4.all_emails()
        self.assertTrue(os.path.isfile("Tony_Stark.txt"))


if __name__ == "__main__":
    unittest.main()
