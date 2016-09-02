#!/usr/bin/env python
# coding: utf-8
"""
test_penne_shell
----------------------------------

Tests for `penne_shell` module.
"""
import os
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

    def test_command_line_interface_ok(self):

        runner = CliRunner()
        result = runner.invoke(cli.main, ['/testes/'])
        assert result.exit_code == -1

    def test_command_line_interface_help(self):

        runner = CliRunner()
        result = runner.invoke(cli.main, ['--help'])
        assert result.exit_code == 0

    def test_command_line_interface_without_argument(self):

        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 2
        assert 'Error: Missing argument "monitored_path".' in result.output


class TestPenne_shellInspector(unittest.TestCase):

    def setUp(self):
        self._dir_path = os.path.dirname(os.path.realpath(__file__))

    def tearDown(self):
        pass

    def test_is_valid_zip_false(self):

        inspector = penne_shell.Inspector(self._dir_path+'/fixtures/invalid.zip')

        assert inspector._is_valid_zip() == False

    def test_is_valid_zip_true(self):

        inspector = penne_shell.Inspector(self._dir_path+'/fixtures/valid.zip')

        assert inspector._is_valid_zip() == True


if __name__ == '__main__':
    sys.exit(unittest.main())
