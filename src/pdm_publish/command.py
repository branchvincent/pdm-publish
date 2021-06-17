from argparse import ArgumentParser, Namespace
from typing import Any

import click
from pdm import Project, termui
from pdm.cli.actions import do_build
from pdm.cli.commands.base import BaseCommand
from pdm.exceptions import PdmUsageError

from .core import Publisher


class PublishCommand(BaseCommand):  # type: ignore
    """Upload artifacts to a remote repository"""

    name = "publish"

    def add_arguments(self, parser: ArgumentParser) -> None:
        parser.add_argument(
            "-r",
            "--repository",
            help="The repository name or url to publish the package to"
            " [env var: PDM_PUBLISH_REPO]",
        )
        parser.add_argument(
            "-u",
            "--username",
            help="The username to access the repository"
            " [env var: PDM_PUBLISH_USERNAME]",
        )
        parser.add_argument(
            "-P",
            "--password",
            help="The password to access the repository"
            " [env var: PDM_PUBLISH_PASSWORD]",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Perform all actions except upload the package",
        )
        parser.add_argument(
            "--no-build",
            action="store_false",
            dest="build",
            help="Don't build the package before publishing",
        )

    def coalesce(
        self, project: Project, options: Namespace, key: str, **kwargs: Any
    ) -> str:
        value = getattr(options, key) or project.config.get(f"publish.{key}")
        if not value:
            value = click.prompt(key.capitalize(), **kwargs)
        return str(value)

    def handle(self, project: Project, options: Namespace) -> None:
        # Validation
        username = self.coalesce(project, options, "username")
        password = self.coalesce(project, options, "password", hide_input=True)

        # Build
        if options.build:
            do_build(project)

        # Check for files
        publisher = Publisher(project)
        if not publisher.files:
            raise PdmUsageError(
                f"No files to publish! Retry without {termui.bold('--no-build')}."
            )

        # Publish
        publisher.publish(
            repo=options.repository or project.config["publish.repo"],
            username=username,
            password=password,
            dry_run=options.dry_run,
        )
