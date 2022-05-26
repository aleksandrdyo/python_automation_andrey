import pytest
from jira_client import JiraAuth
from config import PROJECT_NM

@pytest.fixture(scope="function")
def jira_test():
    JiraAuth.get_jira_tasks(PROJECT_NM)


