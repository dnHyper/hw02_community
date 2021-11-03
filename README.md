# Яндекс.Практикум. Спринт 3

#### Название: hw02_community
#### Группа: когорта 25
#### Когда: 2021 год
#### Кто: Алексей Ерёменко ( https://github.com/dnHyper/ )

------------

## Вместо вступления:
Если вы проходите обучение по курсу Яндекс.Практикум Python-разработчик, и должны выполнить финальный проект третьего спринта, в котором вы делаете практически с нуля социальную сеть, то … рекомендую подсматривать выложенный мной код лишь *в крайнем случае*. Лично я, во время написания данного кода, использовал лишь подсказки ревьюера, поисковик и документацию по python & django, советую и вам поступать таким же образом.

------------
# Описание:
Продолжение изучения Django в рамках курса Python-разработчик. Работаем над социальной сетью, разворачивая её на базе Django + Bootstrap.

Промежуточный этап.

В рамках спринта было добавлено:
 - Вывод десяти последних записей на главную страницу
 - Вывод десяти последних записей группы
 - В административной зоне можно добавлять/удалять записи и группы

**Вне программы**:
 - Пагинация
 - Оптимизация запросов
 - Страница списка существующих групп
 - Отдельная страница для ошибки 404 (**деактивировано**)

## Запуск проекта

Создайте и активируйте виртуальное окружение

    python3 -m venv venv
    source venv/Scripts/activate

Установите зависимости из файла requirements.txt

    python3 -m pip install --upgrade pip
    pip install -r requirements.txt

Выполните миграции

    python3 manage.py migrate


Создайте администратора

    python3 manage.py createsuperuser

Запустите проект

    python3 manage.py runserver

## Возможные проблемы

На данный момент никаких проблем при разворачивании приложения быть не должно. Стоит только учитывать, что база данных создаётся пустой, потому стоит перед началом работы минимально наполнить её, добавив хотя-бы одну группу и пост.

## Вместо послесловия

Во время выполнения данного урока (октябрь 2021) в архиве шаблона, который требовался по уроку и давался на странице урока, не оказалось изображений, которые нужны были на тот момент. Об этой проблеме сразу было сообщено в техническую поддержку.

В данный момент (ноябрь 2021) урок отредактирован: добавлен новый архив с картинками.

По условиям урока, в репозиторий папка со стилями и изображениями не отправляется, потому если они вам нужны, смотрите соответствующий урок или моё продолжение работы над соц.сетью.

## Лицензия
[MIT](https://ru.wikipedia.org/wiki/%D0%9B%D0%B8%D1%86%D0%B5%D0%BD%D0%B7%D0%B8%D1%8F_MIT)