from pytest import mark
from datetime import datetime
from moneytoring.query import get_data_by_year, get_total_expenses, get_total_incomes, get_years


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


@mark.parametrize('dataset', [[
    [datetime.now(), "CARTE", -11.11, "M DUPONT"],
    [datetime.now(), "CARTE", 11.11, "M DUPONT"],
    [datetime.now(), "CARTE", -11.11, "M DUPONT"]
]])
def test_valid_total_expenses(dataset):
    try:
        assert get_total_expenses(
            dataset) == -22.22, f"Wrong total : {get_total_expenses(dataset)}"
    except Exception:
        assert False


@ mark.parametrize('dataset', [[
    [datetime.now(), "CARTE", -11.11, "M DUPONT"],
    [datetime.now(), "CARTE", 11.11, "M DUPONT"],
    [datetime.now(), "CARTE", -11.11, "M DUPONT"]
]])
def test_valid_total_incomes(dataset):
    try:
        assert get_total_incomes(
            dataset) == 11.11, f"Wrong total : {get_total_incomes(dataset)}"
    except Exception:
        assert False


@mark.parametrize('dataset', [[
    [datetime(year=2020, month=10, day=22), "CARTE", -11.11, "M DUPONT"],
    [datetime(year=2020, month=10, day=22), "CARTE", 11.11, "M DUPONT"],
    [datetime(year=2019, month=10, day=22), "CARTE", -11.11, "M DUPONT"]
]])
def test_filter_by_year(dataset):
    assert get_data_by_year("année", dataset) == []
    assert get_data_by_year("2020", dataset) == []
    assert get_data_by_year(1, dataset) == []
    assert len(get_data_by_year(2020, dataset)) == 2
    assert len(get_data_by_year(2019, dataset)) == 1


@mark.parametrize('dataset', [[
    [datetime(year=2020, month=10, day=22), "CARTE", -11.11, "M DUPONT"],
    [datetime(year=2020, month=7, day=22), "CARTE", -11.11, "M DUPONT"],
    [datetime(year=2019, month=10, day=22), "CARTE", 11.11, "M DUPONT"],
    [datetime(year=2018, month=10, day=22), "CARTE", -11.11, "M DUPONT"],
    [datetime(year=2017, month=10, day=22), "CARTE", 11.11, "M DUPONT"]
]])
def test_get_year(dataset):
    assert get_years(dataset) == [2020, 2019, 2018, 2017]
