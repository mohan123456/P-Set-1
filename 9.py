b,r=map(int,input("Enter upper limit: ").split(" "))
k=0
for a in range(b,r):
    
    for i in range(2,a):
        if(a%i==0):
          break
    else:
       k=k+1
print(k)
