import pytest
from jira_client import AuthJira
from config import JIRA_EP, EMAIL, TOKEN

#фикстура для авторизации в jira, возвращает класс из jira_client
@pytest.fixture()
def jira_auth():
    return AuthJira(JIRA_EP, EMAIL, TOKEN)




