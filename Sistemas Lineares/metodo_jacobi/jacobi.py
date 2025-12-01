import pandas as pd
import numpy as np

# Função para calcular sistemas lineares usando o método de Jacobi e imprimir os resultados
def metodo_jacobi(A, b, x0=None, tol=1e-10, max_iterations=100):
    n = len(b)
    x = np.zeros(n) if x0 is None else x0.copy()
    x_new = np.zeros(n)
    
    for iteration in range(max_iterations):
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]
        
        # Verificar convergência
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            break
        
        x = x_new.copy()
    
    # Criar DataFrame para exibir os resultados
    data = {
        'Iteração': list(range(iteration + 1)),
        'Valores de x': [x_new.tolist() for _ in range(iteration + 1)]
    }
    df = pd.DataFrame(data)
    
    print("Tabela de Iterações:")
    print(df)
    print(f"\nSolução do sistema linear após {iteration + 1} iterações: {x_new}")
    
    return x_new

# Exemplo de uso
if __name__ == "__main__":
    A = np.array([[4, -1, 0, 0],
                  [-1, 4, -1, 0],
                  [0, -1, 4, -1],
                  [0, 0, -1, 3]], dtype=float)
    b = np.array([15, 10, 10, 10], dtype=float)
    
    metodo_jacobi(A, b)