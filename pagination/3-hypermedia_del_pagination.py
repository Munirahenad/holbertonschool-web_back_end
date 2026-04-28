#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination."""

import csv
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize a Server instance with empty cached datasets."""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Return the cached dataset from the CSV file."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Return the dataset indexed by sorting position starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }

        return self.__indexed_dataset

    def get_hyper_index(
        self,
        index: int = None,
        page_size: int = 10
    ) -> Dict:
        """Return a deletion-resilient page with pagination metadata.

        Args:
            index: The start index to retrieve from the indexed dataset.
            page_size: The number of rows to include in the page.

        Returns:
            A dictionary containing index, data, page_size, and next_index.
        """
        indexed_data = self.indexed_dataset()

        if index is None:
            index = 0

        assert isinstance(index, int)
        assert isinstance(page_size, int)
        assert index >= 0 and index < len(self.dataset())
        assert page_size > 0

        data = []
        next_index = index

        while len(data) < page_size and next_index < len(self.dataset()):
            if next_index in indexed_data:
                data.append(indexed_data[next_index])
            next_index += 1

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index,
        }
