"""Commands to run from poetry."""
import os
import glob


def start():
    """Run command to read from text and generate csv and pdf."""
    # clear cvs
    for f in glob.glob('./data/csv/export/*'):
        os.remove(f)

    # clear pdf
    for f in glob.glob('./data/pdf/export/*'):
        os.remove(f)

    # create pdfs
