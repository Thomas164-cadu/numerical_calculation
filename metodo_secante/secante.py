import pandas as pd
import numpy as np
import math

# Função para o método da secante com tabela de iterações e print a cada iteração
def metodo_secante_com_tabela(funcao, x0, x1, tol=1e-5, max_iter=100):
    """
    Método da secante com tabela de iterações.

    Args:
        funcao: A função a ser avaliada.
        x0: Primeiro ponto inicial.
        x1: Segundo ponto inicial.
        tol: Tolerância para a convergência.
        max_iter: Número máximo de iterações.

    Returns:
        DataFrame com as iterações ou uma mensagem de erro.
    """
    iteracoes = []

    # Iterações do método da secante, printando a tabela a cada interação
    for i in range(max_iter):
        f_x0 = funcao(x0)
        f_x1 = funcao(x1)
        
        if f_x1 - f_x0 == 0:
            return "Divisão por zero. O método falhou."
        
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        iteracoes.append([i + 1, x0, x1, x2, f_x0, f_x1, funcao(x2)])

        if abs(x2 - x1) < tol:
            break
        
        x0, x1 = x1, x2
    else:
        return "Número máximo de iterações atingido."
    
    colunas = ['Iteração', 'x_n-1', 'x_n', 'x_n+1', 'f(x_n-1)', 'f(x_n)', 'f(x_n+1)']
    tabela = pd.DataFrame(iteracoes, columns=colunas)
    print(tabela)
    return x2

p  = lambda x: 0.5*x - math.tan(x)
print(metodo_secante_com_tabela(p, 0, 1))