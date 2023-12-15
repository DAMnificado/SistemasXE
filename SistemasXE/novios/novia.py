def pirola(n1):
    sumador = 0
    for i in range(1,n1+1):
        if n1%i==0:
           sumador += i
    return sumador



resultado1=pirola(1050)
resultado2=pirola(1925)


if 1050+1925+1 == resultado1 and resultado1==resultado2:
    print("novios")
