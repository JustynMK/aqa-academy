import pytest
from src.applications.ui.github_ui import GitHubUI
from selenium import webdriver

@pytest.fixture
def git_hub_ui_app():
    #1. Prestep. Navigate to GithubAPP
    GitHubUI.open.login

