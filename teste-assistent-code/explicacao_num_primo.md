# Explicação do código de verificação de número primo

Este arquivo descreve o funcionamento da função `eh_primo` presente em `num_primo.py`.

## Objetivo

A função `eh_primo(n: int) -> bool` verifica se um número inteiro `n` é um número primo.

## Como o código funciona

1. Importação de biblioteca:

```python
import math
```

A biblioteca `math` é usada para calcular a raiz quadrada inteira de `n` com `math.isqrt(n)`.

2. Definição da função:

```python
def eh_primo(n: int) -> bool:
```

A função recebe um número inteiro `n` e retorna `True` se ele for primo ou `False` caso contrário.

3. Tratamento de casos pequenos e não primos:

```python
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
```

- Números menores ou iguais a 1 não são primos.
- Os números 2 e 3 são primos, então retornamos `True` para `n <= 3`.
- Se `n` for par e maior que 2, não é primo.

4. Verificação de divisores ímpares:

```python
    limite = int(math.isqrt(n))
    for i in range(3, limite + 1, 2):
        if n % i == 0:
            return False
```

- `limite` é a raiz quadrada inteira de `n`.
- O loop verifica apenas números ímpares de 3 até `limite`, porque todos os fatores pares já foram descartados.
- Se `n` for divisível por algum desses valores, ele não é primo.

5. Retorno final:

```python
    return True
```

Se nenhum divisor for encontrado, então `n` é primo.

## Exemplo de uso

O bloco abaixo permite executar o arquivo diretamente e ver resultados de teste:

```python
if __name__ == "__main__":
    for numero in [1, 2, 3, 4, 16, 17, 19, 20]:
        print(f"{numero}: {eh_primo(numero)}")
```

Ele imprime se cada número da lista é primo ou não.

## Conclusão

A função `eh_primo` é eficiente porque evita testar todos os números até `n` e usa somente candidatos ímpares até a raiz quadrada de `n`.