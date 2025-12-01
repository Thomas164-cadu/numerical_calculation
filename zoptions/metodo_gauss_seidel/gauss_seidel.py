import numpy as np


def formatar_matriz(A, b):
    """
    Formata a matriz aumentada em estilo visual de matriz com colunas alinhadas.
    Mantém consistência com os outros módulos.
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


def metodo_gauss_seidel(A, b, x0=None, tol=1e-10, max_iter=100, verbose=True, omega=1.0):
    """
    Resolve o sistema Ax = b usando o método de Gauss-Seidel.
    Suporta relaxação SOR via parâmetro omega (omega=1.0 -> Gauss-Seidel padrão).

    Parâmetros:
      A - matriz quadrada (lista de listas ou ndarray)
      b - vetor de termos constantes (lista ou ndarray)
      x0 - chute inicial (lista ou ndarray). Se None, usa vetor zero.
      tol - tolerância para o critério de parada (norma infinita das diferenças)
      max_iter - número máximo de iterações
      verbose - se True imprime informações por iteração
      omega - parâmetro de relaxação (1.0 = sem relaxação)

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
        return "Zero na diagonal principal detectado. O método de Gauss-Seidel não pode prosseguir."

    if verbose:
        print("\n=== Início do Método de Gauss-Seidel ===\n")
        try:
            print(formatar_matriz(A, b))
        except Exception:
            pass
        print(f"Chute inicial: {formatar_vetor(x)}\n")
        if omega != 1.0:
            print(f"Usando relaxação SOR com omega = {omega}\n")

    for k in range(1, max_iter + 1):
        x_old = x.copy()

        for i in range(n):
            # Soma das entradas já atualizadas (0..i-1)
            sum1 = np.dot(A[i, :i], x[:i]) if i > 0 else 0.0
            # Soma das entradas ainda não atualizadas (i+1..n-1)
            sum2 = np.dot(A[i, i+1:], x_old[i+1:]) if i < n - 1 else 0.0

            xi_new = (b[i] - sum1 - sum2) / A[i, i]
            # relaxação SOR: x_i <- (1-omega)*x_old + omega * xi_new
            x[i] = (1 - omega) * x_old[i] + omega * xi_new

        diff = np.linalg.norm(x - x_old, ord=np.inf)
        resid = np.linalg.norm(np.dot(A, x) - b, ord=np.inf)

        if verbose:
            print(f"Iteração {k}: x = {formatar_vetor(x)} | ||dx||_inf = {diff:.3e} | ||Ax-b||_inf = {resid:.3e}")

        if diff < tol:
            if verbose:
                print("\nConvergência alcançada.")
                print("\n=== Fim do Método de Gauss-Seidel ===\n")
            return x

    if verbose:
        print("\nMáximo de iterações alcançado sem convergência.")
        print("\n=== Fim do Método de Gauss-Seidel ===\n")

    return x


# Exemplo de uso
if __name__ == "__main__":
    A = [[10.0, -1.0, 2.0, 0.0],
         [-1.0, 11.0, -1.0, 3.0],
         [2.0, -1.0, 10.0, -1.0],
         [0.0, 3.0, -1.0, 8.0]]

    b = [6.0, 25.0, -11.0, 15.0]

    sol = metodo_gauss_seidel(A, b, x0=None, tol=1e-8, max_iter=100, verbose=True, omega=1.0)
    print("Solução aproximada:", formatar_vetor(sol))
