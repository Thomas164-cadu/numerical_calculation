import pandas as pd
import numpy as np

# Função para realizar a interpolação Diferenças divididas e imprimir os resultados

def interpolacao_newton(x_values, y_values, x_to_interpolate):
    def divided_differences(x, y):
        n = len(y)
        coef = np.zeros([n, n])
        coef[:,0] = y
        
        for j in range(1, n):
            for i in range(n - j):
                coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])
        
        return coef[0]

    def newton_interpolation(x, coef, x_point):
        n = len(coef)
        result = coef[0]
        term = 1.0
        
        for i in range(1, n):
            term *= (x_point - x[i - 1])
            result += coef[i] * term
        
        return result

    coef = divided_differences(x_values, y_values)
    interpolated_value = newton_interpolation(x_values, coef, x_to_interpolate)
    
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
    
    interpolacao_newton(x_values, y_values, x_to_interpolate)