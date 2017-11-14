""" Parses command-line arguments """

import argparse
import logging


def parse_arguments(args):
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        "-d",
        "--debug",
        help="Display debugging output",
        action="store_const",
        dest="logging_level",
        const=logging.DEBUG,
        default=logging.ERROR
    )

    parser.add_argument(
        "-v", "--verbose",
        help="Display more verbose output",
        action="store_const",
        dest="logging_level",
        const=logging.INFO
    )

    arguments = parser.parse_args(args)

    logging.basicConfig(
        format="%(levelname)s:%(pathname)s: %(message)s",
        level=arguments.logging_level
    )

    logging.info("Arguments parsing completed")

    return arguments
