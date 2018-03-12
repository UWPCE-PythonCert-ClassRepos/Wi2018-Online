"""Provide pytest unit tests for the mailroom assignment."""
import pytest
import datetime
from unittest.mock import Mock
from unittest.mock import patch
from unittest.mock import MagicMock
from  mailroom import *


@pytest.fixture()
def donors():
    """Provide sample data for the tests."""
    d1 = SingleDonor("Bill Murray", [125, 1.0])
    d2 = SingleDonor("Woody Harrelson", [71.5, 1.25])
    d3 = SingleDonor("Jesse Eisenberg", [99.99, 1.75])
    return Donors([d1, d2, d3])


# TESTS FOR THE SINGLE DONOR CLASS
def test_init_single_donor():
    """Test SingleDonor class instantiation, name and donations properties."""
    # what if an int is passed as a donation?
    d1 = SingleDonor("Bill Murray", 125)
    # what if a list is passed?
    d2 = SingleDonor("Woody Harrelson", [71.5, 1.25])
    # what if a tuple is passed?
    d3 = SingleDonor("Jesse Eisenberg", (99.99, 1.75))
    assert d1.name == "Bill Murray"
    assert d1.donations == [125]
    assert d2.name == "Woody Harrelson"
    assert d2.donations == [71.5, 1.25]
    assert d3.name == "Jesse Eisenberg"
    assert d3.donations == [99.99, 1.75]

def test_str_single_donor(capsys):
    """Test __str__ in the SingleDonor class."""
    d = SingleDonor("Bill Murray", 125)
    print(d)
    out, _ = capsys.readouterr()
    assert out.strip() == "Bill Murray"


def test_repr_single_donor():
    """Test __repr__ method of the SingleDonor class."""
    d = SingleDonor("Bill Murray", 125)
    assert repr(d) == 'SingleDonor("Bill Murray", 125)'
    assert eval(repr(d)) == SingleDonor("Bill Murray", 125)


def test_eq_single_donor(donors):
    """Test equality."""
    d1 = SingleDonor("Bill Murray", [125, 1.0])
    d2 = SingleDonor("Bill Murray", [125, 1.0])
    d3 = SingleDonor("Woody Harrelson", [71.5, 1.25])
    assert d1 == d2
    assert d1 != d3

# def test_lt_single_donor(donors):  # don't understand how __lt__ works
#     """Test less than special method."""
#     d1 = SingleDonor("Bill Murray", [125, 1.0])
#     d2 = SingleDonor("Bill",[125, 1.0])
#     assert d1 < d2


def test_add_donation():
    """Test add_donation() method of the SimpleDonor class."""
    d = SingleDonor("Bill Murray", 125)
    d.add_donation(8.55)
    assert d.donations == [125, 8.55]


def test_get_last_donation():
    """Test if I can get the last donation."""
    d1 = SingleDonor("Bill Murray", 125)
    d2 = SingleDonor("Jesse Eisenberg", (99.99, 1.75))
    assert d1.get_last_donation() == 125
    assert d2.get_last_donation() == 1.75

# TESTS FOR THE DONORS CLASS
def test_init_donors():
    """The Donors class instantiation."""
    d1 = SingleDonor("Bill Murray", 125)
    d2 = SingleDonor("Woody Harrelson", 71.5)
    all_donors = Donors([d1, d2])


def test_iter_donors(donors):
    """Test if I can iterate over a donors class object."""
    names = []
    for donor in donors:
        names.append(donor.name)
    assert names == ["Bill Murray", "Woody Harrelson", "Jesse Eisenberg"]


def test_sort_donors_by_total(donors):
    """Test if I can sort donors by total donation."""
    sorted_copy = sorted(donors, key=SingleDonor.sort_by_total, reverse=True)
    donors_list = [donor.name for donor in sorted_copy]
    assert donors_list == ["Bill Murray", "Jesse Eisenberg", "Woody Harrelson"]
    donors_list_amount = [(donor.name, sum(donor.donations)) for donor in sorted_copy]
    assert donors_list_amount == [("Bill Murray", 126.0),
                                  ("Jesse Eisenberg", 101.74),
                                  ("Woody Harrelson", 72.75)
                                  ]


def test_sort_donors_by_name(donors):
    """Test if I can sort donors by name."""
    sorted_copy = sorted(donors, key=SingleDonor.sort_by_name)
    donors_list = [donor.name for donor in sorted_copy]
    assert donors_list == ["Bill Murray", "Jesse Eisenberg", "Woody Harrelson"]


def test_print_donor_names(capsys, donors):
    """Test print_donor_names() in Donors class."""
    donors.print_donor_names()
    out, _ = capsys.readouterr()
    assert out.strip() == "Bill Murray, Jesse Eisenberg, Woody Harrelson"

def test_contains(donors):
    """Test if I can check that a donor is in donors by name."""
    assert "Bill Murray" in donors

def test_write_report(capsys, donors):
    """Test that the report at least contains certain elements."""
    donors.create_report()
    out, _ = capsys.readouterr()
    assert "Bill Murray" in out
    assert "Woody Harrelson" in out
    assert out.index("Bill Murray") < out.index("Woody Harrelson")


def test_get_donor(donors):
    """Test if I can get a donor class object from a collection, by name."""
    d = donors.get_donor("Woody Harrelson")
    assert isinstance(d, SingleDonor)
    assert d.name == "Woody Harrelson"
    with pytest.raises(ValueError):
        d2 = donors.get_donor("Someone")


def test_append(donors):
    """Test that a new SingleDonor object can be appended to the Donors class object."""
    donors.append(SingleDonor("New Donor", 123.98))
    assert donors.get_donor("New Donor").get_last_donation() == 123.98



# TESTS FOR THE STARTMENU CLASS
# This class is too complicated for me to test as a whole
# so I found a solution in the Internet how to mock complicated  __init__
# in the class and test only simple methods within the class.
# Explanation is available at
# https://medium.com/@george.shuklin/mocking-complicated-init-in-python-6ef9850dd202
def test_menu_selection_user_quits(monkeypatch):
    with patch.object(StartMenu, "__init__", lambda x, y: None):
        s = StartMenu(None)

        # User is prompted to enter something when the main menu is displayed
        # But chooses the option to quit immediately.
        # The line below simulates the user entering "125" in the terminal
        # This value "125" is arbitrary in this test
        monkeypatch.setattr('builtins.input', lambda _: "125")

        # Now fake all methods that the menu_selection would call:
        # Fake the main dispatch dict
        s.main_dispatch = Mock()
        # This assigns the key "125" the value "s.quit" in the dispatch dict
        s.main_dispatch.return_value = {"125": s.quit}

        # Fake quit() which would be called by main_dispatch()
        s.quit = Mock()
        s.quit.return_value = "exit menu"

        assert s.menu_selection("prompt", s.main_dispatch()) is None


def test_quit():
    """Test the quit() method."""
    # This mocks the complicated __init__ method in the StartMenu class
    with patch.object(StartMenu, "__init__", lambda x, y: None):
        s = StartMenu(None)

        assert s.quit() == "exit menu"


def test_main_menu_dispatch():
    """Test that the main_dispatch() method at least returns a dict."""
    # This mocks the complicated __init__ method in the StartMenu class
    with patch.object(StartMenu, "__init__", lambda x, y: None):
        s = StartMenu(None)

        # Need to fake a self.donors object within the StartMenu class
        # which object is used in the main_menu_dispatch() method
        s.donors = Mock()
        s.donors.return_value = donors

        assert isinstance(s.main_menu_dispatch(), dict)


def test_main_menu_prompt():
    """Test the main_menu_prompt() method."""
    # This mocks the complicated __init__ method in the StartMenu class
    with patch.object(StartMenu, "__init__", lambda x, y: None):
        s = StartMenu(None)

        assert "Main Menu" in s.main_menu_prompt()
        assert "0 - Quit\n" in s.main_menu_prompt()


def test_send_thank_you_dispatch():
    """Test that the send_thank_you_dispatch() at least returns a dict."""
    # This mocks the complicated __init__ method in the StartMenu class
    with patch.object(StartMenu, "__init__", lambda x, y: None):
        s = StartMenu(None)

        # Need to fake a self._donors object within the StartMenu class
        # which object is used in the send_thanks_dispatch() method
        s.donors = Mock()
        s.donors.return_value = donors

        assert isinstance(s.send_thank_you_dispatch(), dict)


def test_send_thank_you_prompt():
    """Test the send_thank_you_prompt() method."""
    # This mocks the complicated __init__ method in the StartMenu class
    with patch.object(StartMenu, "__init__", lambda x, y: None):
        s = StartMenu(None)

        assert "Send-Thank-You Sub-Menu" in s.send_thank_you_prompt()
        assert "0 - Quit\n" in s.send_thank_you_prompt()


def test_get_email():
    """Test the get_email() method."""
    # This mocks the complicated __init__ method in the StartMenu class
    with patch.object(StartMenu, "__init__", lambda x, y: None):
        s = StartMenu(None)

        mail = s.get_email("Bob", 125.25)

        assert "Dear Bob" in mail
        assert "$125.25" in mail

# def test_add_exist_donor_donation(donors):
#     """add_donation(name, amount) for an existing donor."""
#     mailroom.add_donation("A", 1000.0)
#     assert mailroom.donors["A"][-1] == 1000.0
#
#
def test_input_donation_zero(monkeypatch):
    """input_donation(name) with the user typing zero."""
    # This mocks the complicated __init__ method in the StartMenu class
    with patch.object(StartMenu, "__init__", lambda x, y: None):
        s = StartMenu(None)

        # This simulates the user entering "0" on prompt
        # causing the program to return False
        monkeypatch.setattr('builtins.input', lambda _: "0")
        assert s.input_donation("any_name") is False
#
#
def test_input_donation_number(monkeypatch, donors):
    """input_donation(name) with the user typing a valid number (> 0)."""
    # This mocks the complicated __init__ method in the StartMenu class
    with patch.object(StartMenu, "__init__", lambda x, y: None):
        s = StartMenu(None)

        # Need to fake a self.donors object within the StartMenu class
        s.donors = Mock()
        s.donors.return_value = donors

        # This simulates the user entering "300" on prompt
        # while a new donor name is passed to the method
        # so such donor and his donation are added and
        # the method returns True
        monkeypatch.setattr('builtins.input', lambda _: "300")
        assert s.input_donation("New name") is True
        # assert donors.get_donor("New name").get_last_donation() == 300

#
def test_old_donor_interaction_user_input_zero(monkeypatch):
    """_old_donor_interaction() user enters zero on prompt."""
    # This mocks the complicated __init__ method in the StartMenu class
    with patch.object(StartMenu, "__init__", lambda x, y: None):
        s = StartMenu(None)

        # Need to fake a self.donors object within the StartMenu class
        s.donors = MagicMock()
        s.donors.return_value = donors

        # This simulates the user entering "0" on prompt to quit
        monkeypatch.setattr('builtins.input', lambda _: "0")
        assert s.old_donor_interaction() is None
#
#
def test_new_donor_interaction_user_input_zero(monkeypatch):
    """new_donor_interaction() user enters 0 on promp."""
        # This mocks the complicated __init__ method in the StartMenu class
    with patch.object(StartMenu, "__init__", lambda x, y: None):
        s = StartMenu(None)

        # Need to fake a self.donors object within the StartMenu class
        s.donors = MagicMock()
        s.donors.return_value = donors

        # This simulates the user entering "0" on prompt to quit
        monkeypatch.setattr('builtins.input', lambda _: "0")
        assert s.new_donor_interaction() is None


def test_new_donor_interaction_user_input_name(monkeypatch, capsys):
    """new_donor_interaction(); User enters a new name on prompt."""
    # WHEN the user enters a name when prompted to enter a name
    # THEN the function should print a thank-you email
    # This mocks the complicated __init__ method in the StartMenu class
    with patch.object(StartMenu, "__init__", lambda x, y: None):
        s = StartMenu(None)

        # Need to fake a self.donors object within the StartMenu class
        s.donors = MagicMock()
        s.donors.return_value = donors

        # This simulates the user typing "Any_name" on prompt
        monkeypatch.setattr('builtins.input', lambda _: "Any_name")

        # Fake all functions inside old_donor_interaction()
        s.input_donation = Mock()
        s.input_donation.return_value = True

        s.get_email = Mock()
        s.get_email.return_value = "some_text"

        s.get_last_donation = Mock()
        s.get_last_donation.return_value = True

        s.new_donor_interaction()
        out, _ = capsys.readouterr()
        assert out.strip() == "some_text"
#
#
# def test_old_donor_interaction_user_input_name(monkeypatch, capsys, donors):
#     """old_donor_interaction(); User enters an old name on prompt."""
#     # WHEN the user enters an old name when prompted to enter a name
#     # THEN the function should print a thank-you email
#     # This mocks the complicated __init__ method in the StartMenu class
#     with patch.object(StartMenu, "__init__", lambda x, y: None):
#         s = StartMenu(None)
#
#     # Need to fake a self.donors object within the StartMenu class
#     s.donors = MagicMock()
#     s.donors.return_value = donors
#
#     # This simulates the user typing "Old_name" on prompt
#     monkeypatch.setattr('builtins.input', lambda _: "Bill Murray")
#
#     # Fake all functions inside any_donor()
#     s.input_donation = Mock()
#     s.input_donation.return_value = True
#
#     s.get_email = Mock()
#     s.get_email.return_value = "some_text"
#
#     s.get_last_donation = Mock()
#     s.get_last_donation.return_value = True
#
#     s.old_donor_interaction()
#     out, _ = capsys.readouterr()
#     assert out.strip() == "some_text"


def test_send_all_dispatch():
    """Test that send_all_dispatch() method at least returns a dict."""
    # This mocks the complicated __init__ method in the StartMenu class
    with patch.object(StartMenu, "__init__", lambda x, y: None):
        s = StartMenu(None)

        # Need to fake a self.donors object within the StartMenu class
        s.donors = Mock()
        s.donors.return_value = donors

        assert isinstance(s.send_all_dispatch(), dict)


def test_send_all_prompt():
    """Test the send_all_menu_prompt() method."""
    # This mocks the complicated __init__ method in the StartMenu class
    with patch.object(StartMenu, "__init__", lambda x, y: None):
        s = StartMenu(None)

        assert "Send to everyone sub-menu" in s.send_all_prompt()
        assert "0 - Quit\n" in s.send_all_prompt()
#
#
@pytest.fixture
def patch_datetime_today(monkeypatch):
    """Found on stackoverflow and modified for my purposes."""
    class mydatetime:
        @classmethod
        def today(cls):
            return "2020-12-25"

    monkeypatch.setattr(datetime, 'date', mydatetime)


def test_get_full_path(tmpdir, patch_datetime_today):
    """get_full_path(path, name). Should return path/date-donor name.txt."""
    # This mocks the complicated __init__ method in the StartMenu class
    with patch.object(StartMenu, "__init__", lambda x, y: None):
        s = StartMenu(None)

        expected_path = tmpdir.join("2020-12-25-Alex Skrn.txt")
        assert s.get_full_path(tmpdir, "Alex Skrn") == expected_path


def test_write_file(tmpdir):
    """write_file(path, text)."""
    # This mocks the complicated __init__ method in the StartMenu class
    with patch.object(StartMenu, "__init__", lambda x, y: None):
        s = StartMenu(None)

        file = tmpdir.join('output.txt')
        s.write_file(file.strpath, "some text")  # or str(file)
        assert file.read() == "some text"


# def test_write_cwd(monkeypatch, tmpdir, capsys, donors):
#     """write_cwd() User writes all emails to cwd."""
#     # Check that the final print statement in the function is okey
#     # Check that the function indeed created 2 files ('cos only 2 donors now)
#     # Check that the files created are not empty at least
#     # This mocks the complicated __init__ method in the StartMenu class
#     with patch.object(StartMenu, "__init__", lambda x, y: None):
#         s = StartMenu(None)
#
#         # Need to fake a self.donors object within the StartMenu class
#         s.donors = MagicMock()
#         s.donors.return_value = donors
#
#         monkeypatch.chdir(tmpdir)
#         s.write_cwd()
#         out, _ = capsys.readouterr()  # out has an extra \n, hence .strip() below
#         expected = ("\nAll letters saved in {}\n".format(str(tmpdir))).strip()
#         assert out.strip() == expected
#         assert len(tmpdir.listdir()) == 3
#         for file in tmpdir.listdir():
#             assert bool(file.read()) is True
#
#
# def test_write_select_dir(tmpdir, capsys, donors):
#     """write_select_dir(). User selects a directory."""
#     # Check that the print statement in the function is okey
#     # Check that the function indeed created 2 files
#     # Check that the files created are not empty at least
#     # This mocks the complicated __init__ method in the StartMenu class
#     with patch.object(StartMenu, "__init__", lambda x, y: None):
#         s = StartMenu(None)
#
#     # Need to fake a self.donors object within the StartMenu class
#         s.donors = MagicMock()
#         s.donors.return_value = donors
#
#         s.ask_user_dir = Mock()
#         s.ask_user_dir.return_value = tmpdir
#
#         s.write_select_dir()
#         out, _ = capsys.readouterr()
#         expected = ("\nAll letters saved in {}\n".format(str(tmpdir))).strip()
#         assert out.strip() == expected
#         assert len(tmpdir.listdir()) == 2
#         for file in tmpdir.listdir():
#             assert bool(file.read()) is True
#
#
def test_write_select_dir_user_cancel():
    """In write_select_dir() the user hits cancel."""
    # When the user hits cancel when asked to select a directory
    # Then the function should return
    # This mocks the complicated __init__ method in the StartMenu class
    with patch.object(StartMenu, "__init__", lambda x, y: None):
        s = StartMenu(None)

        # Fake a function inside write_select_dir()
        s.ask_user_dir = Mock()
        s.ask_user_dir.return_value = ""

        assert s.write_select_dir() is None
