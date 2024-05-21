from src.applications.ui.pages.login_page import LoginPage
from src.applications.ui.pages.signup_page import SignUpPage

class GitHubUI(BaseApp):

    def __init__(self) -> None:
        self.login_page = LoginPage()
        self.signup_page = SignUpPage()
    
    def try_login(username: str, password: str):
        return self.login_page.try_login(username, password)
    
    def logout(self):
        pass
    def create_user(sefl):
        pass