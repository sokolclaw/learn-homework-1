"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

phrase = ''
def hello_user(phrase):
    
    while phrase != 'Хорошо':
         try:
            phrase = input('Как дела? ')
         except KeyboardInterrupt:
            print('Пока')
            break 
            
       


if __name__ == "__main__":
    hello_user(phrase)
