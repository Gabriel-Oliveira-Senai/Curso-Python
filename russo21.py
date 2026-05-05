notas = []

print("--- Sistemas de notas --- " )
      
for i in range(4):
    valor = float(input(f"Digite a nota {1+1}: "))
    notas.append(valor)

media = sum(notas) / len(notas)

print(f"\n Notas digitadas: {notas}")
print(f"Média final: {media:.2f}")

if media >= 6:
    print("resultado: aprovado!")
else:
    print("resultado: Recuperação")