import requests


class ListRepositories():
    API_BASE_URL = "https://api.github.com"

    def __init__(self, user):
        self._user = user

    def get_repos_by_user(self):
        response = requests.get(
            f"{self.API_BASE_URL}/users/{self._user}/repos")

        if response.status_code == 200:
            return {
                "status_code": 200,
                "body": response.json()
            }
        return {
            "status_code": response.status_code,
            "body": "Error while getting repositories"
        }

    def parse_response(self):
        response = self.get_repos_by_user()
        body = response["body"]

        if response["status_code"] == 200:
            for idx in range(len(body)):
                print(f"{body[idx]['id']} - {body[idx]['name']} - {body[idx]['stargazers_count']}")


if __name__ == "__main__":
    respo = ListRepositories("thiagoneye")
    respo.parse_response()
