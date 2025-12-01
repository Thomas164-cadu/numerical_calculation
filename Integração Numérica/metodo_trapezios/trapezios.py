import pandas as pd
import numpy as np

#Função para integração numérica pelo método dos trapézios e imprimir os resultados
def metodo_trapezios(f, a, b, n):
    h = (b - a) / n
    x_values = np.linspace(a, b, n + 1)
    y_values = f(x_values)
    
    integral = (h / 2) * (y_values[0] + 2 * np.sum(y_values[1:n]) + y_values[n])
    
    # Criar DataFrame para exibir os resultados
    data = {
        'x': x_values,
        'f(x)': y_values
    }
    df = pd.DataFrame(data)
    
    print("Tabela de Valores:")
    print(df)
    print(f"\nValor da integral aproximada pelo método dos trapézios: {integral}")
    
    return integral

# Exemplo de uso
if __name__ == "__main__":
    # Definir a função a ser integrada
    def f(x):
        return x**2  # Exemplo: f(x) = x^2

    a = 0  # Limite inferior
    b = 1  # Limite superior
    n = 4  # Número de subintervalos
    
    metodo_trapezios(f, a, b, n)