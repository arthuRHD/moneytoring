from pytest import mark, fixture
from moneytoring.commandline import summary, help_cmd, yearly_summary
from moneytoring.parser import get_parsed_data
from .test_query import get_dataset_with_multiple_years, get_empty_dataset
from .test_parser import setup_csv_fixture


def test_summary_execution(setup_csv_fixture):
    assert summary()
    assert summary(parsed_dataset=[])


def test_help_execution(setup_csv_fixture):
    assert help_cmd()


@mark.parametrize('year', [
    "all",
    "2020",
    "2019",
    "2018",
    "2017",
])
def test_summary_yearly_working(year, get_dataset_with_multiple_years, setup_csv_fixture):
    dataset = get_dataset_with_multiple_years
    try:
        assert yearly_summary(year_input=year, parsed_dataset=dataset)
    except Exception:
        assert False


@mark.parametrize('year', [
    "19999",
    "fzefzgz",
    "lla",
    "&&&",
])
def test_summary_yearly_not_working(year, get_dataset_with_multiple_years, setup_csv_fixture):
    dataset = get_dataset_with_multiple_years
    try:
        assert yearly_summary(year_input=year, parsed_dataset=dataset)
    except Exception:
        assert False


def test_summary_with_empty_dataset(get_empty_dataset, setup_csv_fixture):
    dataset = get_empty_dataset
    try:
        yearly_summary(year_input="2020", parsed_dataset=dataset)
        assert False
    except Exception:
        assert True
