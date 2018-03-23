#!/usr/local/bin/python3

import Mailroom_mod6 as mailroom
import sys
import os
import pytest

def test_quit():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        mailroom.exit()
    assert pytest_wrapped_e.type == SystemExit
    #assert pytest_wrapped_e.value.code == 42

def test_sum():
    mailroom.donor_sum()
    assert len(mailroom.summary)>0

def test_sperator():
    strings = ('aron', 'test', 'random')
    for str in strings:
        assert len(mailroom.seperator(str)) == len(str)

def test_createfile():
    file_names = mailroom.create_email()
    for file_name in file_names:
        assert os.path.isfile(file_name)

#def test_quit():
#    assert mail.quit() == 'exit'


#def test_send_to_file():
#    file_names = mail.send_to_file()
#    for file_name in file_names:
#        assert os.path.isfile(file_name)