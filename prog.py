import ttg

# Como adicionar novas proposições?
print('Tabela de p, q e r:\n')
print(ttg.Truths(['p', 'q', 'r\n']))

# Quantas operações o usuário deseja fazer?
# quant_operacoes = input('Quantas operações deseja fazer?')

# Utilizar listas
operacao = input('Qual operação você deseja realizar? ')
print(ttg.Truths(['p', 'q', 'r'], [operacao]))