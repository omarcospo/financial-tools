# Importing necessary modules.
import os
import sys
import csv
import random
import pandas as pd
from faker import Faker

# Reading file
csv_file = "cashflow.csv"
file_exists = os.path.isfile(csv_file)

# TODO: Which informations I need in my cashflow
# - date, description, category, amount, payment, account, client
column_headers = [
    "date",
    "description",
    "category",
    "amount",
    "type",
    "payment",
    "account",
    "client",
]


def get_user_input(prompt):
    return input(prompt)


def add_transaction():
    """
    Purpose: Add a transaction to csv database.
    """
    with open(csv_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(column_headers)
        new_row = []
        for header in column_headers:
            in_value = get_user_input(f"{header.capitalize()}: ").capitalize()
            new_row.append(in_value)
        writer.writerow(new_row)
        print("\033[H\033[J", end="")
        print("\033[0;32m--- Transaction added successfully.")


def generate_data():
    """
    Purpose: Generate a random database to work with.
    """
    fake = Faker()
    num_entries = 250
    with open(csv_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(column_headers)
        for _ in range(num_entries):
            entry = [
                fake.date_between(start_date="-365d", end_date="today"),  # date
                fake.sentence(nb_words=3),  # description
                random.choice(
                    [
                        "Sales",
                        "Utilities",
                        "Supplies and Materials",
                        "Advertising and Marketing",
                        "Taxes",
                        "Insurance",
                        "Professional Services",
                        "Research and Development",
                    ]
                ),
                round(random.uniform(5, 1000), 2),  # amount
                random.choice(["Credit", "Debit"]),  # type
                random.choice(["Cash", "Credit Card", "Debit Card"]),  # payment
                random.choice(["Bank XYZ", "Bank Frugal"]),  # account
                fake.company(),  # client
            ]
            writer.writerow(entry)
        print(
            f"\033[0;32m--- CSV database with {num_entries} random entries created in {csv_file}."
        )


def generate_balance_sheet():
    """
    Purpose: Generate a balance sheet based on the cashflow.
    """
    category_sums = {}
    balance_file = "balance_sheet.csv"
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['type'] == 'Debit':
                category = row['category']
                amount = float(row['amount'])
                if category not in category_sums:
                    category_sums[category] = 0.0
                category_sums[category] += amount
    with open(balance_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Category", "Debit", "Credit"])
        for category, total in category_sums.items():
            writer.writerow([category, total])
        print("\033[0;32m--- Balance sheet created.")


if len(sys.argv) < 2:
    print("\033[0;31mUsage:\033[0m python main.py [command]\n")
    print("\033[0;31madd - \033[0mAdd a transaction to database")
    print("\033[0;31mgenerate - \033[0mGenerate a database with random data")
    print("\033[0;31mbalance - \033[0mGenerate a balance sheet based on the cashflow")
else:
    action = sys.argv[1]
    if action == "add":
        add_transaction()
    elif action == "generate":
        generate_data()
    elif action == "balance":
        generate_balance_sheet()
