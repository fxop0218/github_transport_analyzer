from abc import ABC, abstractmethod

class SearchStrategy(ABC):
    """
    Abstract base class for search strategies to build GitHub query strings.
    """

    @abstractmethod
    def build_query(self, term: str, language: str | None = None) -> str:
        """
        Construct the search query to be used with GitHub's API.

        :param term: Main term to search for.
        :param language: Optional language filter.
        :return: GitHub search query string.
        """
        pass