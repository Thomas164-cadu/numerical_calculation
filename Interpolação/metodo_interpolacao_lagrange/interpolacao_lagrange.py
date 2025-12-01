import pandas as pd
import numpy as np

# Função para realizar a interpolação de Lagrange e imprimir os resultados
def interpolacao_lagrange(x_values, y_values, x_to_interpolate):
    def lagrange_interpolation(x, y, x_point):
        total_sum = 0
        n = len(x)
        for i in range(n):
            term = y[i]
            for j in range(n):
                if j != i:
                    term *= (x_point - x[j]) / (x[i] - x[j])
            total_sum += term
        return total_sum

    interpolated_value = lagrange_interpolation(x_values, y_values, x_to_interpolate)
    
    # Criar DataFrame para exibir os resultados
    data = {
        'X': x_values,
        'Y': y_values
    }
    df = pd.DataFrame(data)
    
    print("Tabela de Valores:")
    print(df)
    print(f"\nValor interpolado em x = {x_to_interpolate}: {interpolated_value}")
    
    return interpolated_value

# Exemplo de uso
if __name__ == "__main__":
    x_values = [1, 2, 3, 4]
    y_values = [1, 4, 9, 16]
    x_to_interpolate = 2.5
    
    interpolacao_lagrange(x_values, y_values, x_to_interpolate)