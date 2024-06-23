import numpy as np
import time 
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
def oesort(localArray, local_n):
   for index in range(local_n):
       
       if index%2 != 0:
           for j in range(0,local_n-1):
               if localArray[j] > localArray[j+1]:
                   localArray[j], localArray[j+1]= localArray[j+1], localArray[j]
       else:
            for j in range(0, len(localArray)-1):
                  if localArray[j] > localArray[j+1]:
                     localArray[j], localArray[j+1]= localArray[j+1], localArray[j]
   print(f"rank {rank} after sort: {localArray}\n")

def main():
   n=4000
   local_n = 4000//size
   
   if rank ==0:
      localArray = np.empty(local_n, dtype=int)
      arr = np.random.randint(0, 100, size=4000)
   else:
      arr = None
      localArray = np.zeros(local_n, dtype='i')

   comm.Scatter(arr, localArray, root=0)

   start = time.time()
   print(f"before sort: {localArray}\n")
   
   oesort(localArray, local_n)
   end = time.time()

   parr = end - start
   sortedArray = None
   if rank ==0:
      sortedArray = np.zeros(n, dtype=int)
   comm.Gather(localArray, sortedArray)
   end = time.time()
   if rank ==0:
      start = time.time()
      oesort(sortedArray, n)
      end = time.time()
      ser = end - start
      print(f"after sort: {sortedArray} with runtime complexity in parallel is {parr} and serial is {ser} \n")
   
       
if __name__ == "__main__":
   main()