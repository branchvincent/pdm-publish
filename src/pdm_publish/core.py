from __future__ import annotations

import subprocess
import sys
from dataclasses import dataclass
from typing import Any

from pdm import Project, termui


def twine(*cmd: str, **kwargs: Any) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "twine", *cmd], capture_output=True, text=True, **kwargs
    )


@dataclass
class Publisher:
    project: Project

    @property
    def ui(self) -> termui.UI:
        return self.project.core.ui

    @property
    def files(self) -> list[str]:
        dist = self.project.pyproject_file.parent / "dist"
        return [str(f) for g in {"*.whl", "*.tar.gz"} for f in dist.glob(g)]

    def publish(self, repo: str, username: str, password: str, dry_run: bool) -> None:
        repo_flag_suffix = "" if repo.lower() in {"pypi", "testpypi"} else "-url"
        with self.ui.open_spinner(f"Uploading to {repo}") as spin:
            resp = twine(
                "upload",
                "--non-interactive",
                f"--repository{repo_flag_suffix}",
                repo,
                "--username",
                username,
                *self.files,
                env={"TWINE_PASSWORD": password},
            )
            if resp.returncode:
                spin.fail("Publish failed")
                print(termui.red(resp.stderr))
                resp.check_returncode()
            else:
                spin.succeed("Publish successful")

        self.ui.echo(
            f"Uploaded {termui.cyan(self.project.meta.name)}"
            f" ({termui.bold(self.project.meta.version)})"
        )
