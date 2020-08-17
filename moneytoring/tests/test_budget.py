from pytest import mark, fixture
from datetime import datetime
from moneytoring import get_data_by_year, get_total_expenses, get_total_incomes


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


def test_filter_by_year():
    assert get_data_by_year("année") == []
    assert get_data_by_year("2020") == []
    assert get_data_by_year(1) == []
    assert get_data_by_year(2020) != []
