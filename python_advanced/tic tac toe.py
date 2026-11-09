import random
import time
import os

def show_field(field):
    viualised_field = field
    pass


def ask_for_game(games=0):
    if games == 0:
        answer = input('Здравствуйте! Не желаете ли сыграть?')
        if answer in {"нет", "н", "no"}:
            return ('Спасибо, что играли в крестики-нолики. Хорошего дня!')
        elif answer not in {"да", "д", "yes"}:
            return ('Простите, я вас не понял, так вы хотите поиграть?')
        else:
            games += 1
        pass
    else:
        answer = input('Сыграем еще разок?')
        if answer in {"нет", "н", "no"}:
            return ('Спасибо, что играли в крестики-нолики. Хорошего дня!')
        elif answer not in {"да", "д", "yes"}:
            return ('Простите, я вас не понял, так вы хотите поиграть?')
        else:
            games += 1
        pass


def who_goes_first():
    first_player = int(input('Кто будет ходить первым?(0 - игрок, 1 - компьютер)'))
    if first_player in [0, 1]:
        return first_player
    else:
        first_player = int(input('Пожалуйста, введите число 0 или 1'))
        pass


def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def get_user_move(field):
    current_move = input('Введите ряд и столбец следующего хода через пробел:').split()
    if current_move[0] in range(1,4) and current_move[1] in range(1,4) and len(current_move) == 2:
        if field(current_move[0], current_move[1]) == ' ':
            return (current_move[0], current_move[1])
        else:
            current_move = input('Эта клетка уже занята. Введите ряд и столбец следующего хода через пробел:').split()
    else:
        current_move = input('Кажется, вы ввели неверные значения. Введите ряд и столбец следующего хода через пробел:').split()


def get_computer_move(field):
    move = (random.randint(1, 3), random.randint(1, 3))
    if field[move[0]][move[1]] == ' ':
        return move
    else:
        move = (random.randint(1, 3), random.randint(1, 3))


def check_result(field):
    if field[0][0] == field[0][1] == field[0][2] or field[0][0] == field[1][0] == field[2][0] or field[1][0] == field[1][1] == field[1][2] or field[2][0] == field[2][1] == field[2][2] or field[0][1] == field[1][1] == field[2][1] or field[0][2] == field[1][2] == field[2][2] or field[0][0] == field[1][1] == field[2][2] or field[2][0] == field[1][1] == field[0][2]:
        if field[0][0] == 'X':
            return print('Крестики победили')
        if field[0][0] == 'O':
            return print('Нолики победили')
    else:
        return print('Победителя пока нет, продолжаем игру')


def main_game():
    ask_for_game()
    first_player = who_goes_first()
    field = [[' ' for _ in range(3)] for _ in range(3)]
    moves = 0
    if first_player:
        get_computer_move(field)
        moves += 1
        pass
    elif first_player is False:
        get_user_move(field)
        moves += 1
        pass