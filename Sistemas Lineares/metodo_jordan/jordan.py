import pandas as pd
import numpy as np

# Função para realizar o calculo do método de Jordan e imprimir os resultados
def metodo_jordan(A, b):
    n = len(b)
    # Combinar A e b em uma matriz aumentada
    Ab = np.hstack([A, b.reshape(-1, 1)])
    
    # Eliminação de Jordan
    for i in range(n):
        # Tornar o elemento Ab[i][i] igual a 1
        Ab[i] = Ab[i] / Ab[i][i]
        for j in range(n):
            if j != i:
                Ab[j] = Ab[j] - Ab[i] * Ab[j][i]
    
    # A solução está na última coluna da matriz aumentada
    x = Ab[:, -1]
    
    # Criar DataFrame para exibir os resultados
    data = {
        'Matriz Aumentada': [Ab],
        'Solução x': [x]
    }
    df = pd.DataFrame(data)
    
    print("Matriz Aumentada após Eliminação de Jordan:")
    print(Ab)
    print(f"\nSolução do sistema linear: {x}")
    
    return x

# Exemplo de uso
if __name__ == "__main__":
    A = np.array([[2, 1, -1],
                  [-3, -1, 2],
                  [-2, 1, 2]], dtype=float)
    b = np.array([8, -11, -3], dtype=float)
    
    metodo_jordan(A, b)