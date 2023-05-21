import sys

from jw.csv import get_items_from_csv
from jw.pdf import make_pdf_from_items


input = sys.argv[1]
output = sys.argv[2]
title = sys.argv[3]

items = get_items_from_csv(input)
# print(items)
make_pdf_from_items(items, title, output)
