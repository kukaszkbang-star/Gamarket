import math


def is_prime(number: int) -> bool:
    """
    Verifica se um número inteiro é primo.

    Um número primo é um número natural maior que 1 que não tem divisores positivos
    além de 1 e ele mesmo.

    Args:
        number (int): O número a ser verificado.

    Returns:
        bool: True se o número for primo, False caso contrário.

    Raises:
        ValueError: Se o número não for um inteiro não negativo.
    """
    if not isinstance(number, int) or number < 0:
        raise ValueError("O número deve ser um inteiro não negativo.")

    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0:
        return False

    upper_limit = int(math.isqrt(number))
    for divisor in range(3, upper_limit + 1, 2):
        if number % divisor == 0:
            return False
    return True


def main():
    """Função principal para demonstrar a verificação de números primos."""
    test_numbers = [1, 2, 3, 4, 16, 17, 19, 20]
    for num in test_numbers:
        result = is_prime(num)
        print(f"{num}: {'é primo' if result else 'não é primo'}")


if __name__ == "__main__":
    main()
