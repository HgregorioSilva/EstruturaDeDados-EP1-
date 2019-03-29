'''
---------------------------
-##########EP1############-
---------------------------
Aluno: Henrique Gregório Silva
RA: 1460281523016
Matéria: Estrutura de Dados
Professor: Fernando Masanori Ashikaga
'''

import random
import time


###########FUNÇÃO PARA GERAR VETOR ALEATÓRIO PELA QUANTIDADE DE NÚMEROS NECESSÁRIOS##########
def geraVetorAleatorio(Vquantidade):
    vetor = []
    for x in range (Vquantidade):
        n = 0
        while (n in vetor):
            n = random.randint(1,(Vquantidade + 1000))
        vetor.append(n)
    return vetor

###########MERGESORT##########
def merge(e, d):
    r = []
    i, j = 0, 0
    while i < len(e) and j < len(d):
        if e[i] <= d[j]:
            r.append(e[i])
            i += 1
        else:
            r.append(d[j])
            j += 1
    r += e[i:]
    r += d[j:]
    return r

def mergesort(v):
    if len(v) <= 1:
        return v
    else:
        m = len(v) // 2
        e = mergesort(v[:m])
        d = mergesort(v[m:])
        return merge(e, d)

##########QUICKSORT##########
def quicksort(lista):
    if len(lista) <= 1: 
        return lista
    
    pivô = lista[0]
    iguais  = [x for x in lista if x == pivô]
    menores = [x for x in lista if x <  pivô]
    maiores = [x for x in lista if x >  pivô]
    return quicksort(menores) + iguais + quicksort(maiores)

##########SELECTION##########
def selection(v):
  resp = []
  while v:
    m = min(v)
    resp.append(m)
    v.remove(m)
  return resp

##########FUNÇÕES PARA TEMPO DE EXECUÇÃO########
def tempoMerge(vetor):
    random.shuffle(vetor)
    inicio = time.time()
    mergesort(vetor)
    fim = time.time()
    tempo = fim - inicio
    return tempo

def tempoQuicksort(vetor):
    random.shuffle(vetor)
    inicio = time.time()
    quicksort(vetor)
    fim = time.time()
    tempo = fim - inicio
    return tempo

def tempoSelection(vetor):
    random.shuffle(vetor)
    inicio = time.time()
    selection(vetor)
    fim = time.time()
    tempo = fim - inicio
    return tempo

def tempoSort(vetor):
    random.shuffle(vetor)
    inicio = time.time()
    vetor.sort()
    fim = time.time()
    tempo = fim - inicio
    return tempo



#UTILIZADO FUNÇÃO PARA GERAR VETORES ALEATÓRIOS
vetorDe2000 = geraVetorAleatorio(2000)
vetorDe4000 = geraVetorAleatorio(4000)
vetorDe6000 = geraVetorAleatorio(6000)
vetorDe8000 = geraVetorAleatorio(8000)
vetorDe10000 = geraVetorAleatorio(10000)
vetorDe12000 = geraVetorAleatorio(12000)
vetorDe14000 = geraVetorAleatorio(14000)
vetorDe16000 = geraVetorAleatorio(16000)
vetorDe18000 = geraVetorAleatorio(18000)
vetorDe20000 = geraVetorAleatorio(20000)  
vetorDe22000 = geraVetorAleatorio(22000)


#GERANDO TEMPO DE EXECUÇÃO PARA 2000
tempoMerge2000 = tempoMerge(vetorDe2000)
tempoQuicksort2000 = tempoQuicksort(vetorDe2000)
tempoSelection2000 = tempoSelection(vetorDe2000)
tempoSort2000 = tempoSort(vetorDe2000)
#GERANDO TEMPO DE EXECUÇÃO PARA 4000
tempoMerge4000 = tempoMerge(vetorDe4000)
tempoQuicksort4000 = tempoQuicksort(vetorDe4000)
tempoSelection4000 = tempoSelection(vetorDe4000)
tempoSort4000 = tempoSort(vetorDe4000)
#GERANDO TEMPO DE EXECUÇÃO PARA 6000
tempoMerge6000 = tempoMerge(vetorDe6000)
tempoQuicksort6000 = tempoQuicksort(vetorDe6000)
tempoSelection6000 = tempoSelection(vetorDe6000)
tempoSort6000 = tempoSort(vetorDe6000)
#GERANDO TEMPO DE EXECUÇÃO PARA 8000
tempoMerge8000 = tempoMerge(vetorDe8000)
tempoQuicksort8000 = tempoQuicksort(vetorDe8000)
tempoSelection8000 = tempoSelection(vetorDe8000)
tempoSort8000 = tempoSort(vetorDe8000)
#GERANDO TEMPO DE EXECUÇÃO PARA 10000
tempoMerge10000 = tempoMerge(vetorDe10000)
tempoQuicksort10000 = tempoQuicksort(vetorDe10000)
tempoSelection10000 = tempoSelection(vetorDe10000)
tempoSort10000 = tempoSort(vetorDe10000)
#GERANDO TEMPO DE EXECUÇÃO PARA 12000
tempoMerge12000 = tempoMerge(vetorDe12000)
tempoQuicksort12000 = tempoQuicksort(vetorDe12000)
tempoSelection12000 = tempoSelection(vetorDe12000)
tempoSort12000 = tempoSort(vetorDe12000)
#GERANDO TEMPO DE EXECUÇÃO PARA 14000
tempoMerge14000 = tempoMerge(vetorDe14000)
tempoQuicksort14000 = tempoQuicksort(vetorDe14000)
tempoSelection14000 = tempoSelection(vetorDe14000)
tempoSort14000 = tempoSort(vetorDe14000)
#GERANDO TEMPO DE EXECUÇÃO PARA 16000
tempoMerge16000 = tempoMerge(vetorDe16000)
tempoQuicksort16000 = tempoQuicksort(vetorDe16000)
tempoSelection16000 = tempoSelection(vetorDe16000)
tempoSort16000 = tempoSort(vetorDe16000)
#GERANDO TEMPO DE EXECUÇÃO PARA 18000
tempoMerge18000 = tempoMerge(vetorDe18000)
tempoQuicksort18000 = tempoQuicksort(vetorDe18000)
tempoSelection18000 = tempoSelection(vetorDe18000)
tempoSort18000 = tempoSort(vetorDe18000)
#GERANDO TEMPO DE EXECUÇÃO PARA 20000
tempoMerge20000 = tempoMerge(vetorDe20000)
tempoQuicksort20000 = tempoQuicksort(vetorDe20000)
tempoSelection20000 = tempoSelection(vetorDe20000)
tempoSort20000 = tempoSort(vetorDe20000)
#GERANDO TEMPO DE EXECUÇÃO PARA 22000
tempoMerge22000 = tempoMerge(vetorDe22000)
tempoQuicksort22000 = tempoQuicksort(vetorDe22000)
tempoSelection22000 = tempoSelection(vetorDe22000)
tempoSort22000 = tempoSort(vetorDe22000)






print ("""
-----------------------------------------------------------------------
            |                      time(s)                            |
-----------------------------------------------------------------------
            |  Mergesort      Quicksort      Selection      Native    |""")
print("{0:11} {1} {2:10.2f} {3:14.2f} {4:14.2f} {5:11.2f} {6:>4}".format("2000","|",tempoMerge2000,tempoQuicksort2000,tempoSelection2000,tempoSort2000,"|"))
print("{0:11} {1} {2:10.2f} {3:14.2f} {4:14.2f} {5:11.2f} {6:>4}".format("4000","|",tempoMerge4000,tempoQuicksort4000,tempoSelection4000,tempoSort4000,"|"))
print("{0:11} {1} {2:10.2f} {3:14.2f} {4:14.2f} {5:11.2f} {6:>4}".format("6000","|",tempoMerge6000,tempoQuicksort6000,tempoSelection6000,tempoSort6000,"|"))
print("{0:11} {1} {2:10.2f} {3:14.2f} {4:14.2f} {5:11.2f} {6:>4}".format("8000","|",tempoMerge8000,tempoQuicksort8000,tempoSelection8000,tempoSort8000,"|"))
print("{0:11} {1} {2:10.2f} {3:14.2f} {4:14.2f} {5:11.2f} {6:>4}".format("10000","|",tempoMerge10000,tempoQuicksort10000,tempoSelection10000,tempoSort10000,"|"))
print("{0:11} {1} {2:10.2f} {3:14.2f} {4:14.2f} {5:11.2f} {6:>4}".format("12000","|",tempoMerge12000,tempoQuicksort12000,tempoSelection12000,tempoSort12000,"|"))
print("{0:11} {1} {2:10.2f} {3:14.2f} {4:14.2f} {5:11.2f} {6:>4}".format("14000","|",tempoMerge14000,tempoQuicksort14000,tempoSelection14000,tempoSort14000,"|"))
print("{0:11} {1} {2:10.2f} {3:14.2f} {4:14.2f} {5:11.2f} {6:>4}".format("16000","|",tempoMerge16000,tempoQuicksort16000,tempoSelection16000,tempoSort16000,"|"))
print("{0:11} {1} {2:10.2f} {3:14.2f} {4:14.2f} {5:11.2f} {6:>4}".format("18000","|",tempoMerge18000,tempoQuicksort18000,tempoSelection18000,tempoSort18000,"|"))
print("{0:11} {1} {2:10.2f} {3:14.2f} {4:14.2f} {5:11.2f} {6:>4}".format("20000","|",tempoMerge20000,tempoQuicksort20000,tempoSelection20000,tempoSort20000,"|"))
print("{0:11} {1} {2:10.2f} {3:14.2f} {4:14.2f} {5:11.2f} {6:>4}".format("22000","|",tempoMerge22000,tempoQuicksort22000,tempoSelection22000,tempoSort22000,"|"))
print("-----------------------------------------------------------------------")




