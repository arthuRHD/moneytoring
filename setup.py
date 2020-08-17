from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="budget",  # Replace with your own username
    version="0.1.0",
    author="Arthur RICHARD",
    author_email="arthur.richard@protonmail.com",
    description="A python budgeting tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arthuRHD/budget",
    packages=['budget'],
    package_data={
        "": ["*.csv"]
    },
    python_requires='>=3.6',
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'setup-csv=budget:setup_csv',
            'summary=budget.commandline:summary',
            'summary-year=budget.commandline:yearly_summary',
            'summary-filter=budget.commandline:filter_dest',
            'budget=budget.commandline:report_budget',
            'budget-help=budget.commandline:help_cmd'

        ]
    }
)
