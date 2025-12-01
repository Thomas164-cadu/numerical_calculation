import pandas as pd
import numpy as np

# Função para resolução de Problemas de Valor Inicial (PVI) por diferença finitas e imprimir os resultados
def resolver_pvi(f, y0, x0, xf, h):
    n = int((xf - x0) / h)
    x_values = np.linspace(x0, xf, n + 1)
    y_values = np.zeros(n + 1)
    y_values[0] = y0
    
    for i in range(1, n + 1):
        y_values[i] = y_values[i - 1] + h * f(x_values[i - 1], y_values[i - 1])
    
    # Criar DataFrame para exibir os resultados
    data = {
        'x': x_values,
        'y': y_values
    }
    df = pd.DataFrame(data)
    
    print("Tabela de Valores:")
    print(df)
    print(f"\nValor aproximado de y({xf}) pelo método de diferenças finitas: {y_values[-1]}")
    
    return y_values

# Exemplo de uso
if __name__ == "__main__":
    # Definir a função da equação diferencial dy/dx = f(x, y)
    def f(x, y):
        return x + y  # Exemplo: dy/dx = x + y

    y0 = 1    # Condição inicial y(x0)
    x0 = 0    # Ponto inicial
    xf = 1    # Ponto final
    h = 0.2   # Passo de integração
    
    resolver_pvi(f, y0, x0, xf, h)