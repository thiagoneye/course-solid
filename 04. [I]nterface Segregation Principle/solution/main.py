from github.client import GithubClient
from repositories.parser import RepoParser
from repositories.report_generator import ReportGenerator
from repositories.report.html_generator import HTMLGenerator
from repositories.report.markdown_generator import MarkdownGenerator
from models.member import Member
from models.manager import Manager


if __name__ == "__main__":
    username = "thiagoneye"
    response = GithubClient.get_repos_by_user(username)

    if response["status_code"] == 200:
        repos = RepoParser.parse(response["body"])
        markdown_report = ReportGenerator.build(MarkdownGenerator, repos)
        html_report = ReportGenerator.build(HTMLGenerator, repos)

        print(markdown_report)
        print(html_report)

    else:
        print(response["body"])

    member = Member("thiago", "thiago@gmail.com")
    manager = Manager("ney", "ney@gmail.com")

    print(member.members())

    print(member.work())
    print(manager.work())
