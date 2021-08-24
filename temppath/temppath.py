# vim: expandtab tabstop=4 shiftwidth=4

from contextlib import contextmanager
from pathlib import Path, _windows_flavour, _posix_flavour
#from pathlib import Path
from random import choice
from string import ascii_letters, digits
from tempfile import gettempdir

import os

def make_rand_name(length: int=15) -> str:
    return choice(ascii_letters) + ''.join([choice(ascii_letters+digits) for i in range(length-1)])

class TemporaryPath2(Path):
    _flavour = _windows_flavour if os.name == 'nt' else _posix_flavour

    def __init__(self) -> None:
        print('init called')
        path_str = str(Path(gettempdir()).joinpath(make_rand_name()))
        Path.__new__(Path, path_str)

    def __enter__(self) -> Path:
        print('enter called')
        self.path = Path(gettempdir()).joinpath(make_rand_name())  # pylint: disable=W0201
        self.path.touch()
        return self.path

    def __exit__(self, exc_type, exc_value, exc_traceback) -> None:
        print('exit called')
        self.path.unlink()

@contextmanager
def TemporaryPath():
    path = Path(gettempdir()).joinpath(make_rand_name())  # pylint: disable=W0201

    try:
        path.touch()
        yield path
    finally:
        path.unlink()
