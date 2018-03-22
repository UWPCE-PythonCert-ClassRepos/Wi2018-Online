"""Provide pytest unit tests for the oo-mailroom assignment."""
import pytest
import builtins
import datetime
from io import StringIO
from unittest import mock
from unittest.mock import Mock

import mailroom


@pytest.fixture()
def donors():
    """Provide a data structure for the tests."""
    mailroom.donors = {"A": [1, 2, 3], "B": [3, 4, 5]}
    return mailroom.donors


def test_create_report(donors):
    """Test that the create_report contains the correct sums at least."""
    with mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        mailroom.create_report(donors)
        assert "6" in mock_stdout.getvalue()
        assert "12" in mock_stdout.getvalue()


def test_load_donors():
    """Test that it returns the right type."""
    assert type(mailroom.load_donors()) == dict


def test_add_new_donor_donation(donors):
    """add_donation(name, amount) for a new donor."""
    mailroom.add_donation(donors, "Alex Skrn", 0.0)
    assert mailroom.donors["Alex Skrn"] == [0.0]


def test_add_exist_donor_donation(donors):
    """add_donation(name, amount) for an existing donor."""
    mailroom.add_donation(donors, "A", 1000.0)
    assert mailroom.donors["A"][-1] == 1000.0


def test_get_last_donation(donors):
    """get_last_donation(name) for a given donor."""
    assert mailroom.get_last_donation(donors, "B") == 5


def test_get_donations(donors):
    """get_donations(name) for a given donor."""
    assert mailroom.get_donations(donors, "A") == [1, 2, 3]


def test_get_total_given(donors):
    """get_total_given(name) for a given donor."""
    assert mailroom.get_total_given(donors, "B") == 12


def test_sort_donors_by_total(donors):
    """sort_donors_by_total()."""
    assert mailroom.sort_donors_by_total(donors) == ["B", "A"]


def test_print_donor_names(capsys, donors):
    """print_donor_names()."""
    mailroom.print_donor_names(donors)
    out, _ = capsys.readouterr()
    assert out == "\nA, B\n"


def test_get_email():
    """get_email(name, amount)."""
    result = ("""\nDear A,\n
                  \nI would like to thank you for your donation of $100.\n
                  \nWe appreciate your support.\n
                  \nSincerely,\n
                  \nThe Organization\n
                  """)
    assert mailroom.get_email("A", 100) == result


def test_input_donation_zero(monkeypatch):
    """input_donation(name) with the user typing zero."""
    monkeypatch.setattr('builtins.input', lambda _: "0")
    assert mailroom.input_donation(donors, "A") is False


def test_input_donation_number(monkeypatch, donors):
    """input_donation(name) with the user typing a valid number (> 0)."""
    monkeypatch.setattr('builtins.input', lambda _: "300")
    assert mailroom.input_donation(donors, "A") is True
    assert mailroom.donors["A"][-1] == 300


def test_old_donor_interaction_user_input_zero(donors, monkeypatch):
    """_old_donor_interaction() user enters zero on prompt."""
    monkeypatch.setattr('builtins.input', lambda _: "0")
    assert mailroom.old_donor_interaction(donors) is False


def test_new_donor_interaction_user_input_zero(donors, monkeypatch):
    """new_donor_interaction() user enters 0 on promp."""
    monkeypatch.setattr('builtins.input', lambda _: "0")
    assert mailroom.old_donor_interaction(donors, old=False) is False


def test_new_donor_interaction_user_input_name(donors, monkeypatch, capsys):
    """new_donor_interaction(); User enters a new name on prompt."""
    # WHEN the user enters a name when prompted to enter a name
    # THEN the function should print a thank-you email
    monkeypatch.setattr('builtins.input', lambda _: "Any_name")

    # Fake all functions inside any_donor()
    mailroom.input_donation = Mock()
    mailroom.input_donation.return_value = True

    mailroom.get_email = Mock()
    mailroom.get_email.return_value = "some_text"

    mailroom.get_last_donation = Mock()
    mailroom.get_last_donation.return_value = True

    mailroom.old_donor_interaction(donors, old=False)
    out, _ = capsys.readouterr()
    assert out.strip() == "some_text"


def test_old_donor_interaction_user_input_name(monkeypatch, capsys, donors):
    """old_donor_interaction(); User enters an old name on prompt."""
    # WHEN the user enters an old name when prompted to enter a name
    # THEN the function should print a thank-you email
    monkeypatch.setattr('builtins.input', lambda _: "B")

    # Fake all functions inside any_donor()
    mailroom.input_donation = Mock()
    mailroom.input_donation.return_value = True

    mailroom.get_email = Mock()
    mailroom.get_email.return_value = "some_text"

    mailroom.get_last_donation = Mock()
    mailroom.get_last_donation.return_value = True

    mailroom.old_donor_interaction(donors)
    out, _ = capsys.readouterr()
    assert out.strip() == "some_text"


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
    expected_path = tmpdir.join("2020-12-25-Alex Skrn.txt")
    assert mailroom.get_full_path(tmpdir, "Alex Skrn") == expected_path


def test_write_file(tmpdir):
    """write_file(path, text)."""
    file = tmpdir.join('output.txt')
    mailroom.write_file(file.strpath, "some text")  # or str(file)
    assert file.read() == "some text"


def test_write_cwd(monkeypatch, tmpdir, capsys, donors):
    """write_cwd() User writes all emails to cwd."""
    # Check that the final print statement in the function is okey
    # Check that the function indeed created 2 files ('cos only 2 donors now)
    # Check that the files created are not empty at least
    monkeypatch.chdir(tmpdir)
    mailroom.write_cwd(donors)
    out, _ = capsys.readouterr()  # out has an extra \n, hence .strip() below
    expected = ("\nAll letters saved in {}\n".format(str(tmpdir))).strip()
    assert out.strip() == expected
    assert len(tmpdir.listdir()) == 2
    for file in tmpdir.listdir():
        assert bool(file.read()) is True


def test_write_select_dir(tmpdir, capsys, donors):
    """write_select_dir(). User selects a directory."""
    # Check that the print statement in the function is okey
    # Check that the function indeed created 2 files
    # Check that the files created are not empty at least
    mailroom.ask_user_dir = Mock()
    mailroom.ask_user_dir.return_value = tmpdir

    mailroom.write_select_dir(donors)
    out, _ = capsys.readouterr()
    expected = ("\nAll letters saved in {}\n".format(str(tmpdir))).strip()
    assert out.strip() == expected
    assert len(tmpdir.listdir()) == 2
    for file in tmpdir.listdir():
        assert bool(file.read()) is True


def test_write_select_dir_user_cancel(donors):
    """In write_select_dir() the user hits cancel."""
    # When the user hits cancel when asked to select a directory
    # Then the function should return

    # Fake a function inside write_select_dir()
    mailroom.ask_user_dir = Mock()
    mailroom.ask_user_dir.return_value = ""

    assert mailroom.write_select_dir(donors) is None


@pytest.mark.parametrize('factor, minim, maxim, exception',
                         [(0, None, None, ValueError),
                          (0.41, None, None, ValueError),
                          (1, None, None, ValueError),
                          (-1, None, None, ValueError),
                          (-3.5, None, None, ValueError),
                          ("a", None, None, ValueError),
                          (2, 100, 50, ValueError),
                          (2, "a", None, ValueError),
                          (2, None, "a", ValueError),
                          ]
                         )
def test_multiplier_factory_wrong_inputs(factor, minim, maxim, exception):
    """Must raise ValueError if imputs are wrong."""
    with pytest.raises(exception):
        mailroom.multiplier_factory(factor, minim, maxim)


@pytest.mark.parametrize('factor, minim, maxim, value, expected',
                         [(2, None, None, 4, 8),
                          (2, 10, None, 4, 4),
                          (2, None, 10, 12, 12),
                          (2, 10, None, 15, 30),
                          (2, None, 10, 5, 10),
                          ]
                         )
def test_multiplier_factory_in_use(factor, minim, maxim, value, expected):
    """Pass a number of good inputs and evalute result at value."""
    assert mailroom.multiplier_factory(factor, minim, maxim)(value) == expected


@pytest.mark.parametrize('factor, minim, maxim, projection, expected',
                         [(2, None, None, True, int),
                          (2, 10, None, False, dict),
                          ]
                         )
def test_do_challenge(donors, factor, minim, maxim, projection, expected):
    """See that the type of return value is correct at least."""
    assert type(mailroom.do_challenge(donors,
                                      factor,
                                      minim,
                                      maxim,
                                      projection)) == expected



@pytest.mark.parametrize('user_input, expected',
                         [("", None),
                          (0, False),
                          (100, 100),
                          ]
                         )
def test_validate_user_input(user_input, expected):
    """Test several user input cases - function return some values."""
    # Simulates the user entering some values
    builtins.input = Mock()
    builtins.input.return_value = user_input

    assert mailroom.validate_user_input("Some message") == expected


def test_validate_user_input_wrong_input():
    """User inputs a negative factor, then 0 to quit"""
    # Simulates the user entering a series of values on prompts
    builtins.input = Mock()
    builtins.input.side_effect = [-1, 0]

    # Capture output
    with mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        mailroom.validate_user_input("Some message", factor=True)
        assert "Factor must be greater than 1" in mock_stdout.getvalue()




# ###############################
# # TESTS FOR THE STARTMENU CLASS
# ###############################
# def test_menu_selection_user_quits(monkeypatch):
#     """Test menu_selection(). The user quits."""
#     # This mocks the __init__ method in the StartMenu class
#     # https://medium.com/@george.shuklin/mocking-complicated-init-in-python-6ef9850dd202
#     with patch.object(StartMenu, "__init__", lambda x, y: None):
#         s = StartMenu(None)
#
#         # User is prompted to enter something when the main menu is displayed
#         # But chooses the option to quit immediately.
#         # The line below simulates the user entering "125" in the terminal
#         # This value "125" is arbitrary
#         monkeypatch.setattr('builtins.input', lambda _: "125")
#
#         # Now fake all methods that the menu_selection would call:
#         # Fake the main dispatch dict
#         s.main_dispatch = Mock()
#         # This assigns the key "125" the value "s.quit" in the dispatch dict
#         s.main_dispatch.return_value = {"125": s.quit}
#
#         # Fake quit() which would be called by main_dispatch()
#         s.quit = Mock()
#         s.quit.return_value = "exit menu"
#
#         assert s.menu_selection("prompt", s.main_dispatch()) is None
#
#
# def test_quit():
#     """Test the quit() method."""
#     # This mocks the __init__ method in the StartMenu class
#     with patch.object(StartMenu, "__init__", lambda x, y: None):
#         s = StartMenu(None)
#
#         assert s.quit() == "exit menu"
#
#
@pytest.mark.parametrize("user_input, expected",
                         [("1", None),
                          ("2", None),
                          ("3", None),
                          ("wrong_input", None),
                          ("", None),
                          ]
                         )
def test_main_menu_user_quits(donors, user_input, expected):
    """User types some of menu options, including wrong ones."""
    # Fake reurn values for functions inside
    mailroom.send_thank_you_sub_menu = Mock()
    mailroom.send_thank_you_sub_menu.return_value = False

    mailroom.create_report = Mock()
    mailroom.create_report.return_value = False

    mailroom.send_all_sub_menu = Mock()
    mailroom.send_all_sub_menu.return_value = False

    # mailroom.challenge = Mock()
    # mailroom.challenge.return_value = False

    # mailroom.run_projection = Mock()
    # mailroom.run_projection.return_value = False

    # Simulate user input
    builtins.input = Mock()
    builtins.input.side_effect = [user_input, "0"]
    # Capture output
    with mock.patch('sys.stdout', new_callable=StringIO):
        assert mailroom.main_menu(donors) is expected


@pytest.mark.parametrize('inputs',
                         [([False]),
                          ([None, False]),
                          ([None, None, False]),
                          ]
                         )
def test_challenge_false(donors, inputs):
    """Internal function returns False and the function itself returns."""
    # Fake a function inside challenge
    mailroom.validate_user_input = Mock()
    mailroom.validate_user_input.side_effect = inputs

    # Captures all print statements
    with mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        assert mailroom.challenge(donors, projection=True) is False
        assert "(This is a projection)" in mock_stdout.getvalue()


def test_challenge_proper_input(donors):
    """Internal function returns False and the function itself returns."""
    # Fake a function inside challenge
    mailroom.validate_user_input = Mock()
    mailroom.validate_user_input.return_value = False

    # Captures all print statements
    with mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        assert mailroom.challenge(donors, projection=True) is False
        assert "(This is a projection)" in mock_stdout.getvalue()


@pytest.mark.parametrize('inputs, value, expected',
                         [([2, 100], True, int),
                          ([2, 100], False, dict),
                          ([2, None, 100], False, dict),
                          ]
                         )
def test_challenge_proper_input(donors, inputs, value, expected):
    """Internal function returns a series of values. Main func returns right type"""
    # Fake a function inside challenge to return some values successively
    mailroom.validate_user_input = Mock()  # 2 for factor, 100 for min_donation
    mailroom.validate_user_input.side_effect = inputs

    assert type(mailroom.challenge(donors, projection=value)) == expected


def test_run_projection(donors):
    """Test that the function prints the statement."""
    # Mock a function inside
    mailroom.challenge = Mock()
    mailroom.challenge.return_value = 1

    # Captures all print statements
    with mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        mailroom.run_projection(donors)
        assert "Your contribution would total $" in mock_stdout.getvalue()
