import pandas as pd
import numpy as np

#Função para realizar o ajuste de curvas pelo método dos mínimos quadrados e imprimir os resultados
def minimos_quadrados(x_values, y_values, grau):
    def ajustar_curva(x, y, grau):
        n = len(x)
        A = np.vander(x, grau + 1)
        coeficientes, _, _, _ = np.linalg.lstsq(A, y, rcond=None)
        return coeficientes

    def calcular_valores_ajustados(x, coeficientes):
        A = np.vander(x, len(coeficientes))
        y_ajustado = A @ coeficientes
        return y_ajustado

    coeficientes = ajustar_curva(x_values, y_values, grau)
    y_ajustado = calcular_valores_ajustados(x_values, coeficientes)
    
    # Criar DataFrame para exibir os resultados
    data = {
        'X': x_values,
        'Y Observado': y_values,
        'Y Ajustado': y_ajustado
    }
    df = pd.DataFrame(data)
    
    print("Tabela de Valores:")
    print(df)
    print(f"\nCoeficientes do polinômio ajustado de grau {grau}: {coeficientes}")
    
    return coeficientes, y_ajustado

# Exemplo de uso
if __name__ == "__main__":
    x_values = np.array([1, 2, 3, 4, 5])
    y_values = np.array([2.2, 2.8, 3.6, 4.5, 5.1])
    grau = 1  # Grau do polinômio para ajuste (linear)
    
    minimos_quadrados(x_values, y_values, grau)