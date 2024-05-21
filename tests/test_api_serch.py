def test_check_serch_repo():
    """
    1. Send API request to find the repo named BLA
    2. Analyse the responce

    `expected result:
    number of found repos == SOMENUMBER
    """

repos_list, reaponse = git_hub_api_client.serch_repos("BLA")

#2. Analyse the responce
response.reise