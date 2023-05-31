# Programa de manipulação de grafos
Este programa permite realizar várias operações em grafos, como impressão em pré-ordem, pós-ordem e em ordem, remoção de vértices, fusão de vértices, contração de vértices e arestas, ordenação topológica (algoritmo de Kahn) e cálculo do caminho mínimo (algoritmo de Dijkstra).

## Como usar
Para usar o programa, execute o arquivo main.py. Isso iniciará o programa e exibirá um menu com as opções disponíveis.

Para escolher uma opção, digite o número correspondente e pressione Enter. Em seguida, siga as instruções na tela para fornecer as informações necessárias para realizar a operação escolhida.

Por exemplo, se você escolher a opção “1. Impressão em Pré-Ordem”, o programa solicitará que você informe o caminho do arquivo que contém o grafo e o nó raiz a partir do qual a impressão em pré-ordem deve ser realizada. Depois de fornecer essas informações, o programa calculará e exibirá a impressão em pré-ordem do grafo.

Para sair do programa, escolha a opção “11. Sair do programa”.

## Formato do arquivo de grafo
O programa lê grafos a partir de arquivos de texto no seguinte formato:

### Árvore

```
50:40,60;
40:30,45,50;
60:55,70,50;
30:40;
45:40;
55:60;
70:60;
```
### GD sem peso

```
A:B,C,D;
B:C,D;
C:A;
D:C,S;
S:A,B;
```
### GD com peso

```
A:B=8,C=5,D=-4;
B:C=-3,D=9;
C:A=-2;
D:C=7,S=2;
S:A=6,B=7;
```
### GND sem peso

```
A:B,C,D,S;
B:A,C,D,S;
C:A,B,D;
D:A,B,C,S;
S:A,B,D;
```
### GND com peso

```
A:B=2,C=4,D=7,S=1;
B:A=2,C=1,D=3,S;
C:A=4,B=1,D=2;
D:A=7,B=3,C=2,S=5;
S:A=1,B=3,D=5;
```


Copiar
Cada linha representa um vértice e suas arestas. O vértice é especificado antes do caractere :, e suas arestas são especificadas depois do caractere : como uma lista separada por vírgulas. Cada linha termina com um caractere ;.

# O que foi pedido:
## Realizar a implementação de um algoritmo que efetue as seguintes ações:
1. Impressão em Pré-Ordem
2. Impressão Pós-Ordem;
3. Impressão EmOrdem;
4. Realize e remoção de um vértice de uma árvore;
5. Realize a Fusão de dois vértices;
6. Realize a Contração de um vértice;
7. Realize a Contração de uma aresta;
8. Realize a Ordenação Topológica (algoritmo de Kahn);
9. Caminho Mínimo - Dijkstra;
10. Caminho Mínimo - Bellman-Ford;

O trabalho deverá ser implementado em qualquer linguagem de programação e a entrada será 
via arquivo .txt; 