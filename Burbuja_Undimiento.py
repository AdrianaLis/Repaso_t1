
"""
for i in range(len(a) - 1):
    for j in range(len(a) - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print("Lista ordenada con éxito:")
print(a)

"""

def OrdenamientoBurbuja(lst):
    n=len(lst)
    for pasada in range(n-1):
        for izqPar in range(0,n- pasada -1):
            derPar= izqPar+1
            if lst[izqPar]> lst[derPar]:
                lst[izqPar], lst[derPar]= lst[derPar], lst[izqPar]


a=[7,3,5,6,11,2,12]
OrdenamientoBurbuja(a)
print(a)

