from jira import JIRA
from requests_toolbelt import user_agent
from config import JIRA_EP, EMAIL, TOKEN, PROJECT_NM

jira = JIRA(JIRA_EP,
                basic_auth=(EMAIL, TOKEN),
                options={"headers": {"User-Agent": user_agent("my_package", "0.0.1")}}
                )

class JiraAuth():
    def get_jira_tasks(self):
        issues = jira.search_issues(self)
        for x in range(len(issues)):
            print(issues[x])



