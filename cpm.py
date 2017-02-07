#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
                    .,
                   ,Wt t
                  i#D. ED.                ..       :
                 f#f   E#K:              ,W,     .Et
               .D#i    E##W;            t##,    ,W#t
              :KW,     E#E##t          L###,   j###t
              t#f      E#ti##f       .E#j##,  G#fE#t
               ;#G     E#t ;##D.    ;WW; ##,:K#i E#t
                :KE.   E#ELLE##K:  j#E.  ##f#W,  E#t
                 .DW:  E#L;;;;;;,.D#L    ###K:   E#t
                   L#, E#t      :K#t     ##D.    E#t
                    jt E#t      ...      #G      ..
                                         j

Container Package Manager - Simple container distribution abstraction.

"""

__version__ = "1.0.0"
__author__ = "Daniel Middleton"
__maintainer__ = "Daniel Middleton"
__email__ = "d@monokal.io"
__repo__ = "https://github.com/monokal/cpm"
__status__ = "Production"
__license__ = "Unlicense"

import argparse
import logging

logger = logging.getLogger('cpm')


class Cpm(object):
    def __init__(self):
        pass


def main():
    """

    :return:
    """

    # A list of supported container runtimes.
    supported_runtimes = [
        "docker",
        "lxd"
    ]

    # Configure logging.
    logging.basicConfig(level=logging.DEBUG)

    # Configure argument parsing.
    parser = argparse.ArgumentParser(
        prog="cpm",
        description="Container Package Manager - Simple container distribution "
                    "abstraction."
    )

    # Top-level arguments.
    parser.add_argument(
        "-d",
        "--debug",
        required=False,
        action="store_true",
        help="output in debug verbosity"
    )

    # Subparser arguments.
    subparsers = parser.add_subparsers()

    # "Create" parser.
    parser_create = subparsers.add_parser(
        "create",
        help="create a new container package"
    )

    group_create = parser_create.add_argument_group('required arguments')

    supported_runtimes_str = "%s" % ", ".join(map(str, supported_runtimes))
    group_create.add_argument(
        "-r",
        "--runtime",
        required=True,
        choices=supported_runtimes,
        type=str,
        nargs=1,
        metavar='RUNTIME_NAME',
        help="where to publish the report (choose from: %s)" %
             supported_runtimes_str
    )

    parser_create.set_defaults(func=Create)

    args = parser.parse_args()

    client = Cpm(args)
    return client


if __name__ == "__main__":
    main()
