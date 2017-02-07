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

import argparse
import logging
import sys

from helpers import Helpers

__version__ = "1.0.0"
__author__ = "Daniel Middleton"
__maintainer__ = "Daniel Middleton"
__email__ = "d@monokal.io"
__repo__ = "https://github.com/monokal/cpm"
__status__ = "Production"
__license__ = "Unlicense"

# Configure global logging.
try:
    logger = logging.getLogger('cpm')
    out = logging.StreamHandler(sys.stdout)
    out.setLevel(logging.DEBUG)
    formatter = logging.Formatter("[cpm] %(message)s")
    out.setFormatter(formatter)
    logger.addHandler(out)
    logging.basicConfig(level=logging.DEBUG)
except:
    print("Failed to initialise logging.")


class Cpm(object):
    def __init__(self, args):
        """

        :param args:
        """

        self.args = args
        self.helpers = Helpers()

    def __call__(self):
        """

        :return:
        """

        print(self.helpers.get_ascii_logo())

        # Create an instance of and call the given class.
        target_class = self.args.func(self.args)
        return target_class()


class Build(object):
    def __init__(self, args):
        pass

    def __call__(self):
        pass


class Push(object):
    def __init__(self, args):
        pass

    def __call__(self):
        pass


class Package(object):
    def __init__(self, args):
        pass

    def __call__(self):
        pass


def main():
    """

    :return:
    """

    # A list of supported container runtimes, used by argparse below.
    supported_runtimes = [
        "docker"
    ]

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

    #
    # Start of "Build" subparser.
    parser_build = subparsers.add_parser(
        "create",
        help="build a new container"
    )

    group_build = parser_build.add_argument_group('required arguments')

    group_build.add_argument(
        "-r",
        "--runtime",
        required=True,
        choices=supported_runtimes,
        type=str,
        nargs=1,
        metavar='RUNTIME_NAME',
        help="the container runtime you're using (choose from: %s)" %
             ", ".join(map(str, supported_runtimes))
    )

    parser_build.set_defaults(func=Build)
    # End of "Build" subparser.
    #

    #
    # Start of "Package" subparser.
    parser_package = subparsers.add_parser(
        "package",
        help="create a new container abstraction"
    )

    group_package = parser_package.add_argument_group('required arguments')

    group_package.add_argument(
        "-r",
        "--runtime",
        required=True,
        choices=supported_runtimes,
        type=str,
        nargs=1,
        metavar='RUNTIME_NAME',
        help="the container runtime you're using (choose from: %s)" %
             ", ".join(map(str, supported_runtimes))
    )

    parser_package.set_defaults(func=Package)
    # End of "Package" subparser.
    #

    try:
        args = parser.parse_args()
    except Exception:
        logger.exception("Failed to parse arguments.")

    # Turn on debug output if -d/--debug was passed.
    if args.debug:
        logger.setLevel(logging.DEBUG)
        logger.debug('Debug mode on.')

    client = Cpm(args)
    return client()


if __name__ == "__main__":
    main()
