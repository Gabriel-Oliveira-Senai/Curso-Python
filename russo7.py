def processar_boletim(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3

    if media >= 6.0: 
        situacao = "Aprovado" 
    else: 
        situacao = "Reprovado" 
    return media, situacao

media_aluno, status_aluno = processar_boletim(7.5, 5.0, 8.0)

print(f"Resultado final: Media {media_aluno:.1f} -> Status {status_aluno}")
