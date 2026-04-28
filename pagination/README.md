# Pagination

This project covers different pagination techniques in Python using a CSV dataset.

## Learning Objectives

- How to paginate a dataset using `page` and `page_size` parameters.
- How to calculate the correct start and end indexes for pagination.
- How to return pagination metadata using hypermedia.
- How to build deletion-resilient pagination using indexed datasets.

## Files

| File | Description |
|---|---|
| `0-simple_helper_function.py` | Contains `index_range`, a helper function that returns the start and end indexes for pagination. |
| `1-simple_pagination.py` | Implements simple pagination using `page` and `page_size`. |
| `2-hypermedia_pagination.py` | Implements pagination with hypermedia metadata such as next page, previous page, and total pages. |
| `3-hypermedia_del_pagination.py` | Implements deletion-resilient hypermedia pagination using indexed data. |
| `Popular_Baby_Names.csv` | Dataset used for pagination examples. |



```python
#!/usr/bin/env python3
