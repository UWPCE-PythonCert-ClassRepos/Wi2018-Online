#!/usr/bin/env python3
"""
Unit tests for the mailroom program
"""


contributor_list = [('Ken', 'Murray', '10.00', '4.00'),
                    ('Tew', 'Tangsuk', '2.68', '78268', '265.68'),
                    ('Joe', 'joe', '5.50', '57.89'),
                    ('Tina', 'Tangsuk', '29.02'),
                    ('Nathan', 'Merrill', '20.00')
                    ]


def test_donor_list():
    from mailroom import donor_list
    assert len(donor_list()) > 0
    assert type(donor_list()) == list


def test_add_donor():
    from mailroom import add_donor
    test_list = add_donor('Kenwas here')
    assert len(add_donor('Kenwas here')) > 0
    assert test_list[-1] == ('Kenwas', 'here')


def test_is_donor():
    from mailroom import is_donor
    assert is_donor('Ken Murray') is True
    assert is_donor('Daves Nothere') is False


def test_new_donation():
    from mailroom import new_donation
    assert new_donation('99.00', 'Ken Murray') is True


def test_thankyou_email():
    from mailroom import thankyou_email
    test_email = thankyou_email('99.00', 'Ken Murray')
    assert type(test_email) is str
    print('thankyou email')


def test_create_report():
    from mailroom import create_report
    assert create_report() is True


def test_send_letters_all():
    from mailroom import send_letters_all
    assert send_letters_all() is True






