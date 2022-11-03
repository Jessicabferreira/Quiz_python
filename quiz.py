print(''' 
    Seja bem vindo ao Quiz da Jessica!
    
    Ai vai algumas perguntas sobre Alimentação Saudável!

''')
print('Vamos começar... \n')

print('1- Alimentação saudável é constituída por equilíbrio, variação e moderação. \n ')
print('(A) V \n')
print('(B) F \n')


pontos = 0

resposta_1 = input('Digite uma das opções: \n').upper()

if resposta_1 == 'A':
    print('Correto! \n')
    pontos = pontos + 1
else:
    print('Incorreto! \n')

print('2- Uma alimentação adequada é essencial para o bem estar físico e mental do indivíduo. \n')
print('(A) F \n')
print('(B) V \n')


resposta_2 = input('Digite uma das opções: \n').upper()

if resposta_2 == 'B':
    print('Correto! \n')
    pontos = pontos + 1
else:
    print('Incorreto! \n')

print('3- Quais são os alimentos de origem animal? \n')
print('(A) Leite, pão e arroz \n')
print('(B) Ovos, carne e leite \n')
print('(B) Feijão, manteiga e leite \n')
print('(B) Banha, carne e farinha \n')

resposta_3 = input('Digite uma das opções: \n').upper()


if resposta_3 == 'B':
    print('Correto! \n')
    pontos = pontos + 1
else:
    print('Incorreto! \n')

print('4- Quais os nomes comuns de lactose e frutose? \n')
print('(A) Leite e Frutas \n')
print('(B) Laticínios e Frutas \n')
print('(C) Açúcar do Leite e Açúcar das Frutas \n')

resposta_4 = input('Digite uma das opções: \n').upper()

if resposta_4 == 'C':
    print('Correto! \n')
    pontos = pontos + 1
else:
    print('Incorreto! \n')

print('5- Que tipo conhecido de substância química alimentícia é um carboidrato completo? \n')
print('(A) Glicose \n')
print('(B) Amido \n')
print('(C) Glicídio \n')

resposta_5 = input('Digite uma das opções: \n').upper()

if resposta_5 == 'B':
    print('Correto! \n')
    pontos = pontos + 1
else:
    print('Incorreto! \n')

print('6- Quais são os órgãos do sistema digestório? \n')
print('(A) O nariz, a boca e o estômago \n')
print('(B) O intestino delgado e a traqueia \n')
print('(C) A boca, o estômago e o intestino delgado \n')
print('(D) O estômago, o coração e a laringe \n')

resposta_6 = input('Digite uma das opções: \n').upper()

if resposta_6 == 'C':
    print('Correto! \n')
    pontos = pontos + 1
else:
    print('Incorreto! \n')

print('7- Como é chamada a transformação dos alimentos dentro do nosso corpo? \n')
print('(A) Circulação \n')
print('(B) Nutrição \n')
print('(C) Mastigação \n')
print('(D) Digestão \n')

resposta_7 = input('Digite uma das opções: \n').upper()

if resposta_7 == 'D':
    print('Correto! \n')
    pontos = pontos + 1
else:
    print('Incorreto! \n')

print('8- Qual dos alimentos a seguir é o mais saudável? \n')
print('(A) Verduras \n')
print('(B) Frutas \n')
print('(C) Óleos vegetais \n')
print('(D) Leite e derivados \n')
print('(E) Legumes \n')

resposta_8 = input('Digite uma das opções: \n').upper()

if resposta_8 == 'C':
    print('Correto! \n')
    pontos = pontos + 1
else:
    print('Incorreto! \n')

print('9- Quais desses alimentos são de origem vegetal? \n')
print('(A) Carne \n')
print('(B) Ovos \n')
print('(C) Verduras \n')
print('(D) Chocolate \n')

resposta_9 = input('Digite uma das opções: \n').upper()

if resposta_9 == 'C':
    print('Correto! \n')
    pontos = pontos + 1
else:
    print('Incorreto! \n')

print('10- Qual nutriente tem função construtora com principal função? \n')
print('(A) Carboidratos \n')
print('(B) Sais Minerais \n')
print('(C) Fibras \n')
print('(D) Proteínas \n')
print('(E) Vitaminas \n')

resposta_10 = input('Digite uma das opções: \n').upper()

if resposta_10 == 'E':
    print('Correto! \n')
    pontos = pontos + 1
else:
    print('Incorreto! \n')

print(f'Quiz acabou... Parabéns sua pontuação foi: {pontos}/10')


