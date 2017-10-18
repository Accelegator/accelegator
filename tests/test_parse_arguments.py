# python libraries
import logging

# internal dependencies
import parse_arguments

def test_parse_arguments_no_arguments():
    args = []
    parsed_arguments = parse_arguments.parse_arguments(args)

    assert parsed_arguments.logging_level == logging.ERROR

def test_parse_arguments_debug_logging_level():
    args = ['--debug']
    parsed_arguments = parse_arguments.parse_arguments(args)

    assert parsed_arguments.logging_level == logging.DEBUG

def test_parse_arguments_d_logging_level():
    args = ['--d']
    parsed_arguments = parse_arguments.parse_arguments(args)

    assert parsed_arguments.logging_level == logging.DEBUG

def test_parse_arguments_verbose_logging_level():
    args = ['--verbose']
    parsed_arguments = parse_arguments.parse_arguments(args)

    assert parsed_arguments.logging_level == logging.INFO

def test_parse_arguments_v_logging_level():
    args = ['--v']
    parsed_arguments = parse_arguments.parse_arguments(args)

    assert parsed_arguments.logging_level == logging.INFO
