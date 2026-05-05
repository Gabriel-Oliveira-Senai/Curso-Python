def verificar_revisao(quilometragem_atual):
    limite_revisao = 10000

    if quilometragem_atual >= limite_revisao:
        return "ALERTA: agendar revisão na oficina imediatamente" \
    
    else:
        km_restantes = limite_revisao - quilometragem_atual
        return f"Tudo certo. Faltam {km_restantes} km para proxima revisão"
    
print("Diagnóstico do Opala", verificar_revisao(10500))
print("Diagnóstico do Maveric", verificar_revisao(8200))
print("Diagnóstico da Caminhonete", verificar_revisao(10000))