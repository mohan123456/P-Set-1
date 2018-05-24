a,b= input("string").split(" ")
c=0
d=len(a)
for i in range(0,d):
  if(a[i]!=b[i]):
    c=c+1
if(c==1):
  print("yess") 
else:
  print("no")       
