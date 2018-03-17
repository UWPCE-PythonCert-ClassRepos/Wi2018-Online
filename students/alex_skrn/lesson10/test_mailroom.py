"""Provide pytest unit tests for the oo-mailroom assignment."""
import pytest
import builtins
import datetime
from io import StringIO
from unittest import mock
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
    res = Donors([d1, d2, d3])
    return res


##################################
# TESTS FOR THE SINGLE DONOR CLASS
##################################
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

# @pytest.mark.parametrize("test_input,expected", [
#     ("3+5", 8),
#     ("2+4", 6),
#     ("6*9", 42),
# ])
# def test_eval(test_input, expected):
#     assert eval(test_input) == expected


def test_challenge_creates_instance_single_donor():
    """Test that challenge() returns the right type."""
    d1 = SingleDonor("Jesse Eisenberg", (5, 15))
    assert type(d1.challenge(1)) == SingleDonor


@pytest.mark.parametrize('inp, exception',
                         [(0, ValueError),
                          (0.41, ValueError),
                          (-1, ValueError),
                          (-3.5, ValueError),
                          ("a", ValueError),
                          ]
                         )
def test_challenge_single_factor_wrong_input(inp, exception):
    """Raise ValueError if the factor is wrong: negative or less than 1."""
    d1 = SingleDonor("Jesse Eisenberg", (5, 15))
    with pytest.raises(exception):
        d1.challenge(inp)


@pytest.mark.parametrize('inp, expectation',
                         [(1, [10, 30]),
                          (1.5, [12.5, 37.5]),
                          (2, [15, 45]),
                          (2.4, [17, 51]),
                          ]
                         )
def test_challenge_single_factor_right_input(inp, expectation):
    """Test that the donations property is updated correctly."""
    d1 = SingleDonor("Jesse Eisenberg", (5, 15))
    updated_donor = d1.challenge(inp)
    assert updated_donor.donations == expectation


############################
# TESTS FOR THE DONORS CLASS
############################
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
    # assert type(donors) == int  # Must fail


def test_challenge_collection_donors_create_right_type(donors):
    """Check that the method returns a Donors class object."""
    d = donors.challenge(1)
    assert type(d) == Donors
    #
    # d1 = SingleDonor("Bill Murray", [125, 1.0])
    # d2 = SingleDonor("Woody Harrelson", [71.5, 1.25])
    # d3 = SingleDonor("Jesse Eisenberg", [99.99, 1.75])


def test_challenge_donors_right_output_donations(donors):
    """Check that the Donors class object has donors with correct donations."""
    d = donors.challenge(1)
    assert d.get_donor("Bill Murray").donations == [250, 2]
    assert d.get_donor("Woody Harrelson").donations == [143, 2.5]
    assert d.get_donor("Jesse Eisenberg").donations == [199.98, 3.5]

    d2 = donors.challenge(1.5)
    assert d2.get_donor("Bill Murray").donations == pytest.approx([312.5, 2.5])
    assert d2.get_donor("Woody Harrelson").donations == pytest.approx([178.75, 3.125])
    assert d2.get_donor("Jesse Eisenberg").donations == pytest.approx([249.975, 4.375])

###############################
# TESTS FOR THE STARTMENU CLASS
###############################
def test_menu_selection_user_quits(monkeypatch):
    """Test menu_selection(). The user quits."""
    # This mocks the __init__ method in the StartMenu class
    # https://medium.com/@george.shuklin/mocking-complicated-init-in-python-6ef9850dd202
    with patch.object(StartMenu, "__init__", lambda x, y: None):
        s = StartMenu(None)

        # User is prompted to enter something when the main menu is displayed
        # But chooses the option to quit immediately.
        # The line below simulates the user entering "125" in the terminal
        # This value "125" is arbitrary
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
    # This mocks the __init__ method in the StartMenu class
    with patch.object(StartMenu, "__init__", lambda x, y: None):
        s = StartMenu(None)

        assert s.quit() == "exit menu"


def test_main_menu_dispatch():
    """Test that the main_dispatch() method at least returns a dict."""
    # This mocks the __init__ method in the StartMenu class
    with patch.object(StartMenu, "__init__", lambda x, y: None):
        s = StartMenu(None)

        # Need to fake a self.donors object within the StartMenu class
        # which object is used in the main_menu_dispatch() method
        s.donors = Mock()
        s.donors.return_value = donors

        assert isinstance(s.main_menu_dispatch(), dict)


def test_main_menu_prompt():
    """Test the main_menu_prompt() method."""
    # This mocks the __init__ method in the StartMenu class
    with patch.object(StartMenu, "__init__", lambda x, y: None):
        s = StartMenu(None)

        assert "Main Menu" in s.main_menu_prompt()
        assert "0 - Quit\n" in s.main_menu_prompt()


def test_send_thank_you_dispatch():
    """Test that the send_thank_you_dispatch() at least returns a dict."""
    # This mocks the __init__ method in the StartMenu class
    with patch.object(StartMenu, "__init__", lambda x, y: None):
        s = StartMenu(None)

        # Need to fake a self._donors object within the StartMenu class
        # which object is used in the send_thanks_dispatch() method
        s.donors = Mock()
        s.donors.return_value = donors

        assert isinstance(s.send_thank_you_dispatch(), dict)


def test_send_thank_you_prompt():
    """Test the send_thank_you_prompt() method."""
    # This mocks the __init__ method in the StartMenu class
    with patch.object(StartMenu, "__init__", lambda x, y: None):
        s = StartMenu(None)

        assert "Send-Thank-You Sub-Menu" in s.send_thank_you_prompt()
        assert "0 - Quit\n" in s.send_thank_you_prompt()


def test_get_email():
    """Test the get_email() method."""
    # This mocks the __init__ method in the StartMenu class
    with patch.object(StartMenu, "__init__", lambda x, y: None):
        s = StartMenu(None)

        mail = s.get_email("Bob", 125.25)

        assert "Dear Bob" in mail
        assert "$125.25" in mail


def test_input_donation_zero(monkeypatch):
    """input_donation(name) with the user typing zero."""
    # This mocks the __init__ method in the StartMenu class
    with patch.object(StartMenu, "__init__", lambda x, y: None):
        s = StartMenu(None)

        # This simulates the user entering "0" on prompt
        # causing the program to return False
        monkeypatch.setattr('builtins.input', lambda _: "0")
        assert s.input_donation("any_name") is False


# #  doesn't work
# def test_append_donor_via_startmenu_class():
#     """StartMenu.donors.append(SingleDonor(name, val)."""
#     # Sample data - I am not using donors fixture here for clarity
#     d1 = SingleDonor("Bill", [125])
#     d2 = SingleDonor("Woody", [71.5, 1.25, 0.5])
#     d3 = SingleDonor("Jesse", [99.99, 1.75, 16])
#     all_donors = Donors([d1, d2, d3])
#
#     # This simulates the user entering "0" for quit on prompt
#     # but I guess a class instance that I create later remains in place
#     # so I can test its methods and properties
#     builtins.input = Mock()
#     builtins.input.side_effect = ["0"]
#
#     # Capture all print statements the class object generates, into a mock object
#     with mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
#         # Instantitate a class object (though in reality this class never gets
#         # assigned to a name)
#         s = StartMenu(all_donors)
#
#         # This works
#         assert s.donors.get_donor("Bill").get_last_donation() == 125
#
#         # # This does not work for some reason: append() does not add the donor
#         # s.donors.append(SingleDonor("New Name", 999.99))
#         # assert s.donors.get_donor("New name").get_last_donation() == 999.99
#
#         # But here append() works nevertheless!
#         all_donors.append(SingleDonor("New", 0.99))
#         assert all_donors.get_donor("New").get_last_donation() == 0.99


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


def test_new_donor_interaction_user_input_zero(monkeypatch):
    """new_donor_interaction() user enters 0 on promp."""
        # This mocks the __init__ method in the StartMenu class
    with patch.object(StartMenu, "__init__", lambda x, y: None):
        s = StartMenu(None)

        # Need to fake a self.donors object within the StartMenu class
        s.donors = MagicMock()
        s.donors.return_value = donors

        # This simulates the user entering "0" on prompt to quit
        monkeypatch.setattr('builtins.input', lambda _: "0")
        assert s.new_donor_interaction() is None


def test_new_donor_interaction_user_input_new_name(donors):
    """new_donor_interaction(); User enters a new name on prompt."""
    # WHEN the user enters a new name when prompted to enter a name
    # THEN the function should ask for a donation and print a thank-you email

    # This simulates the user entering "0", "New Name", and donation amount on
    # a series of prompts, with the "0" to quit main_menu running at the start,
    # but I guess a class instance that I create remains in place
    # so I can test its methods
    builtins.input = Mock()
    builtins.input.side_effect = ["0", "New Name", 333.33]  # Multiple calls

    # Captures all print statements the class object generates, into a mock object
    with mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        # Instantitate a class object (though in reality this class never gets
        # assigned to a name)
        s = StartMenu(donors)

        # Check that the method prints the correct email on screan
        s.new_donor_interaction()
        assert "Dear New Name" in mock_stdout.getvalue()
        assert "$333.33" in mock_stdout.getvalue()


def test_old_donor_interaction_user_input_name(donors):
    """old_donor_interaction(); User enters an old name on prompt."""
    # WHEN the user enters an old name when prompted to enter a name
    # THEN the function should ask for an amount and print a thank-you email

    # This simulates the user entering "0" for quit on prompt
    # but I guess a class instance that I create remains in place
    # so I can test its methods
    builtins.input = Mock()
    builtins.input.side_effect = ["0", "Woody Harrelson"]

    # Captures all print statements the class object generates, into a mock object
    with mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        # Instantitate a class object (though in reality this class never gets
        # assigned to a name)
        s = StartMenu(donors)

        # This fakes a method so that the execution proceeds to final print()
        s.input_donation = Mock()
        s.input_donation.return_value = True

        # Check that the method prints the correct email on screan
        s.old_donor_interaction()
        assert "Dear Woody Harrelson" in mock_stdout.getvalue()
        # assert "Dear Bill" in mock_stdout.getvalue()  # Must fail


def test_input_donation_multiple_invalid_inputs():
    """Test input_donation() for a a number of invalid inputs."""
    # On the first prompt to enter a number, the user enters "A"
    #     The method prints "Input must be a number".
    # Then, on the next prompt, the user enters "-1".
    #     The method prints "Input must not be negative"
    # Then the user enters 0 to quit.
    #     So the method returns False.

    # This mocks the __init__ method in the StartMenu class
    with patch.object(StartMenu, "__init__", lambda x, y: None):
        s = StartMenu(None)

        # This simulates the user entering "A", then "-1", then "0" on prompts
        builtins.input = Mock()
        builtins.input.side_effect = ["A", "-1", "0"]

        # This captures all print statements into a mock object
        with mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            res = s.input_donation("Alex")

            #  The method should generate the following print statements
            assert "Input must be a number" in mock_stdout.getvalue()
            assert "Input must not be negative" in mock_stdout.getvalue()

            #  These statements should be in the following order
            assert mock_stdout.getvalue().index("number") < mock_stdout.getvalue().index("negative")

            # The method must return False when user enters 0 to quit
            assert res is False


def test_send_all_dispatch():
    """Test that send_all_dispatch() method at least returns a dict."""
    # This mocks the  __init__ method in the StartMenu class
    with patch.object(StartMenu, "__init__", lambda x, y: None):
        s = StartMenu(None)

        # Need to fake a self.donors object within the StartMenu class
        s.donors = Mock()
        s.donors.return_value = donors

        assert isinstance(s.send_all_dispatch(), dict)


def test_send_all_prompt():
    """Test the send_all_menu_prompt() method."""
    # This mocks the __init__ method in the StartMenu class
    with patch.object(StartMenu, "__init__", lambda x, y: None):
        s = StartMenu(None)

        assert "Send to everyone sub-menu" in s.send_all_prompt()
        assert "0 - Quit\n" in s.send_all_prompt()


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
    # This mocks the __init__ method in the StartMenu class
    with patch.object(StartMenu, "__init__", lambda x, y: None):
        s = StartMenu(None)

        file = tmpdir.join('output.txt')
        s.write_file(file.strpath, "some text")  # or str(file)
        assert file.read() == "some text"


def test_write_cwd(monkeypatch, tmpdir, donors):
    """write_cwd() User writes all emails to cwd."""
    # Check that the function indeed created 3 files ('cos there are 3 donors)
    # Check that the files created are not empty at least

    # This simulates the user entering "0" for quit on prompt
    # but I guess a class instance that I create remains in place
    # so I can test its methods
    builtins.input = Mock()
    builtins.input.side_effect = ["0"]

    # Captures all print statements the class object generates, into a mock object
    with mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        # Instantitate a class object (though in reality this class never gets
        # assigned to a name)
        s = StartMenu(donors)
        # This checks the self.donors property
        assert "Bill Murray" in s.donors

        # This fakes cwd by substituting it for a temp dir
        monkeypatch.chdir(tmpdir)

        # Test a method that writes letters to all donors. Should create 3 files
        s.write_cwd()
        assert len(tmpdir.listdir()) == 3

        # Check that all files in temp dir contain the word "Dear"
        for file in tmpdir.listdir():
            # assert "something " in file.read()  # Must fail
            assert "Dear " in file.read()

        # Check that the method executed its print statement
        assert "All letters saved in" in mock_stdout.getvalue()


def test_write_select_dir(monkeypatch, tmpdir, donors):
    """write_select_dir() User selects a directory."""
    # Check that the function indeed created 3 files ('cos there are 3 donors)
    # Check that the files created are not empty at least

    # This simulates the user entering "0" for quit on prompt
    # but I guess a class instance that I create later remains in place
    # so I can test its methods
    builtins.input = Mock()
    builtins.input.side_effect = ["0"]

    # Captures all print statements the class object generates, into a mock object
    with mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        # Instantitate a class object (though in reality this class never gets
        # assigned to a name)
        s = StartMenu(donors)

        # This fakes the user's choice of the directory
        s.ask_user_dir = Mock()
        s.ask_user_dir.return_value = tmpdir

        # Test a method that writes letters to all donors. Should create 3 files
        s.write_select_dir()
        assert len(tmpdir.listdir()) == 3

        # Check that all files in temp dir contain the word "Dear"
        for file in tmpdir.listdir():
            # assert "something " in file.read()  # Must fail
            assert "Dear " in file.read()

        # Check that the method executed its print statement
        assert "All letters saved in" in mock_stdout.getvalue()


def test_write_select_dir_user_cancel():
    """In write_select_dir() the user hits cancel."""
    # When the user hits cancel when asked to select a directory
    # Then the function should return
    # This mocks the __init__ method in the StartMenu class
    with patch.object(StartMenu, "__init__", lambda x, y: None):
        s = StartMenu(None)

        # This fakes the user's choice of the directory. User hits cancel
        s.ask_user_dir = Mock()
        s.ask_user_dir.return_value = ""

        assert s.write_select_dir() is None


def test_start_menu_user_choose_match_donations(donors):
    """User chooses to match all donations by a factor of 1."""
    # This simulates the user entering "0" to quit main_menu running at start,
    # but I guess a class instance that I create remains in place
    # so I can test its methods
    # Then I test the challenge() method, where the user types a factor of 1
    builtins.input = Mock()
    builtins.input.side_effect = ["0", "1"]  # Multiple calls

    # Captures all print statements the class object generates, into a mock object
    with mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        # Instantitate a class object (though in reality this class never gets
        # assigned to a name)
        s = StartMenu(donors)

        # Test that the challenge method correctly modifies self.donors
        s.challenge()
        assert s.donors.get_donor("Bill Murray").donations == [250, 2]
        assert s.donors.get_donor("Woody Harrelson").donations == [143, 2.5]
        assert s.donors.get_donor("Jesse Eisenberg").donations == [199.98, 3.5]

        # Test that the create_report contains the correct sums
        s.donors.create_report()
        assert "252" in mock_stdout.getvalue()
        assert "145.5" in mock_stdout.getvalue()


def test_start_menu_user_choose_match_donations_wrong_inputs():
    """Test StartMenu.challenge() for a number of invalid inputs."""
    # On the first prompt to enter a number, the user enters "A"
    #     The method prints "Input must be a number".
    # Then, on the next prompt, the user enters "0.5".
    #     The method prints "Input must not be less than 1"
    # Then the user enters 0 to quit.
    #     So the method returns False.

    # This mocks the __init__ method in the StartMenu class
    with patch.object(StartMenu, "__init__", lambda x, y: None):
        s = StartMenu(None)

        # This simulates the user entering "A", then "0.5", then "0" on prompts
        builtins.input = Mock()
        builtins.input.side_effect = ["A", "0.5", "0"]

        # This captures all print statements into a mock object
        with mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            res = s.challenge()

            #  The method should generate the following print statements
            assert "Input must be a number" in mock_stdout.getvalue()
            assert "Input must not be less than 1" in mock_stdout.getvalue()

            #  These statements should be in the following order
            assert mock_stdout.getvalue().index("number") < mock_stdout.getvalue().index("less than")

            # The method must return False when user enters 0 to quit
            assert res is False
