# Bearbeitet durch Eric Böwer

import math
import threading


# Leibniz algo should run way faster but because the Global Interpreter Lock (GIL)
# does not allow parallel execution of Python Code in multiple Threads,
# one could use multiprocessing but that is way over my head and would just be me copying code
# I think it makes more sense to actually talk about that in the meeting

def partOfLeibniz(start, end):
    sumPart = 0.0
    for k in range(start, end):
        sumPart += ((-1) ** k) / (2 * k + 1)
    return sumPart


if __name__ == "__main__":
    numberOfThreads = 12
    numberOfLeibnizIterations = 10000000
    threads = []
    partialSumOfLeibniz = []

    iterationCountPerThread = numberOfLeibnizIterations // numberOfThreads
    print("Starting: ", numberOfThreads, " Threads with each Thread computing: ", iterationCountPerThread,
          " Leibniz iterations")
    # there could be some rest computations to do,
    # we do them on the main thread afterward, not ideal, but it is what it is
    restIterations = numberOfLeibnizIterations % numberOfThreads
    for i in range(numberOfThreads):
        start = i * iterationCountPerThread
        end = start + iterationCountPerThread
        thread = threading.Thread(target=lambda: partialSumOfLeibniz.append(partOfLeibniz(start, end)))
        threads.append(thread)
        thread.start()

    # Blocking main thread until every async thread has finished its computation
    for x in threads:
        x.join()

    # Compute rest on main thread
    if restIterations > 0:
        print("Computing rest")
        partialSumOfLeibniz.append(partOfLeibniz(numberOfThreads * iterationCountPerThread, numberOfLeibnizIterations))

    res = sum(partialSumOfLeibniz) * 4

    print(res)
    print(math.pi)
    print("Diff: '{:.10f}'".format(math.pi - res))
