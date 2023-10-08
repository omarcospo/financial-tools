![Python](http://ForTheBadge.com/images/badges/made-with-python.svg)

**Project Overview**

This Python project is designed for managing cashflow data and offers several useful features.

**Usage**

To get started with the project, simply run the main file without any arguments. You will receive instructions on how to use it:
``` shell
python main.py
```

**Features**

- [X] **Generate Random CSV Cashflow Database:** You can create a random CSV cashflow database for testing purposes. This feature is helpful when you need sample data to work with.

- [X] **Add Transactions:** The project allows you to add transactions to the cashflow database. This functionality helps you keep track of income and expenses.

- [ ] **Generate Balance Sheet:** Although this feature is currently a work in progress, the project aims to generate a balance sheet based on the cashflow data. This can be incredibly useful for assessing your financial position.

- [ ] **Linear Regression Cashflow Prediction:** While not yet implemented, there are plans to incorporate a cashflow prediction feature using linear regression. This will enable you to forecast cashflow for the next year, helping with financial planning.

**Libraries used**

This project utilizes several Python libraries to implement its functionality:

- `os`: Used for checking the existence of files.
- `sys`: Makes it possible to run the python file with arguments.
- `csv`: Used for reading and writing CSV files.
- `pandas`: A powerful data manipulation library that is employed for data processing and analysis.
- `random`: Used to generate random data, including numbers.
- `Faker`: Utilized to generate fake data, which can be helpful for testing and creating sample transactions.

Make sure to install these libraries if they are not already installed in your Python environment by using the appropriate package manager, such as `pip`:

```shell
pip install pandas faker
```
