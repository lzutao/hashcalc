#!/usr/bin/env python
from __future__ import print_function
from builtins import bytes, str

import argparse
import logging
import sys

# local import
import hashcalc

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s: %(message)s',
)
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(
        prog="hashcalc",
        usage='%(prog)s [OPTION]... [FILE]',
        description='Print MD5 (128-bit) or SHA1 (160-bit) checksum.',
        epilog="[+] Written by 15520599"
        )
    parser.add_argument(
        'FILE',
        nargs='?',
        type=argparse.FileType('rb'),
        default=sys.stdin,
        help="With no FILE, or when FILE is -, read from standard input."
        )
    parser.add_argument(
        '-m', '--mode',
        help='Choose hash algorithm: MD5 or SHA1 (Default MD5).',
        choices=['md5', 'sha1']
        )
    parser.add_argument(
        '-x', '--hex',
        action="store_true",
        help='Read input encoded in hex mode.',
        )

    args = parser.parse_args()
    logger.debug(args.FILE)

    hash_func = None
    file_name = None
    content = None

    if not args.mode:
        hash_func = 'md5'
    else:
        hash_func = args.mode

    # if input is stdin or input encoded in hex
    if (args.FILE is sys.stdin) or args.hex:
        # be careful with newline character
        content = args.FILE.read()
        if args.hex:
            content = bytes.fromhex(content)
        hash_func += 'sumhex'
    else:
        # read from opened file
        hash_func += 'filehex'
        file_name = args.FILE.name

    hash_func = getattr(hashcalc, hash_func)

    logger.debug("hash func: %r"%hash_func)

    checksum = None
    if file_name:
        checksum = hash_func(file_name)
    else:
        checksum = hash_func(content)

    print("%s"%checksum)


if __name__ == '__main__':
    main()

