import requests
from app.cache import cache_get, cache_set
from app.strategies.strategy_factory import get_strategy

class GitHubClient:
    """
    GitHubClient uses a pluggable strategy to construct GitHub API search queries
    and fetch repository information including statistics, using optional authentication.
    """

    BASE_URL = "https://api.github.com"

    def __init__(self, token: str | None = None, mode: str = "term"):
        """
        Initialize the client with an optional GitHub token and search mode.

        :param token: Personal GitHub token to increase rate limits.
        :param mode: Strategy mode, e.g., 'term' or 'org'.
        """
        self.headers = {"Authorization": f"token {token}"} if token else {}
        self.strategy = get_strategy(mode)

    def search_repositories(self, term: str, language: str | None = None, sort: str = "stars", limit: int = 5):
        """
        Search GitHub repositories using the configured strategy.

        :param term: Search term (or organization name, depending on strategy)
        :param language: Optional programming language filter
        :param sort: Sorting criterion (stars, created, etc.)
        :param limit: Max number of results to retrieve
        :return: List of repositories (JSON)
        """
        query = self.strategy.build_query(term, language)
        url = f"{self.BASE_URL}/search/repositories?q={query}&sort={sort}&per_page={limit}"

        # Try to retrieve from cache before hitting the API
        cached = cache_get(url)
        if cached:
            return cached

        # Todo: Comprobar si devuelve bien
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        data = response.json()

        # Store in cache
        cache_set(url, data)
        return data

    def get_repo_stats(self, full_name: str):
        """
        Retrieve key statistics for a GitHub repository.

        :param full_name: Repository full name in format 'owner/repo'
        :return: Dictionary with commits, contributors, and open issues
        """
        base = f"{self.BASE_URL}/repos/{full_name}"
        return {
            "commits": self._get(base + "/commits")[:3],
            "contributors": self._get(base + "/contributors"),
            "open_issues": self._get(base).get("open_issues_count", 0)
        }

# Todo: Poner docstring
    def _get(self, url: str):
        """
        Internal helper to perform a GET request with error handling and optional caching.

        :param url: Fully qualified GitHub API URL
        :return: JSON-decoded response
        """
        cached = cache_get(url)
        if cached:
            return cached

        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        cache_set(url, data)
        return data
