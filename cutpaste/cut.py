#!/usr/bin/env python3

from cutpaste import utils


def cut_line(line, delimiter, field_indices):
    """Extract specified fields from a line and return them joined by delimiter."""
    parts = line.rstrip("\n\r").split(delimiter)
    selected = []
    for idx in field_indices:
        if 0 <= idx < len(parts):
            selected.append(parts[idx])
        else:
            selected.append("")
    return delimiter.join(selected)


def main():
    """
    Cut - extract fields from lines using a delimiter.
    Streams line-by-line for memory efficiency.
    """
    args = utils.parse_args("pycut")
    delimiter = utils.decode_escapes(args.delimiter)
    field_indices = utils.parse_fields(args.field)

    # Process each file (or stdin) line by line
    for file_path in args.files:
        with utils.open_file(file_path) as f:
            for line in f:
                print(cut_line(line, delimiter, field_indices))


if __name__ == "__main__":
    main()
