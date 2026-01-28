import argparse
import codecs
import sys
from contextlib import contextmanager

from cutpaste.version import version


def decode_escapes(s):
    """Decode escape sequences like \\t, \\n in a string."""
    return codecs.decode(s, "unicode_escape")


def parse_fields(field_spec):
    """
    Parse field specification into a list of 0-based indices.

    Supports:
    - Single field: "1" -> [0]
    - Multiple fields: "1,3" -> [0, 2]
    - Ranges: "1-3" -> [0, 1, 2]
    - Mixed: "1,3-5,7" -> [0, 2, 3, 4, 6]

    Fields are 1-based in input (like Unix cut), converted to 0-based indices.
    """
    indices = []
    for part in field_spec.split(","):
        part = part.strip()
        if "-" in part:
            start, end = part.split("-", 1)
            start = int(start)
            end = int(end)
            indices.extend(range(start - 1, end))
        else:
            indices.append(int(part) - 1)
    return indices


@contextmanager
def open_file(path):
    """
    Context manager that yields a file-like object for reading.
    If path is "-", yields stdin. Otherwise opens the file.
    """
    if path == "-":
        yield sys.stdin
    else:
        f = open(path)
        try:
            yield f
        finally:
            f.close()


def parse_args(prog):
    p = get_parser(prog)
    args = p.parse_args()
    return args


def get_parser(prog):
    p = get_common_parser(prog)
    if prog == "pycut":
        p.add_argument("-f", "--field", required=True, help="fields to select")
    return p


def get_common_parser(prog):
    p = argparse.ArgumentParser(prog)
    p.add_argument(
        "-v", "-V", "--version", action="version", version="%(prog)s " + version
    )
    p.add_argument(
        "-d", "--delimiter", default="\t", help="string delimiter to use. default: TAB"
    )
    p.add_argument(
        "files", default=["-"], nargs="*", help="input files; defaults to - (stdin)"
    )
    return p
