import time 
import numpy as np
from time import time
import multiprocessing as mp
print("Number of processors: ", mp.cpu_count())


import multiprocessing

output = mp.Queue()

# define a example function
def hold(nn, output):
    import time 
    t0 = time.time()
    while t0+10>time.time():
        pass
    output.put(nn)

# Setup a list of processes that we want to run
processes = [mp.Process(target=hold, args=(x, output)) for x in range(8)]

# Run processes
for p in processes:
    p.start()

# Exit the completed processes
for p in processes:
    p.join()

# Get process results from the output queue
results = [output.get() for p in processes]

print(results)

exit()


import time 
from joblib import Parallel, delayed 
# A function that can be called to do work:
def work(arg):    
    print("Function receives the arguments as a list:", arg)
    # Split the list to individual variables:
    i, j = arg    
    # All this work function does is wait 1 second...
#     time.sleep(1)  
    t0 = time.time()
    while t0+10>time.time():
        pass
    # ... and prints a string containing the inputs:
    print("%s_%s" % (i, j))
    return "%s_%s" % (i, j)
# List of arguments to pass to work():
arg_instances = [(1, 1), (1, 2), (1, 3), (1, 4)]
# Anything returned by work() can be stored:
results = Parallel(n_jobs=4, verbose=1, backend="threading")(map(delayed(work), arg_instances))
print(results)




