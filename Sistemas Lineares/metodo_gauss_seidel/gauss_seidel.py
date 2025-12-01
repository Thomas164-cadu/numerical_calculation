import pandas as pd
import numpy as np

# Função para calcular o método de Gauss-Seidel e imprimir os resultados
def metodo_gauss_seidel(A, b, x0=None, tol=1e-10, max_iterations=100):
    n = len(b)
    x = np.zeros(n) if x0 is None else x0.copy()
    
    for iteration in range(max_iterations):
        x_old = x.copy()
        for i in range(n):
            s1 = sum(A[i][j] * x[j] for j in range(i))
            s2 = sum(A[i][j] * x_old[j] for j in range(i + 1, n))
            x[i] = (b[i] - s1 - s2) / A[i][i]
        
        # Verificar convergência
        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            break
    
    # Criar DataFrame para exibir os resultados
    data = {
        'Iteração': list(range(iteration + 1)),
        'Valores de x': [x.tolist() for _ in range(iteration + 1)]
    }
    df = pd.DataFrame(data)
    
    print("Tabela de Iterações:")
    print(df)
    print(f"\nSolução do sistema linear após {iteration + 1} iterações: {x}")
    
    return x

# Exemplo de uso
if __name__ == "__main__":
    A = np.array([[4, -1, 0, 0],
                  [-1, 4, -1, 0],
                  [0, -1, 4, -1],
                  [0, 0, -1, 3]], dtype=float)
    b = np.array([15, 10, 10, 10], dtype=float)
    
    metodo_gauss_seidel(A, b)