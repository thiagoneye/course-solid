from models.repo import Repo


class RepoParser():

    @classmethod
    def parse(cls, response):
        for idx in range(len(response)):
            repo = response[idx]
            repo = Repo(repo["id"], repo["name"], repo["stargazers_count"])
            print(repo)
