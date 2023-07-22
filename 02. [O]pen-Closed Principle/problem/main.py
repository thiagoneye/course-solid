from github.client import GithubClient
from repositories.parser import RepoParser
from repositories.report_generator import ReportGenerator


if __name__ == "__main__":
    username = "thiagoneye"
    response = GithubClient.get_repos_by_user(username)

    if response["status_code"] == 200:
        repos = RepoParser.parse(response["body"])
        markdown_report = ReportGenerator.build("Markdown", repos)
        html_report = ReportGenerator.build("HTML", repos)

        print(markdown_report)
        print(html_report)

    else:
        print(response["body"])
