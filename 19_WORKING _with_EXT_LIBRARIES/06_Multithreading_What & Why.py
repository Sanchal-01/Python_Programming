# MULTITHREADING IN PYTHON
#=========================

# If we want to execute multiple I/O bound task we use THREADS.

# THREADS vs PROCESS:
# A process is an independent execution environment with its own isolated memory space,
# A thread is a smaller, lightweight unit of execution that runs inside a process and shares its memory space with other peer threads.

# Example:
# Web browsers like ⁠Google Chrome run individual browser tabs as separate processes. If a web page inside one tab completely freezes or crashes, your other open tabs
# remain perfectly safe and operational. This is called a PROCESS.

# Text editors like Microsoft Word use threads. One thread handles typing and UI responsiveness while a second background thread automatically checks your spelling.
# Since MS Word itself is a Process running AS an isolated software and using its own CPU and memory but inside this process it is using multiple threads for different tasks.

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# What is Multithreading in Python?
# Multithreading in Python is a technique that allows a single Python process to run multiple threads (smaller, concurrent paths of execution) at the same time to perform tasks in parallel.

# However, Python features a highly unique mechanism called the Global Interpreter Lock (GIL). Because of the GIL, Python threads do not run in true parallel on multiple CPU cores.
# Instead, they take turns running on a single core.

# How Multithreading Works in Python?
# Python provides a built-in module called ⁠threading to create and manage threads.
# When you start multiple threads in Python, the operating system attempts to distribute them. However, the GIL ensures that only one thread executes Python bytecode at any given microsecond.
# The Python interpreter rapidly switches back and forth between your threads, giving the illusion of simultaneous execution.

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# The GIL Bottleneck: When to Use It (and When Not To)

# 1. I/O-Bound Tasks (Highly Effective)

# What they are?
# Tasks where the program spends most of its time waiting for external responses (e.g., web scraping, downloading files, API calls, or reading/writing to a database).

# Why threads work:
# When a Python thread waits for a network response, it releases the GIL. This allows another thread to jump in and do work while the first one waits.Result: Massive speed improvements.
# Result: Massive speed improvements.



# 2. CPU-Bound Tasks (Ineffective / Slower)

# What they are?
# Tasks that require heavy mathematical calculations, data processing, or image rendering (e.g., machine learning training or matrix multiplication).

# Why threads fail?
# The threads constantly fight each other to grab the single GIL lock. The overhead of constantly switching between threads actually makes the program run slower than a simple, single-threaded program.
# Result: No performance gain, potential slowdown.