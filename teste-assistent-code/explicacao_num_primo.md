# Explicação do Código de Verificação de Número Primo

Este arquivo descreve o funcionamento da função `is_prime` presente em `num_primos.py`.

## Objetivo

A função `is_prime(number: int) -> bool` verifica se um número inteiro `number` é um número primo.

## Como o Código Funciona

1. **Importação de Biblioteca:**

```python
import math
```

A biblioteca `math` é utilizada para calcular a raiz quadrada inteira de `number` com `math.isqrt(number)`.

2. **Definição da Função:**

```python
def is_prime(number: int) -> bool:
```

A função recebe um número inteiro `number` e retorna `True` se ele for primo ou `False` caso contrário. Ela também inclui validação de entrada e documentação detalhada.

3. **Validação de Entrada:**

```python
if not isinstance(number, int) or number < 0:
    raise ValueError("O número deve ser um inteiro não negativo.")
```

- Garante que o parâmetro seja um inteiro não negativo, lançando um erro se não for.

4. **Tratamento de Casos Pequenos e Não Primos:**

```python
if number <= 1:
    return False
if number <= 3:
    return True
if number % 2 == 0:
    return False
```

- Números menores ou iguais a 1 não são primos.
- Os números 2 e 3 são primos.
- Se `number` for par e maior que 2, não é primo.

5. **Verificação de Divisores Ímpares:**

```python
upper_limit = int(math.isqrt(number))
for divisor in range(3, upper_limit + 1, 2):
    if number % divisor == 0:
        return False
```

- `upper_limit` é a raiz quadrada inteira de `number`.
- O loop verifica apenas números ímpares de 3 até `upper_limit`, pois fatores pares já foram descartados.
- Se `number` for divisível por algum `divisor`, ele não é primo.

6. **Retorno Final:**

```python
return True
```

Se nenhum divisor for encontrado, então `number` é primo.

## Exemplo de Uso

O bloco abaixo permite executar o arquivo diretamente e ver resultados de teste:

```python
def main():
    test_numbers = [1, 2, 3, 4, 16, 17, 19, 20]
    for num in test_numbers:
        result = is_prime(num)
        print(f"{num}: {'é primo' if result else 'não é primo'}")

if __name__ == "__main__":
    main()
```

Ele imprime se cada número da lista é primo ou não, com mensagens mais descritivas.

## Conclusão

A função `is_prime` segue princípios de Clean Code: nomes descritivos, validação de entrada, documentação clara e eficiência na verificação. Ela evita testar todos os números até `number` e usa apenas candidatos ímpares até a raiz quadrada de `number`.