class LoginPage:
    # URL of the page
    URL = "https://github.com/login"
    # Elements of the page
    LOGIN_FLD = '//*[@id="login_field]'
    PASSWORD_FLD = '//*[@id="password]'
    SIGNIN_BUT = '//*[@id="login"]/div[4]/from/div/input[13]'
    
    def __init__(self, app) -> None:
        self.app = app

    # users metods
    def try_login(self, username: str, password: str):
        pass
    
    def navigate_to(self):
        self.app.navigate_to(self.URL)

    # check functions
    def check_wrong_creds_message(self):
        # find error message
        # check if message is equal to "something" text
        return False

    def check_documentation_link(self):
        pass