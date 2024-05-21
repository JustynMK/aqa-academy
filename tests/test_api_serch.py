def test_check_serch_repo(git_hub_api_client):
    """
    1. Send API request to find the repo named XYZ
    2. Analyse the responce

    Expected result:
    number of found repos == SOMENUMBER
    """

#1. Send API request to find the repo named XYZ
repos_number, response = git_hub_api_client.serch_repos("XYZ")

#2. Analyse the responce
response.raise_for_status()

assert repos_number == 10