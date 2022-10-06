# THREADS

Generaly we using threads when wanted to execute a process at once or to work with operations in bulk.
An example of some cases to use.

1. We'll simulate multiple process runs at once and when one of process finish it's continue, other processes will are running. [show example](process_data_at_once_example.py)

2. Process bulk data with threads [show example](process_bulk_data.py)

Obs: It's only example over how threads runs.

I already push an example using Golang on my repository specificaly how to work with multithreads and channels to pass data to these.

Note: you might be asking the question: what if while the processes are running one of them has a problem, will the application crash?

The answer would be: it won't, the threads already self-manage this issue, it will simply skip the error notification if there is something to handle and continue as normal.