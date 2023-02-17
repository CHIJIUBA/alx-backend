#!/usr/bin/env python3
"""
Returns the start and end index pagination
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns the start and end index pagination"""
    end_index = page * page_size
    start_index = end_index - page_size
    return (start_index, end_index)
