import pytest
from jira_client import AuthJira
from config import JIRA_EP, EMAIL, TOKEN, PROJECT_NM


@pytest.fixture(scope="function")
def jira():
    x = AuthJira(JIRA_EP, EMAIL, TOKEN)



