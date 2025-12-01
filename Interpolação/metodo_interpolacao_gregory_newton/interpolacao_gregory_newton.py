import pandas as pd
import numpy as np

# Função para realizar a interpolação de Diferenças finitas (Gregory-Newton) e imprimir os resultados
def interpolacao_gregory_newton(x_values, y_values, x_to_interpolate):
    def forward_differences(y):
        n = len(y)
        diff_table = np.zeros((n, n))
        diff_table[:, 0] = y
        
        for j in range(1, n):
            for i in range(n - j):
                diff_table[i][j] = diff_table[i + 1][j - 1] - diff_table[i][j - 1]
        
        return diff_table

    def gregory_newton_interpolation(x, y, x_point):
        n = len(y)
        h = x[1] - x[0]
        diff_table = forward_differences(y)
        
        u = (x_point - x[0]) / h
        result = y[0]
        u_term = 1.0
        
        for i in range(1, n):
            u_term *= (u - (i - 1)) / i
            result += u_term * diff_table[0][i]
        
        return result

    interpolated_value = gregory_newton_interpolation(x_values, y_values, x_to_interpolate)
    
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
    
    interpolacao_gregory_newton(x_values, y_values, x_to_interpolate)