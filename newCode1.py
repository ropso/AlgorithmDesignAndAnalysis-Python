length,powx,powy=list(map(int,input().split(" ")))
number=int(input())
divisor=10**powx
multiple=number//(divisor)
no=number-(multiple*(divisor))
i=powx-1
if no>(divisor//2):
    #the adding it
    while no%divisor!=0:
        if no+(10**i)<=divisor:
            no=no+(10**i)
        else:
            pass
else:
    while no%divisor!=0:
        if 

