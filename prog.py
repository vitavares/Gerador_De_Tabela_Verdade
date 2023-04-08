import ttg

i = 0
listaOperacoes = []
continuar = True
# Como adicionar novas proposições?
print('Tabela de p, q e r:\n')
print(ttg.Truths(['p', 'q', 'r\n']))

# Quantas operações o usuário deseja fazer?

while continuar:
    op = input("Digite uma para operação (ou 'fim' para ver o resultado da operações): ")
    if op == "fim":
        continuar = False
    else:
        listaOperacoes.append(op)

print("As operações escolhidas foram:", listaOperacoes)

# print(ttg.Truths(['p', 'q', 'r'], [operacao]))