# Parallel Python Tutorial
This directory includes examples of two ways to perform parallel processing in Python.

# Multiprocessing

# Joblib ([fibonacci_joblib.py](./fibonacci_joblib.py))
For tasks that are embarassingly parallel or uses NumPy arrays, joblib can be a more efficient and convenient solution. In this tutorial we will use joblib to compute Fibonacci numbers in parallel.

In line 23 of this example, n_jobs or the number of parallel processes, should match the number of CPUs or tasks you request in order to see any runtime improvements.