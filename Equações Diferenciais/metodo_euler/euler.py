import pandas as pd
import numpy as np

#Função para calcular equações diferenciais usando o método de Euler e imprimir os resultados
def metodo_euler(f, y0, t0, tf, h):
    n = int((tf - t0) / h)
    t_values = np.linspace(t0, tf, n + 1)
    y_values = np.zeros(n + 1)
    y_values[0] = y0
    
    for i in range(1, n + 1):
        y_values[i] = y_values[i - 1] + h * f(t_values[i - 1], y_values[i - 1])
    
    # Criar DataFrame para exibir os resultados
    data = {
        't': t_values,
        'y': y_values
    }
    df = pd.DataFrame(data)
    
    print("Tabela de Valores:")
    print(df)
    print(f"\nValor aproximado de y({tf}) pelo método de Euler: {y_values[-1]}")
    
    return y_values

# Exemplo de uso
if __name__ == "__main__":
    # Definir a função da equação diferencial dy/dt = f(t, y)
    def f(t, y):
        return t + y  # Exemplo: dy/dt = t + y

    y0 = 1    # Condição inicial y(t0)
    t0 = 0    # Tempo inicial
    tf = 1    # Tempo final
    h = 0.2   # Passo de integração
    
    metodo_euler(f, y0, t0, tf, h)