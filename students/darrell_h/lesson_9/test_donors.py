from mailroom_class_using_composition import Donor, Mailroom
import pytest
from seed_data import initial_data

mailroom = Mailroom()


for k, v in initial_data.items():
    mailroom.donor_collection[k] = Donor(k, v['lname'], v['donations'])

def test_create_mailroom():
    assert isinstance(mailroom, Mailroom)

def test_initial_data_load():
    assert len(mailroom.donor_collection) == 6

def test_initial_data_load2():
    assert mailroom.total_number_of_donors() == 6

def test_add_donation_to_existing_donor():
    mailroom.add_donation('bob', 80)
    assert mailroom.donor_collection['bob'].donations == [60000, 70000, 7668, 4,80]

def test_zero_division():
    with pytest.raises(Exception):
        1 / 0

def test_zero_division_specific():
    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_add_donation_to_non_existing_donor():
    with pytest.raises(ValueError) as excinfo:
        mailroom.add_donation('sparky', 80)
    assert 'Donor not found' in str(excinfo.value)


def test_sum_donor_donations():
    assert mailroom.sum_donations('jack') == 1000

def test_list_donor():
    assert len(mailroom.list_donors()) > 0

def test_create_report():
    assert len(mailroom.create_report()) > 0



