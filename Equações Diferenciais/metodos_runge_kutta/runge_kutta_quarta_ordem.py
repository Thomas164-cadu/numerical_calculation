import pandas as pd
import numpy as np

# Função para calcular equações diferenciais usando o método de Runge-Kutta de quarta ordem e imprimir os resultados
def runge_kutta_quarta_ordem(f, y0, t0, tf, h):
    n = int((tf - t0) / h)
    t_values = np.linspace(t0, tf, n + 1)
    y_values = np.zeros(n + 1)
    y_values[0] = y0
    
    for i in range(1, n + 1):
        k1 = f(t_values[i - 1], y_values[i - 1])
        k2 = f(t_values[i - 1] + h / 2, y_values[i - 1] + (h / 2) * k1)
        k3 = f(t_values[i - 1] + h / 2, y_values[i - 1] + (h / 2) * k2)
        k4 = f(t_values[i - 1] + h, y_values[i - 1] + h * k3)
        y_values[i] = y_values[i - 1] + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    
    # Criar DataFrame para exibir os resultados
    data = {
        't': t_values,
        'y': y_values
    }
    df = pd.DataFrame(data)
    
    print("Tabela de Valores:")
    print(df)
    print(f"\nValor aproximado de y({tf}) pelo método de Runge-Kutta de quarta ordem: {y_values[-1]}")
    
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
    
    runge_kutta_quarta_ordem(f, y0, t0, tf, h)