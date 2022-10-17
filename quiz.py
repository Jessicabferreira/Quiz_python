print('Seja bem vindo ao quiz da Jessica!')
print('Ai vai algumas perguntas sobre a linguagem Python!')

usuario = input('Quer começar? (S/N) ').upper()
print(usuario)

if usuario != 'S':
    quit()

pontos = 0

print('Começando... \n')
print('O que é Python? \n (A) Aplicativo \n (B) Documento \n (C) Linguagem de programação \n (D) IDE \n')
resposta_1 = input('Resposta: \n').upper()

if resposta_1 == 'C':
    print('Correto')
    pontos = pontos + 1
else:
    print('Incorreto\n')
print()
print('O simbolo # é usuado para? \n (A) Pular linha \n (B) Deixar a palavra em negrito \n (C) Separae as palavras \n '
'(D) Fazer comentario \n')
resposta_2 = input('resposta: \n').upper()

if resposta_2 == 'D':
    print('Correto')
    pontos = pontos + 1
else:
    print('Incorreto')

print(f'Quiz acabou... Pontuação: {pontos}/2')


