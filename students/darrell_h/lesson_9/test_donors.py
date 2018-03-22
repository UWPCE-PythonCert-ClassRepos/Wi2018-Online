from mailroom_class_using_composition import Donor, Mailroom

mailroom = Mailroom()

intial_data = {'jack': [100, 200, 300, 400],
               'mary': [3000, 5000],
               'frank': [29.50, 31],
               'jane': [3000, 5000],
               'scrouge': [1, 2, 3],
               'bob': [60000, 70000, 7668, 4]}

for k, v in intial_data.items():
    mailroom.donor_collection[k] = Donor(k, v)

def test_create_mailroom():
    assert isinstance(mailroom, Mailroom)

def test_initial_data_load():
    assert len(mailroom.donor_collection) == 6

def test_initial_data_load2():
    assert mailroom.total_number_of_donors() == 6

def test_add_donation_to_existing_donor():
    mailroom.add_donation('scrouge', 80)
    assert mailroom.donor_collection['scrouge'].donations == [1,2,3,80]

def add_donor_without_initial_donation():
    mike = Donor('mike')

def add_donor_with_initial_donation():
    mike = Donor('mike',20)

def test_add_donation_to_non_existing_donor():
    mailroom.add_donation('sparky', 80)
    assert mailroom.donor_collection['sparky'].donations == 80

def test_sum_donor_donations():
    assert mailroom.sum_donations('jack') == 1000

def test_list_donor():
    assert len(mailroom.list_donors()) > 0



