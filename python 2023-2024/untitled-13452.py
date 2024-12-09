from colorama import Fore
counter_user_answers = counter_edited_s_answers_user = 0
counter_user_action = count_example = count_example_ = 1
copy_user_answer = copy_user_result = None

def check_user_answer(user_answer, x_one=1, x_two=1):
    global counter_user_answers
    if len(user_answer) != 0:
        if sum(1 for letter in user_answer if letter.isalpha()) == 0 \
                and sum(1 for digit in user_answer if digit.isdigit()) >= 1:
            if sum(1 for comma in user_answer if comma == ',') == 1 \
                    and user_answer[0].isdigit() \
                    and sum(1 for digit in user_answer if digit.isdigit()) == len(user_answer) - 1:
                user_answer = float(user_answer.replace(',', '.'))
            elif sum(1 for comma in user_answer if comma == ',') == 1 \
                    and user_answer[0] == '-' and user_answer[1].isdigit() \
                    and sum(1 for digit in user_answer if digit.isdigit()) == len(user_answer) - 2:
                user_answer = float(user_answer.replace(',', '.'))
            elif sum(1 for period in user_answer if period == '.') == 1 \
                    and user_answer[0].isdigit() \
                    and sum(1 for digit in user_answer if digit.isdigit()) == len(user_answer) - 1:
                user_answer = float(user_answer)
            elif sum(1 for period in user_answer if period == '.') == 1 \
                    and user_answer[0] == '-' and user_answer[1].isdigit() \
                    and sum(1 for digit in user_answer if digit.isdigit()) == len(user_answer) - 2:
                user_answer = float(user_answer)
            elif sum(1 for period in user_answer if period == '.') == 1 \
                    and user_answer[0] == '+' and user_answer[1].isdigit() \
                    and sum(1 for digit in user_answer if digit.isdigit()) == len(user_answer) - 2:
                user_answer = float(user_answer.replace('+', ''))
            elif sum(1 for comma in user_answer if comma == ',') == 1 \
                    and user_answer[0] == '+' and user_answer[1].isdigit() \
                    and sum(1 for digit in user_answer if digit.isdigit()) == len(user_answer) - 2:
                user_answer = float(user_answer.replace(',', '.').replace('+', ''))
            elif user_answer[0] == '-' \
                    and sum(1 for digit in user_answer if digit.isdigit()) == len(user_answer) - 1:
                user_answer = float(user_answer)
            elif user_answer[0] == '+' \
                    and sum(1 for digit in user_answer if digit.isdigit()) == len(user_answer) - 1:
                user_answer = float(user_answer.replace('+', ''))
            elif sum(1 for digit in user_answer if digit.isdigit()) == len(user_answer):
                user_answer = float(user_answer)
            else:
                return 'Error'

            answer = round(((-1 * x_two) / x_one), 1)
            if user_answer == answer:
                counter_user_answers += 1
    return user_answer
    
def replace_user_answer(user_input, list_answers, list_examples):
    global counter_user_answers, count_example
    if user_input == 'Да' or user_input == 'yes':
        user_input = True
        while user_input == True:
            print('_' * 60)
            for answer in list_answers:
                index_answer = list_answers.index(answer)
                print(f'{f"Пример {count_example} | {list_examples[index_answer][0]} + {list_examples[index_answer][1]} = 0":<24} | ', end='')
                print(f'Ваш ответ: {answer}')
                count_example += 1
            count_example = 1
            number_example = input('\nВведите номер примера, в котором вы хотите исправить ответ: ')
            while not(number_example.isdigit()):
                number_example = input(Fore.LIGHTRED_EX + '\nValueError\nВведите номер примера, в котором вы хотите исправить ответ: ')
            while not(int(number_example) in range(1, 8)):
                number_example = input(Fore.LIGHTRED_EX + '\nlist index out of range\nВведите номер примера, в котором вы хотите исправить ответ: ')
            print(Fore.LIGHTWHITE_EX + '_' * 60)
            if ' (edited)' in str(list_answers[int(number_example) - 1]):
                copy_answer = list_answers[int(number_example) - 1].replace(' (edited)', '')
                if str(copy_answer) == str(round(((-1 * list_examples[int(number_example) - 1][1]) / list_examples[int(number_example) - 1][0]), 1)):
                    counter_user_answers -= 1
            else:
                if str(list_answers[int(number_example) - 1]) == str(round(((-1 * list_examples[int(number_example) - 1][1]) / list_examples[int(number_example) - 1][0]), 1)):
                    counter_user_answers -= 1
            print(Fore.LIGHTWHITE_EX + f'Пример {number_example}\n\n{list_examples[int(number_example) - 1][0]} + {list_examples[int(number_example) - 1][1]} = 0')
            print('\nВведите ответ: ', end='')
            list_answers[int(number_example) - 1] = check_user_answer(input(),
            list_examples[int(number_example) - 1][0],
            list_examples[int(number_example) - 1][1])
            list_answers[int(number_example) - 1] = str(list_answers[int(number_example) - 1]) + ' (edited)'
            print('_' * 60)
            print(f'Хотите исправить ответ ещё в каком-нибудь примере{chr(10067)}{chr(10071)}\n'
                  f'Если да, то введите "Да".\nЕсли нет, то введите "Я исправил(а) то, что хотел(а).\nЧто выбираете: ', end='')
            user_input = input().capitalize()
            if user_input != 'Да':
                user_input = False
            else:
                user_input = True
    return list_examples, list_answers
    
def user_action():
    global counter_user_action
    print(f'{counter_user_action} действие: ', end='')
    user_action = input().lower()
    while user_action != 'записать ответ':
        if user_action == 'write answer':
            user_action = 'записать ответ'
        else:
            counter_user_action += 1
            print(f'{counter_user_action} действие: ', end='')
            user_action = input().lower()
    counter_user_action = 1

def print_user_answers(list_answers, list_examples):
    global counter_edited_s_answers_user, count_example_, counter_user_answers, copy_user_answer
    for user_answer in list_answers:
        index_user_answer = list_answers.index(user_answer)
        if ' (edited)' in str(user_answer):
            counter_edited_s_answers_user += 1
            copy_user_answer = user_answer.replace(' (edited)', '')
        else:
            copy_user_answer = user_answer
        if counter_edited_s_answers_user > 0:
            print(Fore.LIGHTWHITE_EX + f'Пример {count_example_} | {f"{list_examples[index_user_answer][0]} + {list_examples[index_user_answer][1]} = 0":<13} | ', end='')
            if str(copy_user_answer) == str(round(((-1 * list_examples[index_user_answer][1]) / list_examples[index_user_answer][0]), 1)):
                print(Fore.LIGHTGREEN_EX + f'{f"Ответ пользователя: {user_answer}":<{max(len(str(answer)) for answer in list_answers) + 20}} ', end='')
                print(Fore.LIGHTWHITE_EX + f'| Правильный ответ: {round(((-1 * list_examples[index_user_answer][1]) / list_examples[index_user_answer][0]), 1)} | ', end='')
                print('Баллы: ' + Fore.LIGHTGREEN_EX + '1')
            else:
                print(Fore.LIGHTRED_EX + f'{f"Ответ пользователя: {user_answer}":<{max(len(str(answer)) for answer in list_answers) + 20}} ', end='')
                print(Fore.LIGHTWHITE_EX + f'| Правильный ответ: {round(((-1 * list_examples[index_user_answer][1]) / list_examples[index_user_answer][0]), 1)} | ', end='')
                print('Баллы: ' + Fore.LIGHTRED_EX + '0')
        else:
            print(Fore.LIGHTWHITE_EX + f'Пример {count_example_} | {f"{list_examples[index_user_answer][0]} + {list_examples[index_user_answer][1]} = 0":<13} | ', end='')
            if str(user_answer) == str(round(((-1 * list_examples[index_user_answer][1]) / list_examples[index_user_answer][0]), 1)):
                print(Fore.LIGHTGREEN_EX + f'{f"Ответ пользователя: {user_answer}":<{max(len(str(answer)) for answer in list_answers) + 20}} ', end='')
                print(Fore.LIGHTWHITE_EX + f'| Правильный ответ: {round(((-1 * list_examples[index_user_answer][1]) / list_examples[index_user_answer][0]), 1)} | ', end='')
                print('Баллы: ' + Fore.LIGHTGREEN_EX + '1')
            else:
                print(Fore.LIGHTRED_EX + f'{f"Ответ пользователя: {user_answer}":<{max(len(str(answer)) for answer in list_answers) + 20}} ', end='')
                print(Fore.LIGHTWHITE_EX + f'| Правильный ответ: {round(((-1 * list_examples[index_user_answer][1]) / list_examples[index_user_answer][0]), 1)} | ', end='')
                print('Баллы: ' + Fore.LIGHTRED_EX + '0')
        count_example_ += 1
    count_example_ = 1

    print(Fore.LIGHTWHITE_EX + f'\nКоличество правильных ответов пользователя: {counter_user_answers}\n'
          f'Количество неправильных ответов пользователя: {7 - counter_user_answers}\n'
          f'Количество отредактированных ответов пользователя: {counter_edited_s_answers_user}\n'
          f'{"_" * 50}')

def print_user_name():
    with open('user_name.txt', 'r') as file_for_user_name:
        print('_' * len(file_for_user_name.read()))
        print(file_for_user_name.read())