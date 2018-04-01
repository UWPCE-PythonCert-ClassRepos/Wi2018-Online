#!/usr/local/bin/python3


import mailroom_with_exceptions as mail
import os


def test_quit():
    assert mail.quit() == 'exit'


def test_seperator():
    test_strings = ('long_test_string',
                    'test',
                    'test_string')
    for str in test_strings:
        assert len(mail.seperator(str)) == len(str)


def test_send_to_file():
    file_names = mail.send_to_file()
    for file_name in file_names:
        assert os.path.isfile(file_name)
