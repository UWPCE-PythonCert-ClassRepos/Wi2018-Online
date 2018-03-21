#!/usr/bin/env python3

from unittest import TestCase
import mailroom4 as mr


class TstMailroom(TestCase):
    def test_quit_menu(self):
        self.assertEqual(mr.quit_menu(), "exit menu")

    def test_user_select(self):
        pass


if __name__ == 'main':
    TestCase()





