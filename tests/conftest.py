from pathlib import Path

import pytest
from pdm import Core, Project

from pdm_publish.core import Publisher


@pytest.fixture
def core() -> Core:
    return Core()


@pytest.fixture
def project(core: Core, tmp_path: Path) -> Project:
    return Project(core, root_path=tmp_path)


@pytest.fixture
def publisher(project: Project) -> Publisher:
    return Publisher(project)
