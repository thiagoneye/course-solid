from .users import User

class Manager(User):
    def __init__(self, username, email):
        super().__init__(username, email)

    @staticmethod
    def members():
        raise Exception("Member is not authorized to do this!")

    def pay_bill(self):
        return "Paying bills ..."

    def code(self):
        pass
