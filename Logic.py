# hello_logic ('добрый день! Вам удобно сейчас говорить (да/нет/занят/еще раз)?', )

# hello = ('yes')

hello = input('Добрый день! Вам удобно сейчас говорить (да/нет/занят/еще раз)')
hello_repeat = ('Это компания @@@ Подскажите, вам удобно сейчас говорить?')
hello_null = ('Извините, вас не слышно. Вы могли бы повторить')

hangup_wrong_time = ('Извините пожалуйста за беспокойство. Всего вам доброго')
hangup_positive = ('Отлично!  Большое спасибо за уделенное время! Всего вам доброго!')
hangup_negative = ('Я вас понял. В любом случае большое спасибо за уделенное время!  Всего вам доброго. ')


def vote():                             # Recomendation
    print('Готовы ли вы рекомендовать нашу компанию. Оцените, по шкале от «0» до «10:')
    q = int(input())
    if 9 <= q <= 10:
        print(hangup_positive)
    elif 0 <= q <= 8:
        print(hangup_negative)
    else:
        print(hangup_wrong_time)


if hello == ('yes'):
    vote()
if hello == ('no'):
        print(hangup_negative)
if hello == ('занят'):
    print(hangup_wrong_time)


def main_logic():                             # main_logic
    print('Готовы ли вы рекомендовать нашу компанию. Оцените, по шкале от «0» до «10:')
    q = int(input())
    if 9 <= q <= 10:
        print(hangup_positive)
    elif 0 <= q <= 8:
        print(hangup_negative)
    else:
        print(hangup_wrong_time)
