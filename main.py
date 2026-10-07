class User:
    def __init__(self, username, role, password):
        self.failed_attempts = 0
        self.username = username
        self.role = role
        self.password = password

    def change_password(self, old_password, new_password):
        # Locked accounts cannot change their password
        if self.failed_attempts >= 3:
            return "Account Locked"

        # Verify the current password
        elif self.password != old_password:
            return "Invalid Current Password"

        # Change the password
        else:
            self.password = new_password
            return "Password Changed"

    def login(self, password):
        # Prevent login if the account is locked
        if self.failed_attempts >= 3:
            return "Account Locked"

        # Successful login
        elif self.password == password:
            self.failed_attempts = 0
            return "Login Successful"

        # Failed login
        else:
            self.failed_login()
            return "Invalid Password"

    def failed_login(self):
        # Increase failed login counter
        self.failed_attempts += 1

    def is_locked(self):
        # Check whether the account is locked
        return self.failed_attempts >= 3

    def show_info(self):
        # Display basic user information
        print("Username:", self.username)
        print("Role:", self.role)
        print("Failed Attempts:", self.failed_attempts)


class LoginSystem:
    def __init__(self):
        # Store users using username as the dictionary key
        self.users = {}

    def register_user(self, username, role, password):
        # Prevent duplicate usernames
        if username in self.users:
            return "Username Already Exists"

        # Create and store a new User object
        self.users[username] = User(username, role, password)

        return "User Registered"

    def get_user(self, username):
        # Return the User object if the username exists
        if username in self.users:
            return self.users[username]

        # Return None when the user does not exist
        return None

    def login(self, username, password):
        # Find the user
        user = self.get_user(username)

        # User does not exist
        if user is None:
            return "User Not Found"

        # Attempt login
        return user.login(password)

    def delete_user(self, username):
        # Check whether the user exists
        if username not in self.users:
            return "User Not Found"

        # Delete the user
        del self.users[username]

        return "User Deleted"

    def change_user_role(self, admin_username, target_username, new_role):
        # Find the administrator
        admin = self.get_user(admin_username)

        # Administrator account does not exist
        if admin is None:
            return "Admin User Not Found"

        # Only administrators can change roles
        if admin.role != "administrator":
            return "Access Denied"

        # Find the target user
        target = self.get_user(target_username)

        # Target user does not exist
        if target is None:
            return "Target User Not Found"

        # Only allow valid roles
        if new_role != "administrator" and new_role != "user":
            return "Invalid Role"

        # Change the target user's role
        target.role = new_role

        return "Role Changed"