#!/usr/bin/env python3

import os
import sys
import argparse

from cutpaste.version import version


def main():
    p = argparse.ArgumentParser('pypaste')
    p.add_argument('-V', '--version', action='version', version='%(prog)s ' + version)
    args = p.parse_args()


if __name__ == '__main__':
    main()
