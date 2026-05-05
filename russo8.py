def calcular_preco_peca(preco_base, porcentagem_desconto):
    preco_desconto = preco_base * (porcentagem_desconto / 100)
    preco_final = preco_base - preco_desconto
    return preco_final  

valor_a_pagar = calcular_preco_peca(200, 10)
print(f"O cliente deve pagar: R$ {valor_a_pagar}")
