def test_negative_login(git_hub_ui_app):
    """Summary: Test navigate login attemp
    Steps:
    1. Navigate to login page
    2. Enter wrong credentials
    3. Click the login/sig in button

    Expected result
    Error saying XYZ appeared
    """
    #1. Navigate to login page
    git_hub_ui_app.login_page.navigate_to()

    #2. Enter wrong creds
    git_hub_ui_app.try_login(username='jmkl', password='jmkl')

    # Expected result
    assert git_hub_ui_app.login_page.check_wrong_creds_message()
