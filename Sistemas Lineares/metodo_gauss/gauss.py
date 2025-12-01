import pandas as pd
import numpy as np

# Função para realizar a resolução de sistemas lineares pelo método de Gauss e imprimir os resultados
def metodo_gauss(A, b):
    n = len(b)
    # Combinar A e b em uma matriz aumentada
    Ab = np.hstack([A, b.reshape(-1, 1)])
    
    # Eliminação de Gauss
    for i in range(n):
        # Tornar o elemento Ab[i][i] igual a 1
        Ab[i] = Ab[i] / Ab[i][i]
        for j in range(i + 1, n):
            Ab[j] = Ab[j] - Ab[i] * Ab[j][i]
    
    # Substituição regressiva
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = Ab[i][-1] - np.sum(Ab[i][i + 1:n] * x[i + 1:n])
    
    # Criar DataFrame para exibir os resultados
    data = {
        'Matriz Aumentada': [Ab],
        'Solução x': [x]
    }
    df = pd.DataFrame(data)
    
    print("Matriz Aumentada após Eliminação de Gauss:")
    print(Ab)
    print(f"\nSolução do sistema linear: {x}")
    
    return x

# Exemplo de uso
if __name__ == "__main__":
    A = np.array([[2, 1, -1],
                  [-3, -1, 2],
                  [-2, 1, 2]], dtype=float)
    b = np.array([8, -11, -3], dtype=float)
    
    metodo_gauss(A, b)