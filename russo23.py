tempos_voltas = []

print("--- Registro de Tempos: Stock Car ---")

for i in range(5):
    tempo = float(input(f"Digite o tempo da volta {i+1} (em segundos):"))
    tempos_voltas.append(tempo)

melhor_tempo = min(tempos_voltas)

posicao_melhor = tempos_voltas.index(melhor_tempo) + 1

media_tempo = sum(tempos_voltas) / len(tempos_voltas)

print("\n--- Resultados ---")
print(f"O melhor tempo foi de {melhor_tempo:.2f} em segundos")
print(f"A sua maior posição foi {posicao_melhor:.2f}")
print(f"A media foi de {media_tempo:.2f} segundos")