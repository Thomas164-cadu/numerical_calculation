import pandas as pd
import numpy as np

# Função para integração numérica pelo método de Simpson e imprimir os resultados
def metodo_simpson(f, a, b, n):
    if n % 2 == 1:
        raise ValueError("n deve ser um número par para o método de Simpson.")
    
    h = (b - a) / n
    x_values = np.linspace(a, b, n + 1)
    y_values = f(x_values)
    
    integral = y_values[0] + y_values[-1]
    integral += 4 * np.sum(y_values[1:n:2])  # Soma dos termos ímpares
    integral += 2 * np.sum(y_values[2:n-1:2])  # Soma dos termos pares
    integral *= h / 3
    
    # Criar DataFrame para exibir os resultados
    data = {
        'x': x_values,
        'f(x)': y_values
    }
    df = pd.DataFrame(data)
    
    print("Tabela de Valores:")
    print(df)
    print(f"\nValor da integral aproximada pelo método de Simpson: {integral}")
    
    return integral

# Exemplo de uso
if __name__ == "__main__":
    # Definir a função a ser integrada
    def f(x):
        return x**2  # Exemplo: f(x) = x^2

    a = 0  # Limite inferior
    b = 1  # Limite superior
    n = 4  # Número de subintervalos (deve ser par)
    
    metodo_simpson(f, a, b, n)