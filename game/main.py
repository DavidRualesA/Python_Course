# Este es el tradicional juego de piedra, papel o tijera

# Iniciamos definiendo las variables y llamando la biblioteca de numeros


# Definimos las opciones del juego
import random

def choose_option ():

  options = ('piedra', 'papel', 'tijera')

  usuario = input("Elige piedra, papel o tijera: ").lower()
  if usuario not in options:
    print("Esa opcion no es valida")
    return None, None

  computador = random.choice(options)
  print("Usuario elige: ", usuario)
  print("Computador elige: ", computador)
  return usuario, computador

def check_rules(usuario, computador, user_win, computer_win):

  if usuario == computador:
    print('Empate')
  elif (usuario == 'piedra' and computador == 'tijera') or \
    (usuario == 'papel' and computador == 'piedra') or \
    (usuario == 'tijera' and computador == 'papel'):
    print('gana usuario')
    user_win += 1
  else:
    print('gana computador')
    computer_win += 1

  return user_win,computer_win


def run_game():

  user_win = 0
  computer_win = 0
  rounds = 1
  wins = int(input("Cuantas veces para ganar: "))

  while True:

    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)

    print('computer_win', computer_win)
    print('user_win', user_win)
    rounds += 1 

    usuario, computador = choose_option()
    user_win, computer_win = check_rules(usuario, computador, user_win, computer_win)

    if user_win == wins:
      print('El ganador es el usuario')
      break

    if computer_win == wins:
      print('El ganador es el computador')
      break


run_game()