variáveis públicas
 lista[]

procedimento estica

início
    listaAux[]
    comp <- comprimento(lista)
    item <- 1
    para i ← 1 até comp faça
        se (lista[i] mod 2 = 0) então
        
            listaAux[item] ← lista[i] / 2
         	item <- item + 1
            listaAux[item] ← lista[i] / 2
            item ← item + 1
                    
        senão 

         	listaAux[item] ← ((lista[i] + 1) / 2)
         	item <- item + 1
         	listaAux[item] ← ((lista[i] - 1) / 2)
         	item <- item + 1

        fimse

    proximo i

    listaAux = lista

fim


programa teste

início

 lista [18, 7, 4, 24, 11]
 estica
 imprima lista

fim