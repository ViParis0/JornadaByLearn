def calcular_media(notas):

  quantidade = len(notas)
  soma = sum(notas)
  media = soma / quantidade
  print('Aluno tirou', media)
  verificar_aprovacao(media)

def verificar_aprovacao(media):
  if media >= 6:
    print('Aluno aprovado')
  else:
    print('Aluno reprovado')



calcular_media([10, 9, 8, 7])