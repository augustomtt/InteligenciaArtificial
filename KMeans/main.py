import random

import matplotlib.pyplot as plt



def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


def kmeans(K, puntos):
    iter = 0
    c1 = [7,1]
    c2 = [1,5]
    asignados = []
    for i in puntos:
        asignados.append(-1)
    change = True
    while change:
        change = False
        for x in puntos:
            if distance(x, c1) < distance(x, c2):
                if asignados[puntos.index(x)] != 1:
                    change = True
                asignados[puntos.index(x)] = 1
            else:
                if asignados[puntos.index(x)] == 1:
                    change = True
                asignados[puntos.index(x)] = 2

        acumsx = [0, 0]
        acumsy = [0, 0]
        conts = [0, 0]
        for i in range(0, len(asignados)):
            acumsx[asignados[i]-1] += puntos[i][0]
            acumsy[asignados[i]-1] += puntos[i][1]
            conts[asignados[i]-1] += 1
    if(conts[0]!=0):
        c1 = [acumsx[0]/conts[0],acumsy[0]/conts[0]]
    if (conts[1] != 0):
        c2 = [acumsx[1] / conts[1],acumsy[1]/conts[1]]
        print("Iteracion "+ str(iter+1) + ": C1/C2 --> )" + str(c1) +"/"+ str(c2))
        iter = iter +1
    print("Fin del algoritmo");


    return [c1,c2]


if __name__ == '__main__':
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    # Generar un conjunto de puntos (x,y), reduciendo dimensiones de data
    puntos = [[1, 1], [2, 2], [1, 2], [3, 1], [5, 8], [5, 9], [6, 8]]
    clustercenters = kmeans(2, puntos)
    for i in puntos:
        if (distance(i, clustercenters[0]) < distance(i, clustercenters[1])):
            x1.append(i[0])
            y1.append(i[1])
        else:
            x2.append(i[0])
            y2.append(i[1])
    plt.plot(x1,y1,linestyle="None",marker="o",color="red") #puntos grupo 1
    plt.plot(x2, y2, linestyle="None", marker="o", color="blue")  # puntos grupo 2
    plt.plot(clustercenters[0][0],clustercenters[0][1],marker="x",linestyle="None") #cluster1
    plt.plot(clustercenters[1][0], clustercenters[1][1], marker="x", linestyle="None")  # cluster2
    plt.show()
