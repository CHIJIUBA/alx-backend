#!/usr/bin/env python3
import csv
import math
from typing import List, Tuple, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """Returns the start and end index pagination"""
        end_index = page * page_size
        start_index = end_index - page_size
        return (start_index, end_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retuns the contents of the current page
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        my_tuple = self.index_range(page, page_size)
        return self.dataset()[my_tuple[0]:my_tuple[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Returns page, page_size, data, next_page, prev_page, total_page
        """
        data_length = len(self.dataset())
        if (data_length % page_size == 0):
            total_page = int(data_length / page_size)
        else:
            total_page = int(data_length / page_size) + 1
        if (page <= 1):
            prev_page = None
        else:
            prev_page = page - 1
        if (page >= total_page):
            next_page = None
        else:
            next_page = page + 1
        return {
            'page_size': len(self.get_page(page, page_size)),
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_page
        }
