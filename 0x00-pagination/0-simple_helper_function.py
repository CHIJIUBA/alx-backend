#!/usr/bin/env python3
"""
Returns the start and end index pagination
"""


def index_range(page, page_size):
    """Returns the start and end index pagination"""
    end_index = page * page_size
    start_index = end_index - page_size
    return (start_index, end_index)
