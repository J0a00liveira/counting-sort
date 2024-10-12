# counting-sort [![languages](https://skillicons.dev/icons?i=python&perline=10)](https://skillicons.dev)

Counting Sort é um algoritmo de ordenação que não é baseado em comparações, sendo eficiente para certos tipos de entradas. Sua principal ideia é contar a frequência de cada elemento de um conjunto e, com base nessas contagens, posicionar os elementos corretamente no array ordenado. Ele é mais eficiente quando o intervalo de valores do conjunto de dados é relativamente pequeno.

## Biblioteca importada

importamos a biblioteca re para poder tratar com regex a entrada dos dados que solicitamos ao usuario

## Explicação do código: 

1 - Encontrar o maior valor: Isso é necessário para criar o array de contagem com o tamanho apropriado.

2 - Criar o array de contagem: Inicialmente, é um array de zeros, onde o índice representa o número do array de entrada e o valor na posição do índice representa a frequência desse número.

3 - Contar as ocorrências: Para cada número no array de entrada, incrementa-se a posição correspondente no array de contagem.

4 - Acumular as contagens: O array de contagem é ajustado para que cada valor represente o número de elementos menores ou iguais ao valor do índice.

5 - Montar o array final: Utilizando o array acumulado, percorremos o array original de trás para frente para preservar a estabilidade (quando elementos iguais mantêm sua ordem relativa).

