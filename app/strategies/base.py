from abc import ABC, abstractmethod

class SearchStrategy(ABC):
    @abstractmethod
    def build_query(self, term: str, language: str | None) -> str:
        """
        Define the query structure to be used with GitHub API.
        """
        pass
