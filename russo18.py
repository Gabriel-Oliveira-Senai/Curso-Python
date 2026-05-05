def ajustar_motor(nome_motor, posicao, velocidade):
    print(f"--- Configurando Hardware ---")
    print(f"Motor: {nome_motor}")
    print(f"posição: {posicao}°")
    print(f"Velocidade: {velocidade}%")
    print("----------------------------")


ajustar_motor("ombro_direito", 90, 50)
ajustar_motor("joelho_esquerdo", 45, 100)