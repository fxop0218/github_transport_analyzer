from .search_by_term_strategy import SearchByTermStrategy
from .search_by_org_strategy import SearchByOrgStrategy
from .search_strategy import SearchStrategy

def get_strategy(mode: str) -> SearchStrategy:
    """
    Factory method to retrieve the appropriate SearchStrategy instance.

    :param mode: Strategy type: 'term' or 'org'
    :return: Concrete instance of SearchStrategy
    :raises ValueError: If mode is not recognized
    """
    if mode == "term":
        return SearchByTermStrategy()
    elif mode == "org":
        return SearchByOrgStrategy()
    else:
        raise ValueError(f"Unknown search strategy mode: {mode}")
