from github.client import GithubClient
from repositories.parser import RepoParser


if __name__ == "__main__":
    username = "thiagoneye"
    response = GithubClient.get_repos_by_user(username)

    if response["status_code"] == 200:
        RepoParser.parse(response["body"])
    else:
        print(response["body"])
