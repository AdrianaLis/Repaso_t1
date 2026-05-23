cubos=[4,5,9,2,3]
def ordSeleccion(lst):
    n=len(lst)
    for mano in range(n-1):
        posMayor = mano
        print(f"Actualmente mano vale: {mano}")
        for ver in range(mano+1,n):
            if lst[ver].talla > lst[posMayor].talla:
                posMayor=ver
        lst [mano], lst [posMayor]=lst[posMayor], lst[mano]       
