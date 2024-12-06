def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
    if recipient == sender:
        return print('Нельзя отправить письмо самому себе!')

    num_ch = [sender.rfind('@'), recipient.rfind('@'), sender.rfind('.'), recipient.rfind('.')]

    dots = ('.com', '.ru', '.net')

    if -1 in num_ch or (sender[num_ch[2]:] not in dots) or (recipient[num_ch[3]:] not in dots):
        return print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

    if sender != 'university.help@gmail.com':
        return print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
    else:
        return print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')



send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')