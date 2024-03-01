import sys

from envoi.cli import CliApp
from .cantemo import CantemoCommand

import logging

LOG = logging.getLogger(__name__)


class EnvoiMamCli(CliApp):
    DESCRIPTION = "Envoi MAM Command Line Utility"

    PARAMS = {
        "log_level": {
            "flags": ['--log-level'],
            "type": str,
            "default": "INFO",
            "help": "Set the logging level (options: DEBUG, INFO, WARNING, ERROR, CRITICAL)"
        },
    }

    SUBCOMMANDS = {
        'cantemo': CantemoCommand,
    }


def main():
    cli = EnvoiMamCli(auto_exec=False)
    return cli.run()


if __name__ == "__main__":
    sys.exit(main())
