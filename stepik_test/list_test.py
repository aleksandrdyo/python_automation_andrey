from jira import JIRA
from requests_toolbelt import user_agent
from config import JIRA_EP, EMAIL, TOKEN, PROJECT_NM

class AuthJira:
    def __init__(self, end_point, email, token):
        self.jira = JIRA(end_point, basic_auth=(email, token))

    # def get_tasks(self, project_name):
    #     issues = self.jira.search_issues(project_name)
    #     keys_list = []
    #     for key in issues:
    #         keys_list.append(key)
    #     return keys_list

    def get_tasks(self, project_name):
        issues = self.jira.search_issues(project_name)
        keys_list = []
        for key in issues:
            keys_list.append(key)
        return keys_list

        authenticated_jira = JIRA(options={'server': self.jira_server},
                                  basic_auth=(self.jira_username, self.jira_password))
        issue = authenticated_jira.issue(self.id)

        for field_name in issue.raw['fields']:
            print
            "Field:", field_name, "Value:", issue.raw['fields'][field_name]

x = AuthJira(JIRA_EP, EMAIL, TOKEN)
print(type(x.get_tasks(PROJECT_NM)[0]))
print(x.get_tasks(PROJECT_NM))
