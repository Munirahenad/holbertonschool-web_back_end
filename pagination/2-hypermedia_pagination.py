#!/usr/bin/env python3
"""This module provides hypermedia pagination for a dataset."""

import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return the start and end indexes for a given pagination page.

    Args:
        page: The current page number, starting from 1.
        page_size: The number of items displayed on each page.

    Returns:
        A tuple containing the start index and end index.
    """
    start_index: int = (page - 1) * page_size
    end_index: int = start_index + page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize a Server instance with an empty cached dataset."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Return the cached dataset from the CSV file."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a page of rows from the dataset.

        Args:
            page: The page number to retrieve, starting from 1.
            page_size: The number of rows to include in the page.

        Returns:
            A list of rows for the requested page, or an empty list if
            out of range.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        data = self.dataset()

        return data[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Return pagination data with hypermedia metadata.

        Args:
            page: The page number to retrieve, starting from 1.
            page_size: The number of rows to include in the page.

        Returns:
            A dictionary containing the page data and pagination metadata.
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
