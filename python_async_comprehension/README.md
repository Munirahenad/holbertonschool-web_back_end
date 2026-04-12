# Python Async Comprehension

This project is part of the **Holberton School Web Back-End** curriculum.  
It focuses on **asynchronous generators**, **async comprehensions**, and running multiple asynchronous operations in parallel using `asyncio`.

## Learning Objectives

At the end of this project, I should be able to explain:

- What an asynchronous generator is
- How to use `async for`
- How to write an async comprehension
- How to run multiple coroutines in parallel with `asyncio.gather`
- How to measure the runtime of asynchronous tasks


## Tasks

### `0-async_generator.py`
Contains a coroutine called `async_generator` that loops 10 times, waits 1 second asynchronously each time, and yields a random float between `0` and `10`.

### `1-async_comprehension.py`
Contains a coroutine called `async_comprehension` that collects 10 random numbers using an async comprehension over `async_generator` and returns them as a list.

### `2-measure_runtime.py`
Contains a coroutine called `measure_runtime` that runs `async_comprehension` four times in parallel using `asyncio.gather`, measures the total runtime, and returns it.

## Author

**Munirah Alotaibi**




```python
#!/usr/bin/env python3

python_async_comprehension/
├── 0-async_generator.py
├── 1-async_comprehension.py
├── 2-measure_runtime.py
└── README.md
