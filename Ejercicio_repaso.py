
class zapato:
    def __init__(self, modelo = "", talla = 0, precio = 0):
        self.modelo = modelo 
        self.talla = talla 
        self.precio = precio
    
    def __str__(self):
        return f"{self.modelo} - {self.talla} (S/{self.precio})"
    
    def __repr__(self):
        return f"{self.modelo} [{self.talla}] S/{self.precio}"


def buscaZapato(lst,zapa)-> bool :
    for z in lst:
        if z.modelo== zapa.modelo and z.talla==zapa.talla and z.precio==zapa.precio:
             return True
    return False


def ordSeleccion(lst):
    n=len(lst)
    for mano in range(n-1):
        posMayor = mano
        for ver in range(mano+1,n):
            if lst[ver].talla > lst[posMayor].talla:
                posMayor=ver
        lst [mano], lst [posMayor]=lst[posMayor], lst[mano]       
        


lista = []        
while True:
    opc = int(input("1-Agregar, 2-Listar, 3-BorraTalla, 9-Salir"))

    if opc==1 :
        modelo = input("Ingrese modelo")
        talla=int(input("Ingrese talla"))
        precio=float(input("Ingrese precio"))
        nuevo= zapato(modelo, talla, precio)

        if not buscaZapato(lista, nuevo):
            print(nuevo)
            lista.append(zapato(modelo, talla, precio))
            print(len(lista))
       
    elif opc==2:
            print(lista)
    elif opc==3:
        ordSeleccion(lista)
        elitalla= int(input("Ingrese talla a eliminar"))
        for idx, q in enumerate (lista):
            if q.talla == elitalla:
                del lista [idx]


        