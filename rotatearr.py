

def RightRotate(a, n, k):
     
  
    k = k % n;
 
    for i in range(0, n):
 
        if(i < k):
 
          
            print(a[n + i - k], end = " ");
 
        else:
 
       
            print(a[i - k], end = " ");
 
    print("\n");
arr=[]
n=int(input("enter the no of elements"))
for i in range(n):
    a=int(input("enter the elements"))
    arr.append(a)
print(arr) 
k=int(input("enter the no of rotation"))
     
RightRotate(arr, n, k);
    