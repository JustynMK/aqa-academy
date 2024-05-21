def test_positive_login():
    """Summary: Test navigate login attemp
    Steps:
    1. Navigate to login page
    2. Enter wrong credentials
    3. Click the login/sig in button

    Expected result
    Error saying XDXD appeared
    """

    #1. Navigate to login page
    chromeBrowser.open()
    chromeBrowser.github_login_page.navigate_to()

    #2. Enter wrong creds
    user_name_fld = github_login_page.find_username_fld()
    user_name_fld.enter_text("jmkl")

    password_fld = github_login_page.find_password_fld()
    password_fld.enter_text("jmkl")

    #3. Click login/signin button
    signin_btn = github_login_page.find_signin_btn()
    signin_btn.click()

    # Expected result
    error_message = github_login_page.find_error_message()

    assert error_message.text() == "AN ERROR OCURED"

    # CleanUP
    chromeBrowser.close()

def test_positive_updated(GitHubUI):
    """Summary: Test navigate login attemp
    Steps:
    1. Navigate to login page
    2. Enter wrong credentials
    3. Click the login/sig in button

    Expected result
    Error saying something appeared
    """

    #1. Navigate to login page
    GitHubUI.open() # webdriver method -BAD
    GitHubUI.github_login_page.navigate_to()

    #2. Enter wrong creds
    GitHubUI.try_login(username='jmkl', password='jmkl')

    # Expected result
    assert GitHubUI.login_page.check_wrong_creds_message()

    # CleanUP
    GitHubUI.close() # webdrivemethod BAD