import time
import matplotlib.pyplot as plt

letra = 'a'
times = []
while letra != 'f':
    inicio = time.time()
    file = open("dataset-2-"+letra+".csv","r+")
    listaFile = (file.read().split("\n"))
    file.close()
    listaFile = list(map(int, listaFile))
    timeMedia = time.time() - inicio
    times.append(timeMedia)
    maior = max(listaFile)

    novoDocA = open("resposta-dataset-2-"+letra+".txt", "w")
    novoDocA.write(str(maior) + "\n" + str(timeMedia))
    novoDocA.close()
    letra = (chr(ord(letra) + 1))

plt.plot(times)
plt.title("Gráfico Plot")
plt.show()
    


