#!/usr/bin/env python3

import sys
from itertools import zip_longest

from cutpaste import utils


def open_files(paths):
    """Open multiple files and return list of file handles."""
    handles = []
    for path in paths:
        if path == "-":
            handles.append(sys.stdin)
        else:
            handles.append(open(path))
    return handles


def close_files(handles):
    """Close file handles (except stdin)."""
    for f in handles:
        if f is not sys.stdin:
            f.close()


def main():
    """
    Paste - merge lines from multiple files with a delimiter.
    Streams line-by-line for memory efficiency.
    """
    args = utils.parse_args("pypaste")
    delimiter = utils.decode_escapes(args.delimiter)

    # Open all files as iterators
    handles = open_files(args.files)

    try:
        # zip_longest on file iterators - lazy, memory-efficient
        for lines in zip_longest(*handles, fillvalue=""):
            # Strip newlines and join with delimiter
            merged = delimiter.join(line.rstrip("\n\r") for line in lines)
            print(merged)
    finally:
        close_files(handles)


if __name__ == "__main__":
    main()
