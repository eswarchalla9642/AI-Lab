def toh(n,fro,to,aux):
    if n==1:
        print("move disk 1 from rod ",fro," to rod ",to)
        return
    toh(n-1,fro,aux,to)
    print("move disk",n,"from rod ",fro," to rod ",to)
    toh(n-1,aux,to,fro)
toh(3,'a','b','c')