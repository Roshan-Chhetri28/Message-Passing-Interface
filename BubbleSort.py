from mpi4py import MPI
import numpy as np


def bubbleSort(localArray):
    local_n = len(localArray)
    for i in range(local_n):
        for j in range(0, local_n-i-1):
            if(localArray[j]>localArray[j+1]):
                localArray[j], localArray[j+1] = localArray[j+1], localArray[j]


def bubb():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    local_n = 40//size
    if rank == 0:
        arr = np.random.randint(0, 100, size=40)
    else:
        arr = None    


    localArray = np.zeros(local_n, dtype=int)
    comm.Scatter(arr, localArray, root=0)
    print(f" array: {localArray}")

    comm.Barrier()
    bubbleSort(localArray)

    sortedArray = None
    if rank == 0:
        sortedArray = np.zeros(40, dtype=int)
    comm.Gather(localArray, sortedArray)

    if rank == 0:
        sortedArray = np.sort(sortedArray, axis=0, kind="mergesort")
        print(f"sorted array: {sortedArray}")
    MPI.Finalize()


if __name__ == "__main__":
    bubb()