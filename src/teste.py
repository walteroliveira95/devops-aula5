import jogovelha
import sys

erroInicializar = false
jogo = jogovelha.inicializar(0

if len(jogo) !=3:
    erroInicializar = true
else:
    for linha in jogo:
        if len(linha) !=3:
            erroInicializar = true
        else        
            for elemento in linha:
                if elemento != '.':
                    erroInicializar = true
if erroInicializar:
    sys.exit(1)
else:
    sys.exit(0)                        