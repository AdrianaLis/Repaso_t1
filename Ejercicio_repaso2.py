"""
1. Registrar estudiantes nombres, apellidos,dni y nrc
2. Agregarlos
3.Buscarlos por nrc
4.Eliminarlos por nrc

"""
class Estudiante:
    def __init__(self, nombre ="",apellidos= "", dni=0, nrc=0):
        self.nombre= nombre
        self.apellidos= apellidos
        self.dni=dni
        self.nrc= nrc
    def __str__(self):
        return f" Estudiante:{self.nombre} y su DNI:{self.dni} con NRC: {self.nrc}"
    
def ingresar(lst,st)-> bool:
        for m in lst:
         if m.nrc== st.nrc and m.apellidos == st.apellidos and m.nombre==st.nombre and m.dni== st.dni:
             return True
         return False
def buscar_estudiante(lst, nrc_buscado) -> bool:
    for m in lst:
        if m.nrc == nrc_buscado:
            return m # Lo encontró
    return None # No existe
        
def ordSeleccion(lst):
    n = len(lst)
    for mano in range(n-1):
        posMayor = mano
        for ver in range(mano + 1, n):
            if lst[ver].nrc > lst[posMayor].nrc:
                posMayor = ver
        lst[mano], lst[posMayor] = lst[posMayor], lst[mano]

def ordSeleccionNRC(lst):
    n = len(lst)
    for mano in range(n - 1):
        posMenor = mano
        for ver in range(mano + 1, n):
            if lst[ver].nrc < lst[posMenor].nrc: 
                posMenor = ver     
        lst[mano], lst[posMenor] = lst[posMenor], lst[mano]

lista=[]
while True:
    opc= int(input( "1. Registrar - 2. Agregarlos - 3. Buscarlos - 4.ELiminarlos- 5. Ordenar 0. Salir"))
    if opc==1:

        nombre= input("Ingrese nombres\n")
        apellidos= input("Ingrese apellidos\n")
        dni=int(input("Ingrese DNI\n"))
        nrc= int(input("Ingrese NRC\n"))
        nuevo= Estudiante(nombre, apellidos, dni, nrc)
        if not  ingresar(lista, nuevo):
            print(nuevo)
            lista.append(Estudiante(nombre, apellidos, dni, nrc))
            print(len(lista))      
    elif opc==2:
        print("\n--- LISTA DE ESTUDIANTES REGISTRADOS ---")
        for e in lista:
            print(e) # Esto usa tu método __str__ de la clase Estudiante
        print(f"Total registrados: {len(lista)}\n")
    elif opc==3:
        nrc_a_buscar = int(input("Ingrese el nrc del estudiante a buscar: "))
        estudiante_encontrado = buscar_estudiante(lista, nrc_a_buscar)
        if estudiante_encontrado != None:
            print("--- Estudiante Encontrado ---")
            print(estudiante_encontrado)
        else:
             print(f"No se encontró ningún estudiante con el NRC: {nrc_a_buscar}")
       
    elif opc==4:
        ordSeleccion(lista)
        elinrc= int(input("Ingrese el nrc a eliminar"))
        for idx, q in enumerate (lista):
            if q.nrc == elinrc:
                del lista [idx]
    elif opc==5:
        if len(lista) > 0:
          ordSeleccionNRC(lista) # Llamamos a la función
          print("\n--- LISTA ORDENADA POR NRC ---")
        for est in lista:
            print(est)
    else:
        print("Saliendooo")            
            
