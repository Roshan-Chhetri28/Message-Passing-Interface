from mpi4py.MPI import COMM_WORLD as comm 
import numpy as np

size = comm.Get_size()
rank = comm.Get_rank()
 

if __name__ == "__main__":
    arr1= [1,2, 3]
    arr2 = [3, 2, 1]
    a = np.empty((3,3), dtype=int) 
    b = np.empty((3,3), dtype=int) 
    local_n = 3//size
    local_b = np.empty(( local_n,3), dtype=int)
    if rank ==0:
        a = np.array([arr1, arr1, arr1])
        b=  np.array([arr2 , arr2, arr2])
    comm.Scatter(b, local_b, root=0)
    print(local_b)
    comm.Bcast(a, root=0)


    c = np.matmul( local_b, a)
    add = np.add(local_b, a)
    print(f"mul = {c} and add = {add} for {rank}\n")

    mul = np.empty((3,3), dtype=int)
    a_add = np.empty((3,3), dtype=int)
    comm.Gather(c, mul)
    if rank ==0:
        print(f"mul = {mul}\n")
    comm.Gather(add,a_add)
    if rank ==0:
        print(f"a_add = {a_add}\n")