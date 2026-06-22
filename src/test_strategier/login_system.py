class LoginSystem:
    def __init__(self):
        self.users = {}
        self.failed_attempts = {}
        self.locked_users = set()

    def create_user(self, username, password):
        self.users[username] = password
        self.failed_attempts[username] = 0

    def login(self, username, password):
        if username in self.locked_users:
            return "låst"

        if self.users.get(username) != password:
            self.failed_attempts[username] += 1
            if self.failed_attempts[username] >= 3:
                self.locked_users.add(username)
            return "forkert"

        self.failed_attempts[username] = 0
        return "ok"
