# Identificação e Correção de Erros em `debug.py`

Este arquivo identifica os erros presentes no código `debug.py`, explica suas causas e apresenta as correções aplicadas para tornar o código funcional.

## Código Original com Erros

```python
#                                      CÓDIGO COM ERROS                           
# ENTRADA DE DADOS
cliente = input("Qual é seu nome? ")

qtd1 = int(input("Quantidade do item 1: "))
item1 = float(input(Preço do item 1? ))  # Erro 1

qtd2 = int(input("Quantidade do item 2: "))
item2 = float(input("Preço do item 2? "))

qtd3 = int(input("Quantidade do item 3: "))
item3 = float(input("Preço do item 3? "))

# CÁLCULOS DOS ITENS
total_item1 = qtd1 * item1
total_item2 = qtd2 * item2
total_item3 = qtd3 * item3

subtotal = total_item1 + total_item2 + total_item3
imposto = subtotal * 0.10

# DESCONTO
desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))  # Erro 2
desconto = subtotal * (desconto_cupom / 100)  # Erro 3

# TOTAL FINAL
total = subtotal + imposto - desconto

# EXIBIÇÃO
linha = "=" * 31
separador = "-" * 31

print(linha)
print(f" Cliente: {cliente}")
print(linha)
print(f" Item 1:        R$ {total_item1:.2f}")
print(" Item 2:        R$ {total_item2:.2f}")  # Erro 4
print(f" Item 3:        R$ {total_item3:.2f}")
print(separador)
print(f" Subtotal:      R$ {subtotal:.2f}")
print(f" Imposto (10%): R$ {imposto:.2f}")

if desconto_cupom > 0:  # Erro 5
print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")  # Erro 6

print(linha)
print(f" TOTAL:         R$ {round(total, 2):.2f}")  # Erro 7
print(linha)
```

## Erros Identificados e Causas

1. **Erro 1: `item1 = float(input(Preço do item 1? ))`**
   - **Causa:** Falta de aspas ao redor da string no `input()`. Em Python, strings devem estar entre aspas simples ou duplas. Sem aspas, o interpretador trata "Preço" como uma variável indefinida, causando `NameError`.
   - **Correção:** Adicionar aspas: `float(input("Preço do item 1? "))`.

2. **Erro 2: `desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))`**
   - **Causa:** A função `input()` sempre retorna uma string, mesmo que o usuário digite um número. Isso é apropriado aqui, pois o código precisa converter para float posteriormente.
   - **Observação:** Não é erro, mas requer conversão para uso numérico.

3. **Erro 3: `desconto = subtotal * (desconto_cupom / 100)`**
   - **Causa:** `desconto_cupom` é uma string (do `input()`), e não pode ser dividida por 100 diretamente. Isso causa `TypeError: unsupported operand type(s) for /: 'str' and 'int'`.
   - **Correção:** Converter `desconto_cupom` para `float` antes da operação: `desconto = subtotal * (float(desconto_cupom) / 100)`.

4. **Erro 4: `print(" Item 2:        R$ {total_item2:.2f}")`**
   - **Causa:** Falta o prefixo `f` na string. Sem `f`, a string é literal e não interpola variáveis, causando saída incorreta ou erro se houver formatação avançada.
   - **Correção:** Adicionar `f`: `print(f" Item 2:        R$ {total_item2:.2f}")`.

5. **Erro 5: `if desconto_cupom > 0:`**
   - **Causa:** `desconto_cupom` é uma string, e comparar string com inteiro (`0`) pode não funcionar como esperado (ex: "10" > 0 é `TypeError` em Python 3). Mesmo se funcionasse, a lógica está incorreta.
   - **Correção:** Converter para float e comparar: `if float(desconto_cupom) > 0:`.

6. **Erro 6: `print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")`**
   - **Causa:** Falta indentação (deve estar dentro do `if`). Além disso, `desconto_cupom` é string, e `.0f` tenta formatar string como float, causando `ValueError`.
   - **Correção:** Indentar e converter: `print(f" Desconto ({float(desconto_cupom):.0f}%): -R$ {desconto:.2f}")`.

7. **Erro 7: `print(f" TOTAL:         R$ {round(total, 2):.2f}")`**
   - **Causa:** `round(total, 2)` já retorna um float arredondado, mas a f-string tenta formatar novamente com `:.2f`, o que é redundante e pode causar confusão. Além disso, a sintaxe `{round(total, 2):.2f}` é inválida; deve ser apenas `{total:.2f}`.
   - **Correção:** Simplificar para `print(f" TOTAL:         R$ {total:.2f}")`.

## Código Corrigido

```python
#                                      CÓDIGO CORRIGIDO
# ENTRADA DE DADOS
cliente = input("Qual é seu nome? ")

qtd1 = int(input("Quantidade do item 1: "))
item1 = float(input("Preço do item 1? "))

qtd2 = int(input("Quantidade do item 2: "))
item2 = float(input("Preço do item 2? "))

qtd3 = int(input("Quantidade do item 3: "))
item3 = float(input("Preço do item 3? "))

# CÁLCULOS DOS ITENS
total_item1 = qtd1 * item1
total_item2 = qtd2 * item2
total_item3 = qtd3 * item3

subtotal = total_item1 + total_item2 + total_item3
imposto = subtotal * 0.10

# DESCONTO
desconto_cupom = input("Você tem um cupom de desconto? (Digite o percentual ou 0): ")
desconto = subtotal * (float(desconto_cupom) / 100)

# TOTAL FINAL
total = subtotal + imposto - desconto

# EXIBIÇÃO
linha = "=" * 31
separador = "-" * 31

print(linha)
print(f" Cliente: {cliente}")
print(linha)
print(f" Item 1:        R$ {total_item1:.2f}")
print(f" Item 2:        R$ {total_item2:.2f}")
print(f" Item 3:        R$ {total_item3:.2f}")
print(separador)
print(f" Subtotal:      R$ {subtotal:.2f}")
print(f" Imposto (10%): R$ {imposto:.2f}")

if float(desconto_cupom) > 0:
    print(f" Desconto ({float(desconto_cupom):.0f}%): -R$ {desconto:.2f}")

print(linha)
print(f" TOTAL:         R$ {total:.2f}")
print(linha)
```

## Melhorias Adicionais

- Adicionada conversão explícita de `desconto_cupom` para `float` onde necessário.
- Corrigida indentação no bloco `if`.
- Removida redundância no `print` do total.
- O código agora calcula corretamente totais, impostos e descontos, exibindo um recibo formatado.