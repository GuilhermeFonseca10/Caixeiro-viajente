
V = 5
lista = []

 
# função para encontrar o tempo mínimo
def tempo(graph, v, pos, n, contador, cost):
 
  # se chegar no ultimo numero, mantem o minimo valor do custo e retona para verificar
    if (contador == n and graph[pos][0]):
        lista.append(cost + graph[pos][0])
        return
 #percorre a lista e aumenta a contagem por 1 e o custo por o valor do graph
    for i in range(n):
        if (v[i] == False and graph[pos][i]):
             
            # Marca como visitado
            v[i] = True
            tempo(graph, v, i, n, contador + 1,
                cost + graph[pos][i])
             
           # Marca como não visitado
            v[i] = False
 

 
# n é o numero de nos
if __name__ == '__main__':
    n = 4

    graph= [[ 0, 10, 15, 20 ],
            [ 10, 0, 35, 25 ],
            [ 15, 35, 0, 30 ],
            [ 20, 25, 30, 0 ]]
 
  # verifica se um numero foi visitado ou não
    v = [False for i in range(n)]
     
    # marca o no 0 como visitado
    v[0] = True
 
# encontra o minimo
    tempo(graph, v, 0, n, 1, 0)
 

    print("Tempo menor:",min(lista))
    print(max(lista))
    
 
