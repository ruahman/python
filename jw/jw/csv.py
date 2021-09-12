""" Handles csv logic. """

import csv


def print_csv(items, path):
    """ Print content to a csv file. """
    with open(path, mode='w') as f:
        fieldNames = ['first', 'last', 'address', 'phone']
        writer = csv.DictWriter(f, fieldnames=fieldNames)
        writer.writeheader()
        for item in items:
            writer.writerow({
                'first': item.first,
                'last': item.last,
                'address': item.address.replace('\xa0', ''),
                'phone': item.phone
            })


def get_items_from_csv(path):
    """ Get items from csv file. """
    from . import Phone

    with open(path, 'r') as f:
        reader = csv.DictReader(f)
        items = []
        for row in reader:
            items.append(
                Phone(row['first'], row['last'], row['address'], row['phone'])
            )
        return items
