""" Create pdf files for teritroies. """

import re
from fpdf import FPDF


def truncate(str):
    """ Truncate a string. """
    if(len(str) > 22):
        return str[:22] + '...'

    return str


def make_pdf(items, out):
    """ Create pdfs from *.csv file. """
    document = FPDF(orientation="P", unit="mm", format="A4")
    document.add_page()
    document.set_font('helvetica', size=12)
    document.set_auto_page_break(False)

    line_height = document.font_size * 2.5
    phone_reqex = re.compile(r"(\d{3})(\d{3})(\d{4})")

    for index in range(0, len(items), 3):

        if index != 0 and index % 24 == 0:
            document.add_page()

        for idx in range(3):
            i = index + idx

            if(i < len(items)):
                document.multi_cell(
                    w=65,
                    h=10,
                    txt="{name}\n{address}\n{phone}".format(
                        name=truncate(f"{items[i].first} {items[i].last}"),
                        address=truncate(items[i].address),
                        phone=phone_reqex.sub(r'\1-\2-\3', items[0].phone)
                    ),
                    ln=3,
                    border=1)

        document.ln(line_height*3)

    document.output(out)
