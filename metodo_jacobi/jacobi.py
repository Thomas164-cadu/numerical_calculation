import numpy as np


def formatar_matriz(A, b):
    """
    Formata a matriz aumentada em estilo visual de matriz com colunas alinhadas.
    Usado para consistência com os outros módulos.
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
    """Retorna uma string com o vetor x formatado linha a linha."""
    x = np.array(x)
    return "[" + ", ".join(f"{xi:8.5f}" for xi in x) + "]"


def metodo_jacobi(A, b, x0=None, tol=1e-10, max_iter=100, verbose=True):
    """
    Resolve o sistema Ax = b usando o método iterativo de Jacobi.

    Parâmetros:
      A - matriz quadrada (lista de listas ou ndarray)
      b - vetor de termos constantes (lista ou ndarray)
      x0 - chute inicial (lista ou ndarray). Se None, usa vetor zero.
      tol - tolerância para o critério de parada (norma infinita das diferenças)
      max_iter - número máximo de iterações
      verbose - se True imprime informações por iteração

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

    if x0 is None:
        x = np.zeros(n)
    else:
        x = np.array(x0, dtype=float)
        if x.size != n:
            return "Chute inicial x0 tem dimensão incorreta."

    # Verificar se há zeros na diagonal
    if np.any(np.isclose(np.diag(A), 0.0)):
        return "Zero na diagonal principal detectado. O método de Jacobi não pode prosseguir."

    if verbose:
        print("\n=== Início do Método de Jacobi ===\n")
        # Mostrar matriz aumentada apenas como informação
        try:
            print(formatar_matriz(A, b))
        except Exception:
            pass
        print(f"Chute inicial: {formatar_vetor(x)}\n")

    D = np.diag(A)
    R = A - np.diagflat(D)

    for k in range(1, max_iter + 1):
        x_new = (b - np.dot(R, x)) / D

        diff = np.linalg.norm(x_new - x, ord=np.inf)
        resid = np.linalg.norm(np.dot(A, x_new) - b, ord=np.inf)

        if verbose:
            print(f"Iteração {k}: x = {formatar_vetor(x_new)} | ||dx||_inf = {diff:.3e} | ||Ax-b||_inf = {resid:.3e}")

        if diff < tol:
            if verbose:
                print("\nConvergência alcançada.")
                print("\n=== Fim do Método de Jacobi ===\n")
            return x_new

        x = x_new

    if verbose:
        print("\nMáximo de iterações alcançado sem convergência.")
        print("\n=== Fim do Método de Jacobi ===\n")

    return x


# Exemplo de uso
if __name__ == "__main__":
    A = [[10.0, -1.0, 2.0, 0.0],
         [-1.0, 11.0, -1.0, 3.0],
         [2.0, -1.0, 10.0, -1.0],
         [0.0, 3.0, -1.0, 8.0]]

    b = [6.0, 25.0, -11.0, 15.0]

    sol = metodo_jacobi(A, b, x0=None, tol=1e-8, max_iter=100, verbose=True)
    print("Solução aproximada:", sol)

