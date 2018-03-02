"""Provide pytest unit tests for the mailroom assignment."""
import pytest
import datetime
from unittest.mock import Mock
import mailroom


@pytest.fixture()
def donors():
    """Provide a data structure for the tests."""
    mailroom.donors = {"A": [1, 2, 3], "B": [3, 4, 5]}
    return mailroom.donors


def test_add_new_donor_donation(donors):
    """add_donation(name, amount) for a new donor."""
    mailroom.add_donation("Alex Skrn", 0.0)
    assert mailroom.donors["Alex Skrn"] == [0.0]


def test_add_exist_donor_donation(donors):
    """add_donation(name, amount) for an existing donor."""
    mailroom.add_donation("A", 1000.0)
    assert mailroom.donors["A"][-1] == 1000.0


def test_get_last_donation(donors):
    """get_last_donation(name) for a given donor."""
    assert mailroom.get_last_donation("B") == 5


def test_get_donations(donors):
    """get_donations(name) for a given donor."""
    assert mailroom.get_donations("A") == [1, 2, 3]


def test_get_total_given(donors):
    """get_total_given(name) for a given donor."""
    assert mailroom.get_total_given("B") == 12


def test_sort_donors_by_total(donors):
    """sort_donors_by_total()."""
    assert mailroom.sort_donors_by_total() == ["B", "A"]


def test_print_donor_names(capsys, donors):
    """print_donor_names()."""
    mailroom.print_donor_names()
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
    assert mailroom.input_donation("A") is False


def test_input_donation_number(monkeypatch, donors):
    """input_donation(name) with the user typing a valid number (> 0)."""
    monkeypatch.setattr('builtins.input', lambda _: "300")
    assert mailroom.input_donation("A") is True
    assert mailroom.donors["A"][-1] == 300


def test_old_donor_interaction_user_input_zero(monkeypatch):
    """_old_donor_interaction() user enters zero on prompt."""
    monkeypatch.setattr('builtins.input', lambda _: "0")
    assert mailroom.old_donor_interaction() is None


def test_new_donor_interaction_user_input_zero(monkeypatch):
    """new_donor_interaction() user enters 0 on promp."""
    monkeypatch.setattr('builtins.input', lambda _: "0")
    assert mailroom.new_donor_interaction() is None


def test_new_donor_interaction_user_input_name(monkeypatch, capsys):
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

    mailroom.new_donor_interaction()
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

    mailroom.old_donor_interaction()
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
    mailroom.write_cwd()
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

    mailroom.write_select_dir()
    out, _ = capsys.readouterr()
    expected = ("\nAll letters saved in {}\n".format(str(tmpdir))).strip()
    assert out.strip() == expected
    assert len(tmpdir.listdir()) == 2
    for file in tmpdir.listdir():
        assert bool(file.read()) is True


def test_write_select_dir_user_cancel():
    """In write_select_dir() the user hits cancel."""
    # When the user hits cancel when asked to select a directory
    # Then the function should return

    # Fake a function inside write_select_dir()
    mailroom.ask_user_dir = Mock()
    mailroom.ask_user_dir.return_value = ""

    assert mailroom.write_select_dir() is None


def test_menu_selection_user_choice_quit(monkeypatch):
    """menu_selection(). User chooses to quit."""
    # User is prompted to enter something
    # But chooses the option to quit immediately
    monkeypatch.setattr('builtins.input', lambda _: "125")

    # Fake the dispatch dict
    mailroom.main_dispatch = Mock()
    mailroom.main_dispatch.return_value = {"125": mailroom.quit}

    # Fake quit()
    mailroom.quit = Mock()
    mailroom.quit.return_value = "exit menu"

    assert mailroom.menu_selection("prompt", mailroom.main_dispatch()) is None
