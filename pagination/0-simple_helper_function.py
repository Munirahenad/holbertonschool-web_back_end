#!/usr/bin/env python3
"""Simple helper function for pagination."""


def index_range(page: int, page_size: int) -> tuple:
    """Return start and end indexes for pagination.

    Args:
        page: The current page number, starting from 1.
        page_size: The number of items per page.

    Returns:
        A tuple containing the start index and end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)
