from unittest import TestCase
import mailroom_v4 as mailroom


class MailroomTest(TestCase):
    def test_run(self):
        mr = mailroom
        self.assertEqual(mr.quit(),'quit')

    def test_prompt_user(self):
        mr = mailroom
        self.assertEqual(mr.prompt_user(),1)

    def test_donor_letter(self):
        mr = mailroom
        mr.send_letter()
        with open('Jim.txt', 'r') as myfile:
            letter_txt = myfile.read()
        with open('Jim_test.txt', 'r') as myfile:
            letter_test = myfile.read()

        self.assertEqual(letter_txt, letter_test)

    def test_quit(self):
        mr = mailroom
        self.assertEqual(mr.quit(), 'quit')

    def test_create_report_total(self):
        donor_list = {'Jim': [25.00, 150.00, 2000.00, 100000.00], 'Linda': [10000.25], 'Bob': [5.03, 100.01, 6.00]}
        total = 0
        for key, value in donor_list.items():
            total = sum(value)
        self.assertEqual(total, 102175.0)

    def test_create_report_average(self):
        donor_list = {'Jim': [25.00, 150.00, 2000.00, 100000.00], 'Linda': [10000.25], 'Bob': [5.03, 100.01, 6.00]}
        total = 0
        l = 0
        for key, value in donor_list.items():
            total = sum(value)
            l =+ len(value)
        avg = total / l
        self.assertEqual(avg, 25543.75)

    def test_thank_you_add_donnor(self):
        donor_list = {'Jim': [25.00, 150.00, 2000.00, 100000.00], 'Linda': [10000.25], 'Bob': [5.03, 100.01, 6.00]}
        name = 'Don D'
        donnation  = 999.0
        donor_list[name] = []
        donor_list[name].append(donnation)
        print (sum(donor_list[name]))
        self.assertEqual(sum(donor_list[name]), 999.0)

    def test_thank_you_name(self):
        names = []
        donor_list = {'Jim': [25.00, 150.00, 2000.00, 100000.00], 'Linda': [10000.25], 'Bob': [5.03, 100.01, 6.00]}
        for key, value in donor_list.items():
            names.append(key)
        ",".join(names)
        names_test = ['Linda', 'Bob', 'Jim']
        self.assertEqual(names, names_test )
