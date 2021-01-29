def get_years(dataset):
    """

    Args:
        dataset ([type]): [description]

    Returns:
        [type]: [description]
    """
    years = []
    if dataset is not []:
        for row in dataset:
            if row[0].year not in years:
                years.append(row[0].year)
    return years


def get_data_by_year(year_input, dataset):
    """

    Args:
        year_input ([type]): [description]
        dataset ([type]): [description]

    Returns:
        [type]: [description]
    """
    year_dataset = []
    if dataset is not []:
        for row in dataset:
            if row[0].year == year_input:
                year_dataset.append(row)
    return year_dataset


def get_total_expenses(dataset):
    """

    Args:
        dataset ([type]): [description]

    Returns:
        [type]: [description]
    """
    total_expenses = 0
    if dataset is not []:
        for row in dataset:
            if row[2] < 0:
                total_expenses += row[2]
    return total_expenses


def get_total_incomes(dataset):
    """

    Args:
        dataset ([type]): [description]

    Returns:
        [type]: [description]
    """
    total_incomes = 0
    if dataset is not []:
        for row in dataset:
            if row[2] > 0:
                total_incomes += row[2]
    return total_incomes
