import pandas as pd
import numpy as np

# Função para resolução de Problemas de Valor de Contorno (PVC) por diferenças finitas e imprimir os resultados
def resolver_pvc(f, a, b, alpha, beta, n):
    h = (b - a) / (n + 1)
    x_values = np.linspace(a, b, n + 2)
    A = np.zeros((n, n))
    d = np.zeros(n)
    
    # Montar o sistema linear Ax = d
    for i in range(1, n + 1):
        A[i - 1][i - 1] = -2 / h**2 + f(x_values[i])
        if i > 1:
            A[i - 1][i - 2] = 1 / h**2
        if i < n:
            A[i - 1][i] = 1 / h**2
        
        d[i - 1] = 0
        if i == 1:
            d[i - 1] -= alpha / h**2
        if i == n:
            d[i - 1] -= beta / h**2
    
    # Resolver o sistema linear
    y_values = np.linalg.solve(A, d)
    
    # Adicionar as condições de contorno
    y_values = np.concatenate(([alpha], y_values, [beta]))
    
    # Criar DataFrame para exibir os resultados
    data = {
        'x': x_values,
        'y': y_values
    }
    df = pd.DataFrame(data)
    
    print("Tabela de Valores:")
    print(df)
    print(f"\nValores aproximados de y(x) pelo método de diferenças finitas:")
    
    return y_values

# Exemplo de uso
if __name__ == "__main__":
    # Definir a função da equação diferencial d²y/dx² = f(x, y)
    def f(x):
        return -np.pi**2 * np.sin(np.pi * x)  # Exemplo: d²y/dx² = -π²sin(πx)

    a = 0      # Limite inferior
    b = 1      # Limite superior
    alpha = 0  # Condição de contorno y(a)
    beta = 0   # Condição de contorno y(b)
    n = 10     # Número de subintervalos
    
    resolver_pvc(f, a, b, alpha, beta, n)