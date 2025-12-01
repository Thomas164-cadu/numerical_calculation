import pandas as pd
import numpy as np

# Função para o método da posição falsa com tabela de iterações e print a cada iteração
def posicao_falsa_com_tabela(funcao, a, b, tol=1e-5, max_iter=100):
    """
    Método da posição falsa com tabela de iterações.

    Args:
        funcao: A função a ser avaliada.
        a: Limite inferior do intervalo.
        b: Limite superior do intervalo.
        tol: Tolerância para a convergência.
        max_iter: Número máximo de iterações.

    Returns:
        DataFrame com as iterações ou uma mensagem de erro.
    """
    if funcao(a) * funcao(b) >= 0:
        return "O método da posição falsa falhou."

    iteracoes = []

    # Iterações do método da posição falsa, printando a tabela a cada interação
    for i in range(max_iter):
        fa = funcao(a)
        fb = funcao(b)
        c = (a * fb - b * fa) / (fb - fa)
        fc = funcao(c)
        iteracoes.append([i + 1, a, b, c, fa, fb, fc])

        if abs(fc) < tol:
            break

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    else:
        return "Número máximo de iterações atingido."
    
    colunas = ['Iteração', 'a', 'b', 'c', 'f(a)', 'f(b)', 'f(c)']
    tabela = pd.DataFrame(iteracoes, columns=colunas)
    print(tabela)
    return c

p  = lambda x: x**5 - (10/9)*x**3 + (5/21)*x
print(posicao_falsa_com_tabela(p, -0.25, 0.25))