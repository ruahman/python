"""Work with txt data."""

import re


def extract_phone(path, skipList=[]):
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

        def is_phone(txt):
            if(re.search(r"^\d{3}-\d{3}-\d{4}", txt)):
                return True
            return False

        indexes = []
        for idx in range(0, len(filtered)):
            if(is_phone(filtered[idx])):
                indexes.append(idx)

        phones = []
        for idx in indexes:
            names = filtered[idx - 2].split(',')
            address = filtered[idx - 1]
            phone = filtered[idx]

            first = names[-1] if not is_phone(names[-1]) else 'n/a'
            last = " ".join(
                names[:-1]) if not is_phone(" ".join(names[:-1])) else 'n/a'
            address = address if not is_phone(address) else 'n/a'

            phones.append(
                Phone(first, last, address, phone))

        return phones
