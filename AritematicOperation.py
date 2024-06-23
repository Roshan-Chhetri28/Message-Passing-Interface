from mpi4py.MPI import COMM_WORLD as comm

size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    print(1+2)
if rank ==1:
    print(2-1)
if rank ==3:
    print (2*3)
