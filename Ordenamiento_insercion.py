a=[3,9,6,8,5,4,2]
for i in range (1,len(a)):
    j=i
    while j>0 and a[j-1]> a[j]:
        a[j],a[j-1] = a[j-1],a[j]
        j=j-1

print("Lista ordenada por inserción:", a)

def Ordenamientoinsercion(lst):
    n=len(lst)
    for pasada in range(1,n):
        nuePos=pasada
        while nuePos > 0 and lst[nuePos-1]>lst[nuePos]:
        
                lst[nuePos], lst[nuePos]= lst[nuePos], lst[nuePos-1]


a=[7,3,5,6,11,2,12]
Ordenamientoinsercion(a)
print(a)