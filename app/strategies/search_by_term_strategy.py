from .search_strategy import SearchStrategy

class SearchByTermStrategy(SearchStrategy):
    """
    Concrete strategy for searching by keyword terms.
    """

    def build_query(self, term: str, language: str | None = None) -> str:
        """
        Builds a GitHub search query string for a general keyword search.

        :param term: Search keyword (e.g. 'transport')
        :param language: Optional programming language filter.
        :return: A formatted query string for GitHub API.
        """
        query = term
        if language:
            query += f"+language:{language}"
        return query
