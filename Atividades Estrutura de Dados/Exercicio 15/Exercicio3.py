# 3. Verificar se uma sequência de parênteses está balanceada (com pilha)

def esta_balanceado(sequencia):
    pilha = []
    for char in sequencia:
        if char == '(':
            pilha.append(char)
        elif char == ')':
            if not pilha:
                return False  # Fechou sem abrir
            pilha.pop()  # Fecha um parêntese aberto
    return len(pilha) == 0  # Se não sobrou nenhum, está balanceado

# Testes
codigo1 = "(()())"
codigo2 = "(()"
codigo3 = "())("

print(f"{codigo1} -> Balanceado? {esta_balanceado(codigo1)}")
print(f"{codigo2} -> Balanceado? {esta_balanceado(codigo2)}")
print(f"{codigo3} -> Balanceado? {esta_balanceado(codigo3)}")
