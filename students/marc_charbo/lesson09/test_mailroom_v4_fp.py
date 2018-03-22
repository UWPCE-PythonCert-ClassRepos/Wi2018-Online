from unittest import TestCase
import mailroom_v4_fp as mailroom


class MailroomTest(TestCase):
    def test_run(self):
        mr = mailroom
        self.assertEqual(mr.quit(),'quit')

    def test_prompt_user(self):
        mr = mailroom
        self.assertEqual(mr.prompt_user(),1)