from .query import *
import sys
import os


def help_cmd():
    print("help command")
    pass


def filter_dest():
    print("filter by dest command")
    pass


def report_budget():
    salary_input = float(sys.argv[1].replace(",", '.'))
    month_count = int(sys.argv[2])
    money_left = 1419.67
    for i in range(month_count):
        print(f"----------- Month n°{i+1} ------------")
        money_left += salary_input
        print(
            f"\033[92m++ Salary : {salary_input} €\033[0m ==> Money left : \033[93m{round(money_left, 2)} €\033[0m")
        food_expenses = round((salary_input * 26)/100, 2)
        money_left -= food_expenses
        print(
            f"\033[91m-- Food : {food_expenses} €\033[0m ==> Money left : \033[93m{round(money_left, 2)} €\033[0m")
        money_left -= 150
        print(
            f"\033[91m-- Home : 150 €\033[0m ==> Money left : \033[93m{round(money_left, 2)} €\033[0m")
        money_left -= 275
        print(
            f"\033[91m-- Cofidis : 275 €\033[0m ==> Money left : \033[93m{round(money_left, 2)} €\033[0m")


def yearly_summary():
    year_input = sys.argv[1]
    if year_input == "all":
        for year in get_years():
            print("--------------------")
            print(
                f"Dépensé en {str(year)} : \033[91m{round(get_total_expenses(get_data_by_year(year)),2)} €\033[0m")
            print(
                f"Obtenu en {str(year)} : \033[92m{round(get_total_incomes(get_data_by_year(year)), 2)} €\033[0m")
    else:
        print(
            f"Dépensé en {str(year_input)} : \033[91m{round(get_total_expenses(get_data_by_year(int(year_input))),2)} €\033[0m")
        print(
            f"Obtenu en {str(year_input)} : \033[92m{round(get_total_incomes(get_data_by_year(int(year_input))), 2)} €\033[0m")


def summary():
    print(
        f"Total dépensé : \033[91m{round(get_total_expenses(parsed_dataset), 2)} €\033[0m")
    print(
        f"Total obtenu : \033[92m{round(get_total_incomes(parsed_dataset), 2)} €\033[0m")
