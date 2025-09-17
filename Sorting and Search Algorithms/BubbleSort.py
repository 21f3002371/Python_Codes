
nums = [1,2,5,1,3,7,99,444,67]
def bubble_sort(A):
   j = len(A)-1
   while j > 0:
      for i in range(j):
         if A[i]> A[i+1]:
          A[i], A[i+1] = A[i+1], A[i]
      j-= 1   
   return A

print(bubble_sort(nums))

      