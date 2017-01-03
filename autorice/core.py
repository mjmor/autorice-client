"""
Main rice module
"""
import argparse
import logging

QUIET_LOGGING_LEVEL = logging.ERROR
DEFAULT_LOGGING_LEVEL = logging.WARNING
VERBOSE_LOGGING_LEVEL = logging.INFO


class Autorice:
    def __init__(self):
        self._arg_parser = self.get_arg_parser()
        self.args = None
        self.logger = logging.getLogger(__name__)

    def run(self):
        self.args = self._arg_parser.parse_args()
        self.args.action()

    def install(self):
        raise NotImplementedError

    def remove(self):
        raise NotImplementedError

    def get_arg_parser(self):
        """
        Create an argument parser instance
        :return: argparse.ArgumentParser
        """
        parser = argparse.ArgumentParser(description="""
            autoRice is an automatic configuration file manager allowing you to
            check out sweet rices with a single command.
            """)
        parser.set_defaults(action=parser.print_help)
        sp = parser.add_subparsers(title='subcommands')

        # region parser_install
        parser_install = sp.add_parser('install', help='Install a rice.',
                                       aliases=['rice'])
        parser_install.add_argument('rice', type=str,
                                    help="Name of the rice to install.",
                                    nargs='+')
        parser_install.set_defaults(action=self.install)
        # endregion

        # region parser_remove
        parser_remove = sp.add_parser('remove', help='Remove a rice.')
        parser_remove.add_argument('rice', type=str,
                                   help="Name of the rice to remove.",
                                   nargs='+')
        parser_remove.set_defaults(action=self.remove)
        # endregion

        subparsers = [parser_install, parser_remove]

        # region generic_options
        for subparser in subparsers:
            subparser.add_argument("-s", "--dry-run",
                                   help="Don't modify any files.",
                                   action="store_true",
                                   dest='dry_run')

            verbosity = subparser.add_mutually_exclusive_group()
            verbosity.add_argument("-v", "--verbose",
                                   help="Display debugging information",
                                   action="store_const",
                                   dest='verbosity',
                                   const=VERBOSE_LOGGING_LEVEL)
            verbosity.add_argument("-q", "--quiet",
                                   help="Don't print anything unless an error occurs",
                                   action="store_const",
                                   dest='verbosity',
                                   const=QUIET_LOGGING_LEVEL)

            subparser.set_defaults(verbosity=DEFAULT_LOGGING_LEVEL)
            subparser.set_defaults(dry_run=False)
        # endregion
        return parser
