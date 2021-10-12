"""Work with txt data."""

import re


def extract_phone(path, skipList):
    """Extract data from txt."""
    from . import Phone

    with open(path, 'r', encoding='utf8') as f:
        skipList.extend(['TERRITORY', '^$'])

        def skip(item):
            for regex in skipList:
                if re.search(regex, item, re.IGNORECASE):
                    return True
            return False

        filtered = [item for item in f.read().split('\n') if not skip(item)]

        phones = []
        for idx in range(0, len(filtered), 3):
            names = filtered[idx].split(',')
            address = filtered[idx+1]
            phone = filtered[idx+2]

            if(not re.search(r"^\d{3}-\d{3}-\d{4}", phone)):
                raise Exception(
                    f"names:{names} address:{address} phone:{phone}, line:{idx}")

            phones.append(
                Phone(names[-1], " ".join(names[:-1]), address, phone))

        return phones
