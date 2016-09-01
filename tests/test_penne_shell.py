#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test_penne_shell
----------------------------------

Tests for `penne_shell` module.
"""
import sys
import unittest
from contextlib import contextmanager
from click.testing import CliRunner

from penne_shell import penne_shell
from penne_shell import cli


class TestPenne_shell(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass

    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'penne_shell.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output


if __name__ == '__main__':
    sys.exit(unittest.main())
