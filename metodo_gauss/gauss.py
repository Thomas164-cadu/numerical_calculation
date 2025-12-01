import numpy as np

def formatar_matriz(A, b):
    """
    Formata a matriz aumentada em estilo visual de matriz com colunas alinhadas.
    Retorna uma string multilinha.
    """
    A = np.array(A)
    b = np.array(b)
    n = A.shape[0]

    linhas = []
    for i in range(n):
        linha_A = "  ".join(f"{A[i, j]:8.5f}" for j in range(A.shape[1]))
        linha_b = f"{b[i]:8.5f}"
        if i == 0:
            linhas.append(f"⎡ {linha_A} | {linha_b} ⎤")
        elif i == n - 1:
            linhas.append(f"⎣ {linha_A} | {linha_b} ⎦")
        else:
            linhas.append(f"│ {linha_A} | {linha_b} │")

    return "\n".join(linhas)


def eliminacao_gauss_com_tabela(A, b, pivoting=True):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)

    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        return "A deve ser uma matriz quadrada."
    n = A.shape[0]
    if b.size != n:
        return "Dimensões de A e b incompatíveis."

    tol = np.finfo(float).eps

    print("\n=== Início da Eliminação de Gauss ===\n")

    for k in range(n - 1):

        # pivoteamento parcial
        if pivoting:
            max_row = np.argmax(np.abs(A[k:, k])) + k
            if abs(A[max_row, k]) < tol:
                return "Matriz singular ou quase singular. O método falhou."
            if max_row != k:
                A[[k, max_row]] = A[[max_row, k]]
                b[[k, max_row]] = b[[max_row, k]]
                print(f"[Pivoteamento] Trocando linha {k} com linha {max_row}")

        else:
            if abs(A[k, k]) < tol:
                return "Pivô zero encontrado. Considere ativar pivoteamento."

        # Eliminação
        for i in range(k + 1, n):
            factor = A[i, k] / A[k, k]
            A[i, k:] -= factor * A[k, k:]
            b[i] -= factor * b[k]

        # Exibir iteração formatada
        print(f"\n--- Iteração {k + 1} ---")
        print(formatar_matriz(A, b))

    # Retro-substituição
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        if abs(A[i, i]) < tol:
            return "Matriz singular ou quase singular. O método falhou."
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

    print("\n=== Fim da Eliminação ===\n")

    return x


# Exemplo de uso
if __name__ == "__main__":
    A = [[3, 2, -1],
         [2, -2, 4],
         [-1, 0.5, -1]]

    b = [1, -2, 0]

    sol = eliminacao_gauss_com_tabela(A, b, pivoting=True)
    print("Solução:", sol)
