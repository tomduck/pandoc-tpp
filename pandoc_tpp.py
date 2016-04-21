#! /usr/bin/env python

"""pandoc-tpp: A pandoc template preprocessor."""

# Copyright 2016 Thomas J. Duck.
# All rights reserved.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import re
import sys
import os.path
import argparse
import io
import tempfile
import uuid


# Detect python 3
PY3 = sys.version_info > (3,)

# Pandoc uses UTF-8 for both input and output; so must we
if PY3:  # Force utf-8 decoding (decoding of input streams is automatic in py3)
    STDIN = io.TextIOWrapper(sys.stdin.buffer, 'utf-8', 'strict')
    STDOUT = io.TextIOWrapper(sys.stdout.buffer, 'utf-8', 'strict')
else:    # No decoding; utf-8-encoded strings in means the same out
    STDIN = sys.stdin
    STDOUT = sys.stdout

# Patterns
INCLUDE = re.compile(r'^\$include\((.*)\)\$$')  # $include(...)$


def preprocess(path):
    """Preprocesses the template at path."""

    # Save the directory name for the template
    dirname = os.path.dirname(path)

    # Read in the template
    with open(path) as f:
        lines = f.readlines()

    # Process the template
    newlines = []
    for line in lines:
        if INCLUDE.search(line.strip()):  # $include(...)$
            name = INCLUDE.search(line.strip()).group(1)
            path = os.path.normpath(os.path.join(dirname, name))
            newlines += preprocess(path)  # Recursive call
        else:
            newlines.append(line)

    return newlines


def main():
    """Main program."""

    # Read the command-line args
    desc = 'Pandoc template preprocessor.'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('path', help='Path to template.')
    parser.add_argument('-t', '--tempfile', action='store_true',
                        help='Writes to a tempfile and prints tempfile name')
    args = parser.parse_args()

    # Preprocess the template
    lines = preprocess(args.path)

    # Write the lines...
    if args.tempfile:
        # ... to a tempfile and print out the file name.  We must create the
        # tempfile in a manner that persists.
        path = os.path.join(tempfile.gettempdir(),
                            str(uuid.uuid4())+os.path.splitext(args.path)[1])
        with open(path, 'w') as f:
            f.writelines(lines)
        STDOUT.write(path)
    else:
        # ... to stdout.
        STDOUT.writelines(lines)
    STDOUT.flush()


if __name__ == '__main__':
    main()
