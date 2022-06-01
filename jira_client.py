from jira import JIRA
from requests_toolbelt import user_agent
from config import JIRA_EP, EMAIL, TOKEN, PROJECT_NM

class AuthJira:
    def __init__(self, a, b, c):
        self.endp = a
        self.email = b
        self.token = c
        self.jira = JIRA(a, basic_auth=(b, c))

    def get_tasks(self, w):
        issues = self.jira.search_issues(w)
        for y in range(len(issues)):
            print(issues[y])


x = AuthJira(JIRA_EP, EMAIL, TOKEN)

print(x.get_tasks(PROJECT_NM))