estoque = 50
quantidade_desejada = 30

if estoque > 0:
    if quantidade_desejada <= estoque:
        print("Produto disponível para compra.")
    else:
        print("Quantidade desejada não disponível.")
else:
    print("Produto fora de estoque.")