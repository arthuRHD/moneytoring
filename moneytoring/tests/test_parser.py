from pytest import fixture
from moneytoring.parser import get_csv_file_path, get_reader, get_parsed_data
from os import path, remove
from moneytoring.csv import setup_csv


@fixture(scope="module")
def setup_csv_fixture():
    dummyfile = path.join(path.dirname(__file__), "utils/dummy.csv")
    setup_csv(dummyfile)
    yield
    remove(path.join(path.dirname(
        path.dirname(__file__)), "transactions.csv"))


def test_before_type_pathway():
    assert isinstance(get_csv_file_path(), str)


def test_before_get_csv_file_path():
    assert not path.exists(get_csv_file_path())


def test_directory_existence():
    assert path.isdir(path.dirname(get_csv_file_path()))


def test_before_get_reader_type():
    assert isinstance(get_reader(), type(None))


def test_before_get_parsed_data():
    assert get_parsed_data() == []


def test_after_type_pathway(setup_csv_fixture):
    assert isinstance(get_csv_file_path(), str)


def test_after_get_csv_file_path(setup_csv_fixture):
    assert path.exists(get_csv_file_path())


def test_after_get_reader_type(setup_csv_fixture):
    assert not isinstance(get_reader(), type(None))


def test_after_get_parsed_data(setup_csv_fixture):
    assert get_parsed_data() != []
