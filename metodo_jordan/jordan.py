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


def formatar_vetor(x):
    """Retorna uma string com o vetor x formatado linha a linha (5 casas)."""
    x = np.array(x, dtype=float)
    return "[" + ", ".join(f"{xi:8.5f}" for xi in x) + "]"


def eliminacao_jordan(A, b, pivoting=True, verbose=True):
    """
    Resolve o sistema Ax = b usando eliminação de Gauss-Jordan (redução por linhas até a forma reduzida por linhas)
    Opcionalmente usa pivoteamento parcial (troca de linhas pelo maior pivô na coluna atual).

    Entrada:
      A - matriz quadrada (lista de listas ou ndarray)
      b - vetor de termos constantes (lista ou ndarray)
      pivoting - se True usa pivoteamento parcial
      verbose - se True imprime as iterações em formato de tabela

    Retorna:
      x - vetor solução (ndarray) ou string com mensagem de erro
    """
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)

    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        return "A deve ser uma matriz quadrada."
    n = A.shape[0]
    if b.size != n:
        return "Dimensões de A e b incompatíveis."

    tol = np.finfo(float).eps

    if verbose:
        print("\n=== Início da Eliminação de Gauss-Jordan ===\n")

    for k in range(n):
        # Pivoteamento parcial
        if pivoting:
            max_row = np.argmax(np.abs(A[k:, k])) + k
            if abs(A[max_row, k]) < tol:
                return "Matriz singular ou quase singular. O método falhou."
            if max_row != k:
                A[[k, max_row]] = A[[max_row, k]]
                b[[k, max_row]] = b[[max_row, k]]
                if verbose:
                    print(f"[Pivoteamento] Trocando linha {k} com linha {max_row}")
        else:
            if abs(A[k, k]) < tol:
                return "Pivô zero encontrado. Considere ativar pivoteamento."

        # Normalizar linha k
        pivot = A[k, k]
        A[k, k:] = A[k, k:] / pivot
        b[k] = b[k] / pivot

        # Eliminar todas as outras linhas na coluna k
        for i in range(n):
            if i == k:
                continue
            factor = A[i, k]
            if factor != 0:
                A[i, k:] -= factor * A[k, k:]
                b[i] -= factor * b[k]

        if verbose:
            print(f"\n--- Passo (coluna) {k + 1} ---")
            print(formatar_matriz(A, b))

    # Agora A deve ser identidade e b a solução
    x = b.copy()

    if verbose:
        print("\n=== Fim da Eliminação de Gauss-Jordan ===\n")

    return x


# Exemplo de uso local
if __name__ == "__main__":
    A = [[3, 2, -1],
         [2, -2, 4],
         [-1, 0.5, -1]]

    b = [1, -2, 0]

    sol = eliminacao_jordan(A, b, pivoting=True, verbose=True)
    print("Solução:", formatar_vetor(sol))
