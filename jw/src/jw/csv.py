"""Handles csv logic."""

import csv
import re


def create_csv(items, path, territory):
    """Print content to a csv file."""
    phone_regex = re.compile(r'(\d{3})(\d{3})(\d{4})')
    with open(path, mode='w', encoding='cp1252') as f:
        fieldNames = ['Phone', 'First', 'Last',
                      'Address', 'Territory']
        writer = csv.DictWriter(f, fieldnames=fieldNames)
        writer.writeheader()
        for item in items:
            writer.writerow({
                'Phone': phone_regex.sub(r'\1-\2-\3', item.phone),
                'First': item.first,
                'Last': item.last,
                'Address': item.address.replace('\xa0', ''),
                'Territory': territory
            })


def get_items_from_csv(path):
    """Get items from csv file."""
    from . import Phone

    # with open(path, 'r', encoding='cp1252') as f:
    with open(path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        items = []
        for row in reader:
            # print(row)
            # items.append(row)
            items.append(
                # Phone(row['First'], row['Last'],
                #       row['Address'], row['Phone'])
                Phone(row["First Name"], row["Last Name"],
                      row["Address"], row["Phone Number"], row["Notes"])
            )
        return items
