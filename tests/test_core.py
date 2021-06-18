import subprocess
from subprocess import CompletedProcess
from unittest.mock import MagicMock

import pytest
from pytest_mock import MockFixture

from pdm_publish.core import Publisher


@pytest.fixture
def twine(mocker: MockFixture) -> MagicMock:
    return mocker.patch(
        "pdm_publish.core.twine",
        return_value=CompletedProcess(args="notused", returncode=0),
    )


def test_publisher_calls_twine(publisher: Publisher, twine: MagicMock) -> None:
    publisher.publish(repo="pypi", username="user", password="pass")
    twine.assert_called_once_with(
        "upload",
        "--non-interactive",
        "--repository",
        "pypi",
        "--username",
        "user",
        env={"TWINE_PASSWORD": "pass"},
    )


@pytest.mark.parametrize("repo", ["pypi", "testpypi"])
def test_publisher_calls_twine_with_repo(
    publisher: Publisher, twine: MagicMock, repo: str
) -> None:
    publisher.publish(repo=repo, username="user", password="pass")
    assert "--repository" in twine.call_args[0]


@pytest.mark.parametrize(
    "repo_url", ["https://upload.pypi.org/legacy/", "https://example.pypi.org/"]
)
def test_publisher_calls_twine_with_repo_url(
    publisher: Publisher, twine: MagicMock, repo_url: str
) -> None:
    publisher.publish(repo=repo_url, username="user", password="pass")
    assert "--repository-url" in twine.call_args[0]


def test_publisher_displays_stderr_on_twine_failure(
    publisher: Publisher, mocker: MockFixture, capsys: pytest.CaptureFixture[str]
) -> None:
    mocker.patch(
        "pdm_publish.core.twine",
        return_value=CompletedProcess(
            args="notused", returncode=1, stdout="out", stderr="err"
        ),
    )
    with pytest.raises(subprocess.CalledProcessError):
        publisher.publish(repo="repo", username="user", password="pass")
    _, err = capsys.readouterr()
    assert err == "err\n"
