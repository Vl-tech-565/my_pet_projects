# dependencies
import caesar
import time


# preparation
langs = {'1' : 'rus', '2' : 'en'}

print('Привет! Данная программа умеет кодировать и декодировать строки.')
time.sleep(1.5)
print('''Примечание: данная программа может шифровать и дешифровать двумя способами:
               стандартный - шаг сдвига указывается пользователем,
               хитрый - шаг сдвига подбирается индивидуально для каждого слова
               подбирается исходя из его длины (для слова "привет" сдвиг будет 
               равен 6, а для слова "Hello" - 5, и т.д.''')
print()



def get_action():
    action = input('Что ты хочешь сделать? (1 - закодировать строку, 2 - декодировать строку, 3 - закончить) >> ')
    while not action in ['1', '2', '3']:
        action = input('Не знаю такой команды, попробуй еще раз >> ')
    
    return action


def get_data():
    way = input('''Каким способом ты хочешь это сделать:
                               1 - стандартный, 2 - хитрый >> ''')
    while way not in ['1', '2']:
        way = input('Я не знаю такого способа, попробуй ещё раз >> ')

    lang = input('Выбери язык: 1 - русский, 2 - английский, 3 - все вместе >> ')
    while not lang in ['1', '2', '3']:
        lang = input('Я не знаю такого языка, попробуй еще раз >> ')

    original_str = input('Введи строку >> ')

    print()

    return way, lang, original_str


def get_step():
    step = input('Введи значение сдвига >> ')
    while (not step.isdigit()):
        step = input('Ты ввел не число, попробуй ещё раз >> ')
    
    step = int(step)

    return step


# main loop
while True:
    try:
        time.sleep(1)
        print()
        
        action = get_action()

        if action == '1':
            way, lang, original_str = get_data()
            if way == '1':
                step = get_step()
                if lang == '3':
                    print(f'закодированная строка: {caesar.encode_all_lang(original_str, step=step)}')
                else:
                    print(f'закодированная строка: {caesar.encode(original_str, lang=langs[lang], step=step)}')
            else:
                if lang == '3':
                    print(f'закодированная строка: {caesar.encode_pro_all_lang(original_str)}')
                else:
                    print(f'закодированная строка: {caesar.encode_pro(original_str, lang=langs[lang])}')

        if action == '2':
            way, lang, original_str = get_data()

            if way == '1':
                step = get_step()
                if lang == '3':
                    print(f'декодированная строка: {caesar.decode_all_lang(original_str, step=step)}')
                else:
                    print(f'декодированная строка: {caesar.decode(original_str, lang=langs[lang], step=step)}')
            else:
                if lang == '3':
                    print(f'декодированная строка: {caesar.decode_pro_all_lang(original_str)}')
                else:
                    print(f'декодированная строка: {caesar.decode_pro(original_str, lang=langs[lang])}')


        if action == '3':
            print('Пока!')
            time.sleep(2)
            break

    except Exception as e:
        print('Что-то пошло не так, программа завершает работу...')
        time.sleep(3)
        break
