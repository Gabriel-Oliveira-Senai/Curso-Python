total = 0
quantidade = 0

print("Digite 3 números para somer: ")

while quantidade < 3:
    numero = int(input("Digite um numero:"))
    quantidade = quantidade + 1
    total = total + numero
    
print(f"A soma total é {total}")