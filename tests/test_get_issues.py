from config import PROJECT_NAME

expected_tasks = ['DYO-9', 'DYO-8', 'DYO-7', 'DYO-6', 'DYO-5', 'DYO-4', 'DYO-2', 'DYO-1']


#передаем в функцию авторизации jira_auth из conftest
def test_get_issues(jira_client):
    jira = jira_client
    actual_tasks = jira.get_tasks(PROJECT_NAME)

    assert expected_tasks == actual_tasks, "test failed!"
