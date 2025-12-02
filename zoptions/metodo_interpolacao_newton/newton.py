import pandas as pd
import numpy as np

# Função para realizar a interpolação de Newton (diferenças divididas)
def interpolacao_newton(x_values, y_values, x_to_interpolate):
    """
    Interpolação de Newton via diferenças divididas.

    Parâmetros:
      x_values - lista/array de abscissas (tamanho n)
      y_values - lista/array de ordenadas (tamanho n)
      x_to_interpolate - ponto onde avaliar o polinômio

    Retorna:
      interpolated_value - valor interpolado em x_to_interpolate (float)
    """
    x = np.array(x_values, dtype=float)
    y = np.array(y_values, dtype=float)

    n = len(x)
    if len(y) != n:
        raise ValueError("x_values e y_values devem ter o mesmo tamanho.")
    if n == 0:
        raise ValueError("Entradas vazias não são permitidas.")

    # Verificar se existem abscissas repetidas (divisão por zero)
    if len(np.unique(x)) != n:
        raise ValueError("Valores de x duplicados detectados — diferenças divididas indefinidas.")

    # Construir tabela de diferenças divididas (matriz upper-triangular)
    dd = np.full((n, n), np.nan, dtype=float)
    dd[:, 0] = y

    for j in range(1, n):
        for i in range(0, n - j):
            denom = x[i + j] - x[i]
            dd[i, j] = (dd[i + 1, j - 1] - dd[i, j - 1]) / denom

    # Coeficientes de Newton são a primeira linha dd[0, :]
    coef = dd[0, :].copy()

    # Avaliar o polinômio de Newton em x_to_interpolate usando uma versão de Horner
    value = coef[n - 1]
    for k in range(n - 2, -1, -1):
        value = value * (x_to_interpolate - x[k]) + coef[k]

    # Preparar DataFrame para exibição (colunas: f, 1ª dif, 2ª dif, ...)
    columns = [f"f[{i}]" if i == 0 else f"{i}ª diff" for i in range(n)]
    table = {}
    for j in range(n):
        col = []
        for i in range(n):
            if i <= n - j - 1:
                col.append(dd[i, j])
            else:
                col.append(np.nan)
        table[columns[j]] = col

    df = pd.DataFrame(table)
    # Incluir coluna X e Y originais (ajustando o comprimento)
    df.insert(0, "X", list(x) + [np.nan] * (n - len(x)))
    df.insert(1, "Y", list(y) + [np.nan] * (n - len(y)))

    print("Tabela de Diferenças Divididas:")
    print(df)
    print(f"\nValor interpolado em x = {x_to_interpolate}: {value}")

    return value


# Exemplo de uso
if __name__ == "__main__":
    # Mesmo exemplo do módulo de Lagrange para comparação
    x_values = [1, 2, 3, 4]
    y_values = [1, 4, 9, 16]
    x_to_interpolate = 2.5

    interpolated = interpolacao_newton(x_values, y_values, x_to_interpolate)
    print("Resultado (retornado):", interpolated)

