from .search_strategy import SearchStrategy

class SearchByOrgStrategy(SearchStrategy):
    """
    Concrete strategy for searching repositories inside a specific organization.
    """

    def build_query(self, org: str, language: str | None = None) -> str:
        """
        Builds a GitHub search query to find repos in a specific GitHub organization.

        :param org: GitHub organization name.
        :param language: Optional programming language filter.
        :return: A formatted query string.
        """
        query = f"org:{org}"
        if language:
            query += f"+language:{language}"
        return query