
def transpose(a):
    b=[]
    for i in range(len(a[0])):
        row=[]
        for j in a:
            row.append(j[i])
        b.append(row)
    return b

def sum(a,b):
    for i in range(len(a)):
        for j in range(len(a[0])):
            b[i][j]+=a[i][j]
    return b

mat =  [
        [1,2],
        [3,4],
        [5,6]
       ]


print(transpose(mat),sum(mat,mat))