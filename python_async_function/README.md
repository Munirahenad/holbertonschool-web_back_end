# Python Async Function

This project is part of the **Holberton School Web Back-End** curriculum.  
It focuses on learning the basics of **asynchronous programming in Python** using `asyncio`.

## Learning Objectives

At the end of this project, I should be able to explain:

- What `async` and `await` mean
- How to run asynchronous coroutines
- How to execute multiple coroutines concurrently
- How to create and use `asyncio.Task`
- How to measure runtime for asynchronous execution

## Files

### `0-basic_async_syntax.py`
Contains the coroutine `wait_random` that waits for a random delay between `0` and `max_delay`, then returns that delay.

### `1-concurrent_coroutines.py`
Contains the coroutine `wait_n` that runs `wait_random` multiple times concurrently and returns the delays in ascending order.

### `2-measure_runtime.py`
Contains the function `measure_time` that measures the average execution time of `wait_n`.

### `3-tasks.py`
Contains the function `task_wait_random` that returns an `asyncio.Task`.

### `4-tasks.py`
Contains the coroutine `task_wait_n` that works like `wait_n` but uses tasks instead.

```python
#!/usr/bin/env python3


## Project Structure

```bash
python_async_function/
├── 0-basic_async_syntax.py
├── 1-concurrent_coroutines.py
├── 2-measure_runtime.py
├── 3-tasks.py
├── 4-tasks.py
└── README.md
