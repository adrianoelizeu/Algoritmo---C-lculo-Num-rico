#Escreve um algoritmo em python que receba as duas primeiras linhas da matriz_
 # a=| a11 a12 a13 a14|
 #   | a21 a22 a23 a24|
 #   | -1   2   3   4 |
 #   | 1   -3   4  -5 |
# e resolva o sistema Ax=b onde x=(x1,x2,x3,x4), b (-1,2,-1,3), e tenha uma unica solução.
   
def Gaussiana(A, B):
  n = len(A)
  m = len(A[0])
  matriz_U = A
  for k in range(n-1):
    d=[]
    for i in range(k,n-1):
      v=k
      while(matriz_U[v][v]==0):
        temp = matriz_U[v]
        matriz_U[v]=matriz_U[v+1]
        matriz_U[v+1]= temp
      b=matriz_U[i+1][k]
      c=matriz_U[k][k]
      a = -(b/c)
      for j in range(k,m):
        matriz_U[i+1][j]= (a*matriz_U[k][j]) + (matriz_U[i+1][j])

      B[i+1]=(a*B[k])+B[i+1]
  x=[0 for i in range(n)]
  for k in range(n-1,-1,-1):
    soma=0
    for i in range(k,n-1):
      soma = soma + A[k][i+1]*x[i+1]
    x[k]=(B[k]-soma)/matriz_U[k][k]
  return x
A = [[2, 1, -3, 2],[-1, 3, 2, 3], [-1, 2, 3, 4],[1, -3, 4, -5]]
B = [-1,2,-1, 3]
retorno = Gaussiana(A,B)

print("RESPOSTA: ")
print(retorno)