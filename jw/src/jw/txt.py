""" Work with txt data. """

import re


def extract_data(path, headerReg):
    """ Extract data from txt. """
    from . import Phone

    with open(path, 'r', encoding='utf8') as f:
        txt = f.read()
        list = txt.split('\n')  # [:10]
        filter = [t for t in list if not re.search(
            headerReg, t) and t != '']

        items = []
        for idx in range(0, len(filter), 3):
            names = filter[idx].split(',')
            address = filter[idx+1]
            phone = filter[idx+2]

            if(not re.search(r"^\d{3}-\d{3}-\d{4}", phone)):
                raise Exception(
                    f"names:{names} address:{address} phone:{phone}")

            items.append(
                Phone(names[-1], " ".join(names[:-1]), address, phone))

        return items
