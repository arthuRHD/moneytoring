from pytest import mark, fixture
from datetime import datetime
from moneytoring.query import get_data_by_year, get_total_expenses, get_total_incomes, get_years


@fixture
def get_empty_dataset():
    return []


@fixture
def get_dataset_with_multiple_years():
    return [
        [datetime(year=2020, month=10, day=22), "CARTE", -11.11, "M DUPONT"],
        [datetime(year=2020, month=7, day=22), "CARTE", -11.11, "M DUPONT"],
        [datetime(year=2019, month=10, day=22), "CARTE", 11.11, "M DUPONT"],
        [datetime(year=2018, month=10, day=22), "CARTE", -11.11, "M DUPONT"],
        [datetime(year=2017, month=10, day=22), "CARTE", 11.11, "M DUPONT"]
    ]


@fixture(scope="module")
def get_dataset_year_filter():
    return [
        [datetime(year=2020, month=10, day=22), "CARTE", -11.11, "M DUPONT"],
        [datetime(year=2020, month=10, day=22), "CARTE", 11.11, "M DUPONT"],
        [datetime(year=2019, month=10, day=22), "CARTE", -11.11, "M DUPONT"]
    ]


@fixture(scope="module")
def get_dataset_total_calculus():
    return [
        [datetime.now(), "CARTE", -11.11, "M DUPONT"],
        [datetime.now(), "CARTE", 11.11, "M DUPONT"],
        [datetime.now(), "CARTE", -11.11, "M DUPONT"]
    ]


@mark.parametrize('dataset', [[["2020-10-22", "CARTE", 15.00, 'M DUPONT']], [[datetime.now(), "CARTE", 1, 'M DUPONT']]])
def test_wrong_total_expenses(dataset):
    try:
        get_total_expenses(dataset)
        assert False
    except Exception:
        assert True


@mark.parametrize('dataset', [[["2020-10-22", "CARTE", 15.00, 'M DUPONT']], [[datetime.now(), "CARTE", 1, 'M DUPONT']]])
def test_wrong_total_incomes(dataset):
    try:
        get_total_incomes(dataset)
        assert False
    except Exception:
        assert True


def test_valid_total_expenses(get_dataset_total_calculus):
    try:
        assert get_total_expenses(
            get_dataset_total_calculus) == -22.22, f"Wrong total : {get_total_expenses(get_dataset_total_calculus)}"
    except Exception:
        assert False


def test_valid_total_incomes(get_dataset_total_calculus):
    try:
        assert get_total_incomes(
            get_dataset_total_calculus) == 11.11, f"Wrong total : {get_total_incomes(get_dataset_total_calculus)}"
    except Exception:
        assert False


def test_filter_by_year(get_dataset_year_filter):
    dataset = get_dataset_year_filter
    assert len(get_data_by_year(2020, dataset)) == 2
    assert len(get_data_by_year(2019, dataset)) == 1


def test_wrong_year_input_int(get_dataset_year_filter):
    dataset = get_dataset_year_filter
    assert get_data_by_year(1, dataset) == []


def test_wrong_year_input_string(get_dataset_year_filter):
    dataset = get_dataset_year_filter
    assert get_data_by_year("année", dataset) == []
    assert get_data_by_year("2020", dataset) == []


def test_get_years(get_dataset_with_multiple_years):
    assert get_years(get_dataset_with_multiple_years) == [
        2020, 2019, 2018, 2017]


def test_empty_return_get_years(get_empty_dataset):
    assert get_years(get_empty_dataset) == []


def test_empty_return_get_data_by_year(get_empty_dataset):
    assert get_data_by_year("2020", get_empty_dataset) == []


def test_empty_return_get_total_incomes(get_empty_dataset):
    assert get_total_incomes(get_empty_dataset) == 0


def test_empty_return_get_total_expenses(get_empty_dataset):
    assert get_total_expenses(get_empty_dataset) == 0
