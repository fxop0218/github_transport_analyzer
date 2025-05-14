import pytest
from unittest.mock import patch, MagicMock
from app.github_client import GitHubClient

@pytest.fixture
def mock_response():
    """
    Create a mock response object for simulating GitHub API responses.
    """
    mock = MagicMock()
    mock.json.return_value = {"items": [
        {"full_name": "repo1", "stargazers_count": 123},
        {"full_name": "repo2", "stargazers_count": 456}
    ]}
    mock.status_code = 200
    return mock

@patch("app.github_client.requests.get")
def test_search_repositories_with_term_strategy(mock_get, mock_response):
    """
    Test that GitHubClient returns repositories when using the term strategy.
    """
    mock_get.return_value = mock_response
    client = GitHubClient(mode="term")
    results = client.search_repositories(term="transport", language="python")

    assert isinstance(results, dict)
    assert "items" in results
    assert results["items"][0]["full_name"] == "repo1"

@patch("app.github_client.requests.get")
def test_search_repositories_with_org_strategy(mock_get, mock_response):
    """
    Test that GitHubClient works with the organization strategy.
    """
    mock_get.return_value = mock_response
    client = GitHubClient(mode="org")
    results = client.search_repositories(term="openai")

    assert isinstance(results, dict)
    assert len(results["items"]) == 2
    assert results["items"][1]["full_name"] == "repo2"

@patch("app.github_client.requests.get")
def test_get_repo_stats(mock_get):
    """
    Test retrieval of repository statistics (commits, contributors, open issues).
    """
    mock_get.return_value = MagicMock(status_code=200)
    mock_get.return_value.json.side_effect = [
        [{"sha": "123abc"}],  # commits
        [{"login": "user1"}], # contributors
        {"open_issues_count": 3}  # repo info
    ]

    client = GitHubClient()
    stats = client.get_repo_stats("octocat/Hello-World")

    assert "commits" in stats
    assert "contributors" in stats
    assert stats["open_issues"] == 3
