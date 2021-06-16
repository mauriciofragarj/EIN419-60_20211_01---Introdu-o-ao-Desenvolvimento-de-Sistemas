print('''
________________________
ONDE ESTÁ MICHELANGELO? 
________________________

Giorgio Vasari , historiador da arte italiano, precisa encontrar Michelangelo para uma 
entrevista, mas não sabe onde ele pode estar. Ajude Vasari a encontrar Michelangelo!
''')
print('_________________________________________________________________________________________')
print()
print("Vasari: - Bartolomeo,onde está Messer Michelangelo?")
print("Bartolomeo: - Michelangelo está junto de sua escultura que é o símbolo da República de Florença!")
print()
print('''Qual escultura é o símbolo da República de Florença?

a) O Rapto das Sabinas
b) Davi
c) Baco
''')
resposta1 = input('Digite a opção correta:')
print()
if resposta1 == 'a':
    print('Não, "O Rapto das Sabinas" é uma obra de Giambologna!')
elif resposta1 == 'b':
    print('Bravo! O Davi é o símbolo da República de Florença!')
elif resposta1 == 'c':
    print('Não, o Baco é uma escultura de Michelangelo, mas não é o símbolo da República de Florença.')
else:
    print('Esta não é uma opção válida! Escolha entre a, b ou c.')
print('Michelangelo não está mais aqui. E agora, onde estará Michelangelo?')
print('_________________________________________________________________________________________')
print()
print('Vasari: - Cecilia, onde está Messer Michelangelo?')
print('Cecilia: - Michelangelo está na sacristia com os túmulos que fez para a família Medici.')
print ()
print('''Onde fica a sacristia com os túmulos que Michelangelo fez para a família Medici?

a) Igreja de Santa Maria Novella
b) Igreja de Santa Croce
c) Igreja de San lorenzo
''')
resposta2 = input('Digite a opção correta:')
print()
if resposta2 == 'a':
    print('Não, na sacristia de Santa Maria Novella não há túmulos!')
elif resposta2 == 'b':
    print('Não, na sacristia de Santa Croce temos os afrescos de Taddeo Gaddi!')
elif resposta2 == 'c':
    print('Bravo! Na sacristia de San Lorenzo temos os túmulos esculpidos por Michelangelo!')
else:
    print('Esta não é uma opção válida! Escolha entre a, b ou c.')
print('Cheguei tarde demais, Michelangelo já saiu. Melhor perguntar para alguém...')
print('_________________________________________________________________________________________')
print()
print('Vasari: - Rafael, onde está Messer Michelangelo?')
print('Rafael: - Michelangelo está vendo as pinturas que fez para a capela do Papa.')
print()
print('''Qual pintura Michelangelo fez para a capela do Papa?

a) Criação do Homem
b) Disputa do Santíssimo Sacramento
c) Escola de Atenas
''')
resposta3 = input('Digite a opção correta:')
print()
if resposta3 == 'a':
    print('Bravo! A Criação do Homem é uma das cenas que Michelangelo pintou no teto da Capela Sistina!')
elif resposta3 == 'b':
    print('Não, a Disputa do Santíssimo Sacramento é um afresco de Rafael pintado nas salas do Vaticano!')
elif resposta3 == 'c':
    print('Não, a Escola de Atenas é um afresco de Rafael pintado nas salas do Vaticano!')
else:
    print('Esta não é uma opção válida! Escolha entre a, b ou c.')
print('_________________________________________________________________________________________')
print()
print('Michelangelo: - Olá, Messer Vasari.')
print('Vasari: - Finalmente, Messer Michelangelo! Podemos conversar sobre o meu livro?')
if resposta1 == 'b': score1 = 1
else: score1 = 0
if resposta2 == 'c': score2 = 1
else: score2 = 0
if resposta3 == 'a': score3 = 1
else: score3 = 0
scoretotal = score1 + score2 + score3
if scoretotal == 3:
    print('Michelangelo: - Você conhece muito sobre minhas obras! Será um prazer ajudá-lo!')
if scoretotal == 2:
    print('Michelangelo: - Sim, ajudarei um estudioso em sua busca por conhecimento.')
if scoretotal == 1:
    print('Michelangelo: - Sim, desde que seja breve.')
if scoretotal == 0:
    print('Michelangelo: - Desculpe, mas não posso ajudá-lo agora.')
print()
print('GAME OVER')


# ____________________________________________________
# comentários#
# fundo = PhotoImage(file="img_title.png")
# class fundo

# ____________________________________________________
