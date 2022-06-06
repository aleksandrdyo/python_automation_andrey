from jira import JIRA


# класс с методами для работы с jira
class JiraClient:
    # конструктор для авторизации в jira
    def __init__(self, endpoint, email, token):
        self.jira = JIRA(endpoint, basic_auth=(email, token))
    # метод для получения тасков из jira
    def get_tasks(self, project_name):
        issues = self.jira.search_issues(project_name)
        keys_list = []
        for issue in issues:
            keys_list.append(issue.key)
        return keys_list
