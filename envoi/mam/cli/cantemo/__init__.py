from envoi.cli import CliCommand
from .deploy import DeployToAwsCommand


class CantemoCommand(CliCommand):
    DESCRIPTION = "Cantemo Related Commands"
    SUBCOMMANDS = {
        'deploy-to-aws': DeployToAwsCommand,
    }
