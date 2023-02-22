# World_of_sweet_Bot

[![Generic badge](https://img.shields.io/badge/Python-3.10-green.svg)](https://www.python.org/)



Hello!:hand:

В этом репозитории представлен **Телеграм бот** для магазина сладостей на **Python**.
___


## Использование
Найти и протестировать телеграм бота вы сможете по этой ссылке `https://t.me/World_of_sweets_Bot.

**КЛИЕНТКАЯ ВЕРСИЯ**

1. Нажмите ***'Запустить'***
2. У вас появятся следующие кнопки:
   * Режим работы (отправка ответным сообщением графика работы магазина)
   * Расположение (отправка адреса магазина)
   * Меню (отправка меню магазина)
   * Свяжитесь со мной (отправка номера телефона)
   * Мой город (отправка геолокации)
   * Выход (позволяет вернуться в предстартовое положение)
   
**АДМИНСКАЯ ВЕРСИЯ**
(доступ предоставляется по id)
1. Для перехода воспользуйтесь командой `/admin`
2. Далее доступно 2 опции:
    * Загрузить (после нажатия будет предложено поэтапно загрузить в бота фото, название, описание и цену товара. Сначала данные хранятся в оперативной памяти, затем вносятся в базу данных SQLite, которая создастся автоматически при отсутствии);
    * Удалить (после нажатия отобразится все меню из базы данных SQLite и Inline-кнопки для удаления под каждой записью).
    

___

## Установка
Перед установкой на своем сервере необходимо получить ___token___ и ___users' id___ администраторов. 
После этого необходимо установить зависимости.
```
   pip install -r requirements.txt
```
Далее запустить файл локально командой `python World_of_sweet_bot.py`
___

##Планируемые дополнения
* Боковое меню
* Иконки рядом с кнопками команд
* Создать дополнительную базу данных для учета данных клиентов
* Добавить возможность заказа доставки
* Оплата
* Парсинг информации
* Оборачивание в контейнер и запуск в Docker (коммерческие проекты на Heroku и т.п.)
___

## Technologies
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)   
- [x] [Python](https://www.python.org/) 3.10  :snake:
- [ ] [Docker](https://www.docker.com/) 20.10.22  :whale:
___

## License
Apache-2.0



<img src="https://cdn-icons-png.flaticon.com/512/919/919852.png?w=740&t=st=1674815666~exp=1674816266~hmac=d8675dffadfc01e1bb6ec97b220b11c5e004da72099526ebc7569461b3b0ce53" width="150" height="150" >