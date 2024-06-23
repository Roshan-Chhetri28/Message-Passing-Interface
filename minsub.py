from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if __name__ == "__main__":
    arr= np.empty(100, dtype='i')
    if rank ==0:
        arr = np.random.randint(0, 100, size=100, dtype=int)
    n = len(arr)
    local_n = n//size
    localArr = np.empty(local_n, dtype="i")
    
    comm.Scatter(arr, localArr, root=0)

    local_min = localArr.min()
    print(f"local min = {local_min} for rank {rank}")
    total_min = None
    if rank ==0:
        total_min = np.zeros(size, dtype='i') 
    comm.Gather(local_min, total_min)
    if rank ==0:
        
        print(f" all min = {total_min}")
        print(f" global min = {arr.min()}")
    MPI.Finalize()




