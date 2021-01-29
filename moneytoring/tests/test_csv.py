from pytest import mark, fixture
from os import path, remove
from moneytoring.csv import setup_csv
from sys import argv


@fixture
def get_dummy_csv_file_path():
    file_path = path.join(path.dirname(__file__), "utils/dummy.csv")
    return file_path


def test_setup_csv(get_dummy_csv_file_path):
    try:
        setup_csv(path=get_dummy_csv_file_path)
        assert path.exists(path.join(path.dirname(
            path.dirname(__file__)), "transactions.csv"))
        remove(path.join(path.dirname(
            path.dirname(__file__)), "transactions.csv"))
    except Exception:
        assert False


def test_wrong_path():
    try:
        setup_csv(path="path/to/nowhere")
    except FileNotFoundError:
        expected_path = path.join(path.dirname(
            path.dirname(__file__)), "transactions.csv")
        assert not path.exists(expected_path)


def test_no_path():
    try:
        setup_csv()
        assert False
    except FileNotFoundError:
        assert True
