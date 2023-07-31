from .users import User

class Member(User):
    def __init__(self, username, email):
        super().__init__(username, email)

    @staticmethod
    def members():
        return ["username1", "username2", "team"]

    def pay_bill(self):
        pass

    def code(self):
        return "Coding ..."
