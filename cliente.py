import re
from OperacoesMatematicas import OperacoesMatematicas
from FormatMessage import encode_message
import datetime

calculadora = OperacoesMatematicas('localhost', 65432)
opcao = 0

def get_one_param():
  opcao = None
  while True:
    opcao = input('\n\nInforme um número:  ')
    if validate_option(opcao) == False:
      print('Erro, informação inválida!')
    else:
      break
  return opcao

def get_length_of_list():
  opcao = None
  while True:
    opcao = input('\n\nInforme tamanho da lista:  ')
    if validate_option(opcao) == False:
      print('Erro, informação inválida!')
    else:
      break
  return opcao


def get_any_params():
  numbers = num1 = input('\n\nInforme os números separados por espaço:  ')
  return numbers.split(' ')

def validate_option(opcao):
  try:
    int(opcao)
    return True
  except:
    return False

def validate_operation(opcao):
  return True if opcao in ['1', '2', '3', '4', '5', '6'] else False
    


while opcao != '6':
  opcao = input('''
  Selecione a opção:
  [1] soma
  [2] produto
  [3] fatorial
  [4] numeros primos
  [5] converter real para dólar
  [6] ajustar horário
  [7] sair\n''')
  retorno = 0
  if(validate_operation(opcao) == False):
    print('\nErro, operação inválida!\n')
    continue
  if opcao == '7':
    break
  if opcao == '3':
    retorno = get_one_param()
    print('\nFatorial de ', retorno, ' = ', calculadora.fatorial(retorno))
  elif opcao == '5':
    retorno = get_one_param()
    print('\n$',retorno,'em reais: R$', calculadora.realDolar(retorno))
  elif opcao == '4':
    retorno = get_length_of_list()
    print('\nNúmeros primos de 1 a ', retorno, ' = ', calculadora.numeroPrimo(retorno))
  elif opcao == '6':
    date = datetime.datetime(2022,11,11, 15, 30).timestamp() * 1000
    print('DATA', date)
    print('\nDiferença de horário ', date, ' = ', calculadora.horaCerta(date))
  else:
    retorno = get_any_params()
    if opcao == '1':
      print('\nSoma de ', retorno, ' = ', calculadora.soma(retorno))
    else:
      print('\nProduto de ', retorno, ' = ', calculadora.produto(retorno))

