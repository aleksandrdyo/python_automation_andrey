import pytest
from jira_client import JiraClient
from config import JIRA_ENDPOINT, EMAIL, TOKEN


#фикстура для авторизации в jira, возвращает класс из jira_client
@pytest.fixture()
def jira_client():
    return JiraClient(JIRA_ENDPOINT, EMAIL, TOKEN)




