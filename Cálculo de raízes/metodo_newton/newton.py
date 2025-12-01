import pandas as pd
import numpy as np
import math

def metodo_newton_com_tabela(funcao, derivada, x0, tol=1e-5, max_iter=100):
    """
    Método de Newton com tabela de iterações.

    Args:
        funcao: A função a ser avaliada.
        derivada: A derivada da função.
        x0: Ponto inicial.
        tol: Tolerância para a convergência.
        max_iter: Número máximo de iterações.

    Returns:
        DataFrame com as iterações ou uma mensagem de erro.
    """
    iteracoes = []

    # Iterações do método de Newton, printando a tabela a cada interação
    for i in range(max_iter):
        fx0 = funcao(x0)
        dfx0 = derivada(x0)
        
        if dfx0 == 0:
            return "A derivada é zero. O método falhou."
        
        x1 = x0 - fx0 / dfx0
        iteracoes.append([i + 1, x0, fx0, dfx0, x1])

        if abs(x1 - x0) < tol:
            break
        
        x0 = x1
    else:
        return "Número máximo de iterações atingido."
    
    colunas = ['Iteração', 'x_n', 'f(x_n)', "f'(x_n)", 'x_(n+1)']
    tabela = pd.DataFrame(iteracoes, columns=colunas)
    print(tabela)
    return x1

p  = lambda x: x**5 - 6
dp = lambda x: 5*x**4
print(metodo_newton_com_tabela(p, dp, 1.5))