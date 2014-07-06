Djbook.ru >> gen docset for Dash
======

Этот скрипт для тех кто хочет добавить себе в Dash русскую документацию по Django

![Alt text](http://pic.povary.ru/upload/2014/7/6/O_1404671154.jpg "Djbook.ru to Dash")


Описание
======

Создаем HTML(Djbook.ru) документацию с помощью:
https://github.com/Alerion/django_documentation
```
$  python translator.py create
```
или используем готовую из html_doc

Генерим docset
```
$  pip install doc2dash
doc2dash -A <путь_к_html>
```

Создаем индексы
```
$  python djbook2set.py
```
