from pdm.project.config import ConfigItem

CONFIG = {
    "publish.repo": ConfigItem(
        description="PyPI repo name (pypi/testpypi) or url",
        default="pypi",
        env_var="PDM_PUBLISH_REPO",
    ),
    "publish.username": ConfigItem(
        description="PyPI username", default="__token__", env_var="PDM_PUBLISH_USERNAME"
    ),
    "publish.password": ConfigItem(
        description="PyPI password", env_var="PDM_PUBLISH_PASSWORD"
    ),
}
