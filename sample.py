
      
# Linear search

pos=-1
s1 = [3,4,2,6,5,8,1,10,9,7,12]
n=6


def search(s1,n):
  i=0
  while i<len(s1):
    if s1[i]==n:
      globals()['pos']=i
      return True
    i=i+1
  return False



if search(s1,n):
  print("Found at ",pos)
else:
  print("Not Found")
