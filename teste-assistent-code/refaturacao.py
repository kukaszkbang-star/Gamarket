def calcular_estatisticas(numeros):
    """
    Calcula estatísticas básicas de uma lista de números.

    Args:
        numeros (list): Lista de números (int ou float).

    Returns:
        tuple: (total, media, maior, menor)

    Raises:
        ValueError: Se a lista estiver vazia ou não contiver apenas números.
    """
    if not numeros:
        raise ValueError("A lista não pode estar vazia.")

    if not all(isinstance(num, (int, float)) for num in numeros):
        raise ValueError("A lista deve conter apenas números.")

    total = sum(numeros)
    media = total / len(numeros)
    maior = max(numeros)
    menor = min(numeros)

    return total, media, maior, menor


def main():
    """Função principal para demonstrar o cálculo de estatísticas."""
    lista_numeros = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    total, media, maior, menor = calcular_estatisticas(lista_numeros)

    print(f"Total: {total}")
    print(f"Média: {media}")
    print(f"Maior: {maior}")
    print(f"Menor: {menor}")


if __name__ == "__main__":
    main()