import unittest
from autorice.core import (Autorice, DEFAULT_LOGGING_LEVEL, QUIET_LOGGING_LEVEL,
                           VERBOSE_LOGGING_LEVEL)

autorice = Autorice()
parser = autorice.get_arg_parser()


class TestParsingArguments(unittest.TestCase):

    def test_defaults(self):
        args = parser.parse_args(['install', 'foo'])
        self.assertEqual(args.verbosity, DEFAULT_LOGGING_LEVEL)
        self.assertEqual(args.dry_run, False)

    def test_install(self):
        args = parser.parse_args(['install', 'foo'])
        self.assertEqual(args.action, autorice.install)
        self.assertEqual(args.rice, ['foo'])
        args = parser.parse_args(['install', 'foo', 'bar'])
        self.assertEqual(args.action, autorice.install)
        self.assertEqual(args.rice, ['foo', 'bar'])

    def test_remove(self):
        args = parser.parse_args(['remove', 'foo'])
        self.assertEqual(args.action, autorice.remove)
        self.assertEqual(args.rice, ['foo'])
        args = parser.parse_args(['remove', 'foo', 'bar'])
        self.assertEqual(args.action, autorice.remove)
        self.assertEqual(args.rice, ['foo', 'bar'])

    def test_non_existing_action(self):
        with self.assertRaises(SystemExit):
            parser.parse_args(['foo'])

    def test_quiet(self):
        args = parser.parse_args(['install', '-q', 'foo'])
        self.assertEqual(args.verbosity, QUIET_LOGGING_LEVEL)
        args = parser.parse_args(['install', '--quiet', 'foo'])
        self.assertEqual(args.verbosity, QUIET_LOGGING_LEVEL)

    def test_verbose(self):
        args = parser.parse_args(['install', '-v', 'foo'])
        self.assertEqual(args.verbosity, VERBOSE_LOGGING_LEVEL)
        args = parser.parse_args(['install', '--verbose', 'foo'])
        self.assertEqual(args.verbosity, VERBOSE_LOGGING_LEVEL)

    def test_quiet_and_verbose_error(self):
        with self.assertRaises(SystemExit):
            parser.parse_args(['install', '-vq', 'foo'])

    def test_no_package_error(self):
        with self.assertRaises(SystemExit):
            parser.parse_args(['install'])
        with self.assertRaises(SystemExit):
            parser.parse_args(['remove'])

    def test_dry_run(self):
        args = parser.parse_args(['install', '-s', 'foo'])
        self.assertEqual(args.dry_run, True)
        args = parser.parse_args(['install', '--dry-run', 'foo'])
        self.assertEqual(args.dry_run, True)


if __name__ == '__main__':
    unittest.main()