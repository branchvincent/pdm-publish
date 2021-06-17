from pdm import Core

from .command import PublishCommand
from .config import CONFIG


def main(core: Core) -> None:
    core.register_command(PublishCommand)
    for k, v in CONFIG.items():
        core.add_config(k, v)
