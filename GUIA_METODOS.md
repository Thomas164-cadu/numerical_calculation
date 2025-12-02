# Guia de Métodos Numéricos

Este guia explica brevemente cada método numérico implementado neste projeto e como modificar funções e vetores.

---

## Índice

1. [Cálculo de Raízes](#1-cálculo-de-raízes)
2. [Sistemas Lineares](#2-sistemas-lineares)
3. [Interpolação](#3-interpolação)
4. [Integração Numérica](#4-integração-numérica)
5. [Equações Diferenciais](#5-equações-diferenciais)
6. [Ajuste de Curvas](#6-ajuste-de-curvas)
7. [Como Modificar Funções](#como-modificar-funções)
8. [Como Modificar Vetores e Matrizes](#como-modificar-vetores-e-matrizes)

---

## 1. Cálculo de Raízes

### Método da Bisseção
**Arquivo:** `Cálculo de raízes/metodo_bissecao/bissecao.py`

Encontra raízes dividindo o intervalo ao meio iterativamente.

**Exemplo no código:**
```python
p = lambda x: x**5 - (10/9)*x**3 + (5/21)*x
print(bissecao_com_tabela(p, -0.75, -0.25))
```

**Para modificar:** Altere a função `p` na linha 47 e os valores do intervalo `[a, b]` na chamada do método.

### Método de Newton
**Arquivo:** `Cálculo de raízes/metodo_newton/newton.py`

Usa a derivada para convergência mais rápida.

**Exemplo no código:**
```python
p  = lambda x: x**5 - 6
dp = lambda x: 5*x**4
print(metodo_newton_com_tabela(p, dp, 1.5))
```

**Para modificar:** Altere a função `p` (linha 44) e sua derivada `dp` (linha 45), além do ponto inicial na chamada do método.

### Método da Secante
**Arquivo:** `Cálculo de raízes/metodo_secante/secante.py`

Similar ao Newton, mas não requer derivada.

**Exemplo no código:**
```python
import math
p = lambda x: 0.5*x - math.tan(x)
print(metodo_secante_com_tabela(p, 0, 1))
```

**Para modificar:** Altere a função `p` (linha 45) e os dois pontos iniciais na chamada do método. **Nota:** Use `math.tan`, `math.sin`, etc. para funções trigonométricas.

### Método da Posição Falsa
**Arquivo:** `Cálculo de raízes/metodo_posicao_falsa/posicao_falsa.py`

Usa interpolação linear para aproximar a raiz.

**Exemplo no código:**
```python
p = lambda x: x**5 - (10/9)*x**3 + (5/21)*x
print(posicao_falsa_com_tabela(p, -0.25, 0.25))
```

**Para modificar:** Altere a função `p` (linha 49) e os valores do intervalo `[a, b]` na chamada do método.

---

## 2. Sistemas Lineares

### Eliminação de Gauss
**Arquivo:** `Sistemas Lineares/metodo_gauss/gauss.py`

Resolve sistemas Ax = b por eliminação direta.

**Exemplo no código (linhas 36-41):**
```python
if __name__ == "__main__":
    A = np.array([[2, 1, -1],
                  [-3, -1, 2],
                  [-2, 1, 2]], dtype=float)
    b = np.array([8, -11, -3], dtype=float)

    metodo_gauss(A, b)
```

**Para modificar:** Altere os valores da matriz `A` e do vetor `b` dentro do bloco `if __name__ == "__main__":`.

### Eliminação de Jordan
**Arquivo:** `Sistemas Lineares/metodo_jordan/jordan.py`

Método de eliminação completa (acima e abaixo da diagonal).

```python
import numpy as np
from jordan import metodo_jordan

# Definir matriz A e vetor b
A = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]], dtype=float)
b = np.array([8, -11, -3], dtype=float)

# Executar método
solucao = metodo_jordan(A, b)
```

### Método de Jacobi
**Arquivo:** `Sistemas Lineares/metodo_jacobi/jacobi.py`

Método iterativo para sistemas grandes e esparsos.

**Exemplo no código (linhas 35-41):**
```python
if __name__ == "__main__":
    A = np.array([[4, -1, 0, 0],
                  [-1, 4, -1, 0],
                  [0, -1, 4, -1],
                  [0, 0, -1, 3]], dtype=float)
    b = np.array([15, 10, 10, 10], dtype=float)

    metodo_jacobi(A, b)
```

**Para modificar:** Altere os valores da matriz `A` e do vetor `b` dentro do bloco `if __name__ == "__main__":`.

### Método de Gauss-Seidel
**Arquivo:** `Sistemas Lineares/metodo_gauss_seidel/gauss_seidel.py`

Método iterativo mais rápido que Jacobi.

```python
import numpy as np
from gauss_seidel import metodo_gauss_seidel

# Definir matriz A e vetor b
A = np.array([[10, -1, 2],
              [-1, 11, -1],
              [2, -1, 10]], dtype=float)
b = np.array([6, 25, -11], dtype=float)

# Executar método
solucao = metodo_gauss_seidel(A, b, x0=None, tol=1e-10, max_iterations=100)
```

---

## 3. Interpolação

### Interpolação de Lagrange
**Arquivo:** `Interpolação/metodo_interpolacao_lagrange/interpolacao_lagrange.py`

Constrói polinômio interpolador usando base de Lagrange.

**Exemplo no código (linhas 33-37):**
```python
if __name__ == "__main__":
    x_values = [1, 2, 3, 4]
    y_values = [1, 4, 9, 16]
    x_to_interpolate = 2.5

    interpolacao_lagrange(x_values, y_values, x_to_interpolate)
```

**Para modificar:** Altere as listas `x_values`, `y_values` e o valor `x_to_interpolate` dentro do bloco `if __name__ == "__main__":`.

### Interpolação de Newton
**Arquivo:** `Interpolação/metodo_interpolacao_newton/interpolacao_newton.py`

Usa diferenças divididas de Newton.

**Exemplo no código (linhas 46-50):**
```python
if __name__ == "__main__":
    x_values = [1, 2, 3, 4]
    y_values = [1, 4, 9, 16]
    x_to_interpolate = 2.5

    interpolacao_newton(x_values, y_values, x_to_interpolate)
```

**Para modificar:** Altere as listas `x_values`, `y_values` e o valor `x_to_interpolate` dentro do bloco `if __name__ == "__main__":`.

### Interpolação Gregory-Newton
**Arquivo:** `Interpolação/metodo_interpolacao_gregory_newton/interpolacao_gregory_newton.py`

Usa diferenças progressivas (requer pontos igualmente espaçados).

```python
import numpy as np
from interpolacao_gregory_newton import interpolacao_gregory_newton

# Definir pontos igualmente espaçados
x = np.array([0, 1, 2, 3])
y = np.array([1, 2, 5, 10])

# Ponto a interpolar
x_novo = 1.5

# Executar método
valor = interpolacao_gregory_newton(x, y, x_novo)
```

---

## 4. Integração Numérica

### Método dos Trapézios
**Arquivo:** `Integração Numérica/metodo_trapezios/trapezios.py`

Aproxima integral usando trapézios.

**Exemplo no código (linhas 26-34):**
```python
if __name__ == "__main__":
    # Definir a função a ser integrada
    def f(x):
        return x**2  # Exemplo: f(x) = x^2

    a = 0  # Limite inferior
    b = 1  # Limite superior
    n = 4  # Número de subintervalos

    metodo_trapezios(f, a, b, n)
```

**Para modificar:** Altere a função `f(x)` e os valores de `a`, `b` e `n` dentro do bloco `if __name__ == "__main__":`.

### Método de Simpson
**Arquivo:** `Integração Numérica/metodo_simpson/simpson.py`

Aproxima integral usando parábolas (n deve ser par).

**Exemplo no código (linhas 32-40):**
```python
if __name__ == "__main__":
    # Definir a função a ser integrada
    def f(x):
        return x**2  # Exemplo: f(x) = x^2

    a = 0  # Limite inferior
    b = 1  # Limite superior
    n = 4  # Número de subintervalos (deve ser par)

    metodo_simpson(f, a, b, n)
```

**Para modificar:** Altere a função `f(x)` e os valores de `a`, `b` e `n` dentro do bloco `if __name__ == "__main__":`. **IMPORTANTE:** `n` deve ser par!

---

## 5. Equações Diferenciais

### Método de Euler
**Arquivo:** `Equações Diferenciais/metodo_euler/euler.py`

Resolve dy/dt = f(t, y) com condição inicial.

**Exemplo no código (linhas 28-37):**
```python
if __name__ == "__main__":
    # Definir a função da equação diferencial dy/dt = f(t, y)
    def f(t, y):
        return t + y  # Exemplo: dy/dt = t + y

    y0 = 1    # Condição inicial y(t0)
    t0 = 0    # Tempo inicial
    tf = 1    # Tempo final
    h = 0.2   # Passo de integração

    metodo_euler(f, y0, t0, tf, h)
```

**Para modificar:** Altere a função `f(t, y)` e os valores de `y0`, `t0`, `tf` e `h` dentro do bloco `if __name__ == "__main__":`.

### Runge-Kutta 2ª Ordem
**Arquivo:** `Equações Diferenciais/metodos_runge_kutta/runge_kutta_segunda_ordem.py`

Método mais preciso que Euler.

```python
from runge_kutta_segunda_ordem import runge_kutta_segunda_ordem

# Definir equação diferencial
f = lambda t, y: y - t**2

# Executar método
solucao = runge_kutta_segunda_ordem(f, y0=1, t0=0, tf=2, h=0.1)
```

### Runge-Kutta 4ª Ordem
**Arquivo:** `Equações Diferenciais/metodos_runge_kutta/runge_kutta_quarta_ordem.py`

Método de alta precisão, mais usado na prática.

**Exemplo no código (linhas 32-41):**
```python
if __name__ == "__main__":
    # Definir a função da equação diferencial dy/dt = f(t, y)
    def f(t, y):
        return t + y  # Exemplo: dy/dt = t + y

    y0 = 1    # Condição inicial y(t0)
    t0 = 0    # Tempo inicial
    tf = 1    # Tempo final
    h = 0.2   # Passo de integração

    runge_kutta_quarta_ordem(f, y0, t0, tf, h)
```

**Para modificar:** Altere a função `f(t, y)` e os valores de `y0`, `t0`, `tf` e `h` dentro do bloco `if __name__ == "__main__":`.

### Problema de Valor Inicial (PVI)
**Arquivo:** `Equações Diferenciais/PVI e PVC/pvi.py`

Resolve dy/dx = f(x, y) com y(x0) conhecido.

```python
from pvi import resolver_pvi

# Definir equação diferencial
f = lambda x, y: x + y

# Executar método
solucao = resolver_pvi(f, y0=1, x0=0, xf=2, h=0.1)
```

### Problema de Valor de Contorno (PVC)
**Arquivo:** `Equações Diferenciais/PVI e PVC/pvc.py`

Resolve d²y/dx² = f(x) com y(a) e y(b) conhecidos.

```python
from pvc import resolver_pvc

# Definir segunda derivada
f = lambda x: -x

# Condições de contorno: y(0) = 0, y(1) = 0
solucao = resolver_pvc(f, a=0, b=1, alpha=0, beta=0, n=10)
```

---

## 6. Ajuste de Curvas

### Ajuste Linear Múltiplo
**Arquivo:** `Ajuste de Curvas/metodo_ajuste_linear/ajuste_linear.py`

Ajusta modelo linear com múltiplas variáveis.

**Exemplo no código (linhas 34-41):**
```python
if __name__ == "__main__":
    X = np.array([[1, 2],
                  [2, 3],
                  [3, 4],
                  [4, 5],
                  [5, 6]])
    y = np.array([5, 7, 9, 11, 13])

    ajuste_linear_multiplo(X, y)
```

**Para modificar:** Altere a matriz `X` (cada linha é uma observação) e o vetor `y` dentro do bloco `if __name__ == "__main__":`.

### Ajuste Polinomial
**Arquivo:** `Ajuste de Curvas/metodo_polinomial/polinomial.py`

Ajusta polinômio de grau n aos dados.

**Exemplo no código (linhas 35-39):**
```python
if __name__ == "__main__":
    x_values = np.array([1, 2, 3, 4, 5])
    y_values = np.array([2.2, 2.8, 3.6, 4.5, 5.1])
    grau = 2  # Grau do polinômio para ajuste

    ajuste_polinomial(x_values, y_values, grau)
```

**Para modificar:** Altere os arrays `x_values`, `y_values` e o valor de `grau` dentro do bloco `if __name__ == "__main__":`.

### Método dos Mínimos Quadrados
**Arquivo:** `Ajuste de Curvas/metodo_minimos_quadrados/minimos_quadrados.py`

Minimiza erro quadrático (similar ao ajuste polinomial).

```python
import numpy as np
from minimos_quadrados import minimos_quadrados

# Definir dados
x = np.array([0, 1, 2, 3, 4])
y = np.array([1, 2, 5, 10, 17])

# Ajustar polinômio de grau 2
coeficientes, valores_ajustados = minimos_quadrados(x, y, grau=2)
```

---

## Como Modificar Funções

### Para métodos de cálculo de raízes:

**Padrão:** Use `p = lambda x: ...` (variável `p`)

```python
# Exemplos reais do projeto:

# Polinômio (bissecao.py, posicao_falsa.py)
p = lambda x: x**5 - (10/9)*x**3 + (5/21)*x

# Polinômio simples (newton.py)
p = lambda x: x**5 - 6

# Função trigonométrica (secante.py)
import math
p = lambda x: 0.5*x - math.tan(x)

# Outros exemplos que você pode usar:
p = lambda x: x**3 - 2*x - 5
p = lambda x: math.exp(x) - 3*x
p = lambda x: math.cos(x) - x
```

**Para o Método de Newton:** Também defina a derivada `dp`:
```python
p  = lambda x: x**5 - 6
dp = lambda x: 5*x**4  # derivada de p
```

### Para métodos de integração e EDO:

**Padrão:** Use `def f(x):` ou `def f(t, y):` dentro do bloco `if __name__ == "__main__":`

```python
# Para integração (trapezios.py, simpson.py)
def f(x):
    return x**2

# Outros exemplos:
def f(x):
    return np.sin(x)

def f(x):
    return np.exp(-x**2)

# Para equações diferenciais (euler.py, runge_kutta.py)
def f(t, y):
    return t + y  # dy/dt = t + y

# Outros exemplos:
def f(t, y):
    return -0.5*y  # decaimento exponencial

def f(t, y):
    return y - t**2

def f(t, y):
    return t*y - y**2
```

### Dica importante sobre funções matemáticas:

**Para cálculo de raízes (lambda functions):** Use `math.sin`, `math.cos`, `math.exp`, etc.
```python
import math
p = lambda x: math.sin(x) - 0.5
p = lambda x: math.exp(x) - 2*x
```

**Para integração e EDO (numpy arrays):** Use `np.sin`, `np.cos`, `np.exp`, etc.
```python
import numpy as np
def f(x):
    return np.sin(x) + np.exp(x)
```

---

## Como Modificar Vetores e Matrizes

### Vetores (arrays 1D):

```python
import numpy as np

# Criação direta
v = np.array([1, 2, 3, 4, 5])

# Vetor de zeros
v = np.zeros(5)

# Vetor de uns
v = np.ones(5)

# Vetor com valores espaçados
v = np.linspace(0, 10, 11)  # 0, 1, 2, ..., 10

# Vetor com passo definido
v = np.arange(0, 10, 0.5)  # 0, 0.5, 1, 1.5, ..., 9.5
```

### Matrizes (arrays 2D):

```python
import numpy as np

# Matriz 3x3 direta
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]], dtype=float)

# Matriz identidade 3x3
A = np.eye(3)

# Matriz de zeros 3x3
A = np.zeros((3, 3))

# Matriz de uns 3x3
A = np.ones((3, 3))

# Matriz diagonal
A = np.diag([1, 2, 3])  # diagonal com valores 1, 2, 3
```

### Modificar valores específicos:

```python
# Modificar elemento de vetor
v[0] = 10  # primeiro elemento

# Modificar elemento de matriz
A[0, 0] = 10  # linha 0, coluna 0
A[1, 2] = 5   # linha 1, coluna 2

# Modificar linha inteira
A[0, :] = [1, 2, 3]

# Modificar coluna inteira
A[:, 0] = [1, 4, 7]
```

### Pontos para interpolação:

```python
import numpy as np

# Pontos (x, y) para interpolação
x = np.array([0, 1, 2, 3, 4])
y = np.array([1, 3, 2, 5, 4])

# Pontos igualmente espaçados (para Gregory-Newton)
x = np.linspace(0, 4, 5)  # 0, 1, 2, 3, 4
y = np.array([1, 3, 2, 5, 4])
```

### Dados para ajuste de curvas:

```python
import numpy as np

# Dados x, y
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([1.2, 2.8, 4.1, 6.9, 8.3, 10.1])

# Matriz de features (para ajuste linear múltiplo)
# Cada linha é uma observação, cada coluna é uma variável
X = np.array([[1, 2, 3],    # obs 1: x1=1, x2=2, x3=3
              [2, 3, 4],    # obs 2: x1=2, x2=3, x3=4
              [3, 4, 5],    # obs 3: x1=3, x2=4, x3=5
              [4, 5, 6]])   # obs 4: x1=4, x2=5, x3=6
y = np.array([10, 15, 20, 25])
```

---

## Dicas Gerais

1. **Sempre importe NumPy**: `import numpy as np`
2. **Use dtype=float**: Para matrizes de sistemas lineares, use `dtype=float` para evitar erros de divisão inteira
3. **Funções lambda**: Ideais para funções simples de uma linha
4. **Tolerância e iterações**: Ajuste `tol` (tolerância) e `max_iter` (máximo de iterações) conforme necessário
5. **Passo h**: Para métodos numéricos de EDOs e integração, valores menores de `h` dão maior precisão
6. **Grau do polinômio**: Para ajuste polinomial, use grau menor que o número de pontos

---

## Exemplos de Execução

Para executar qualquer método, navegue até o diretório do arquivo e execute:

```bash
python nome_do_arquivo.py
```

Ou modifique a seção `if __name__ == "__main__":` no final de cada arquivo com seus próprios dados.

---

**Observação**: Todos os métodos imprimem tabelas formatadas com os resultados. Use o valor retornado pela função para processamento adicional em Python.