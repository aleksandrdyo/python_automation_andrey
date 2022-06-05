from jira import JIRA
from requests_toolbelt import user_agent
from config import JIRA_EP, EMAIL, TOKEN, PROJECT_NM

# класс с методами для работы с jira
class AuthJira:
    # конструктор для авторизации в jira
    def __init__(self, end_point, email, token):
        self.jira = JIRA(end_point, basic_auth=(email, token))
    # метод для получения тасков из jira
    def get_tasks(self, project_name):
        issues = self.jira.search_issues(project_name)
        keys_list = []
        for issue in issues:
            keys_list.append(issue.key)
        return keys_list
