[![PyPI version](https://badge.fury.io/py/cutpaste.svg)](https://badge.fury.io/py/cutpaste)

## cutpaste

Unix-like `cut` and `paste` commands with **multi-character delimiter support**.

Unlike the standard Unix `cut` which only supports single-character delimiters, `pycut` and `pypaste` can split and join on strings like `::`, `->`, or any delimiter you need.

### Installation

```bash
pip install cutpaste
```

### pycut - Extract fields from lines

Extract specific fields from each line of input, using a delimiter.

```
pycut -d DELIMITER -f FIELDS [FILE...]
```

**Options:**
- `-d, --delimiter` - String delimiter to split on (default: TAB). Supports escape sequences like `\t`, `\n`.
- `-f, --field` - Field(s) to extract (required). 1-based indexing.
- `-v, --version` - Show version and exit.

**Field specification formats:**
- Single field: `-f 2` (extract field 2)
- Multiple fields: `-f 1,3,5` (extract fields 1, 3, and 5)
- Range: `-f 2-4` (extract fields 2, 3, and 4)
- Mixed: `-f 1,3-5,7` (extract fields 1, 3, 4, 5, and 7)

**Examples:**

```bash
# Extract the second field from a space-delimited file
pycut -d ' ' -f 2 data.txt

# Extract first and third columns from CSV
pycut -d ',' -f 1,3 data.csv

# Multi-character delimiter - extract second part of "key::value" lines
pycut -d '::' -f 2 config.txt

# Use with pipes
echo "a->b->c" | pycut -d '->' -f 2
# Output: b

# Extract a range of fields
echo "one,two,three,four,five" | pycut -d ',' -f 2-4
# Output: two,three,four

# Read from stdin explicitly
cat file.txt | pycut -d '\t' -f 1 -
```

### pypaste - Merge files line by line

Merge corresponding lines from multiple files, joining them with a delimiter.

```
pypaste -d DELIMITER [FILE...]
```

**Options:**
- `-d, --delimiter` - String delimiter to join with (default: TAB). Supports escape sequences like `\t`, `\n`.
- `-v, --version` - Show version and exit.

**Examples:**

```bash
# Merge two files with tab delimiter (default)
pypaste names.txt ages.txt

# Merge with comma delimiter
pypaste -d ',' col1.txt col2.txt col3.txt

# Multi-character delimiter
pypaste -d ' | ' left.txt right.txt

# Use stdin as one of the inputs
seq 5 | pypaste -d ',' - letters.txt
```

### Streaming

Both commands process input line-by-line without loading entire files into memory. This means they work efficiently with:
- Large files
- Piped input
- Infinite streams

### License

MIT
