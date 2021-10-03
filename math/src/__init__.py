"""Init with some script."""
from subprocess import call


def start():
    """Start jupeter notes."""
    print("start jupeter notes")
    call(["jupyter", "notebook", "--port=8888", "--no-browser"])
