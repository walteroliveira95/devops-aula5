# Arquitetura

* As funções relacionadas ao gerenciamento das casas do jogo da velha ficarão no modulo **jogovelha.py**.

* o estado de cada casa do jogo será representada por uma string: "." para casa vazia; "X" para casa ocupada pelo 1o jogador; "o" para casa ocupada pelo 2o jogador

* A função inicializar() retornará uma lista 3x3, onde cada posição conterá uma string para indicar o estado de uma casa do jogo. A função retornará todas as casas inicialmente vazias.