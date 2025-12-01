import pandas as pd
import numpy as np

# Função para ajuste de curvas pelo método de ajuste linear múltiplo e imprimir os resultados
def ajuste_linear_multiplo(X, y):
    def calcular_coeficientes(X, y):
        X_b = np.c_[np.ones((X.shape[0], 1)), X]  # Adiciona o termo de interceptação
        coeficientes = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y
        return coeficientes

    def calcular_valores_ajustados(X, coeficientes):
        X_b = np.c_[np.ones((X.shape[0], 1)), X]
        y_ajustado = X_b @ coeficientes
        return y_ajustado

    coeficientes = calcular_coeficientes(X, y)
    y_ajustado = calcular_valores_ajustados(X, coeficientes)
    
    # Criar DataFrame para exibir os resultados
    data = {
        'X': [X[i].tolist() for i in range(X.shape[0])],
        'Y Observado': y,
        'Y Ajustado': y_ajustado
    }
    df = pd.DataFrame(data)
    
    print("Tabela de Valores:")
    print(df)
    print(f"\nCoeficientes do modelo de ajuste linear múltiplo: {coeficientes}")
    
    return coeficientes, y_ajustado

# Exemplo de uso
if __name__ == "__main__":
    X = np.array([[1, 2],
                  [2, 3],
                  [3, 4],
                  [4, 5],
                  [5, 6]])
    y = np.array([5, 7, 9, 11, 13])
    
    ajuste_linear_multiplo(X, y)