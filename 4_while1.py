"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""

# phrase = ''
def hello_user():
    phrase = ''
    while phrase != 'Хорошо':
      phrase = input('Как дела? ')
    
if __name__ == "__main__":
    hello_user()
