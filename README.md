Djbook.ru >> docset for Dash
======

Этот скрипт для тех кто хочет добавить себе в Dash русскую документацию по Django

![Alt text](http://pic.povary.ru/upload/2014/7/6/O_1404671154.jpg "Djbook.ru to Dash")


Описание
======

Создаем HTML документацию с помощью:
https://github.com/Alerion/django_documentation
```
$  python translator.py create
```

Создаем docset, используем doc2dash
```
$  pip install doc2dash
doc2dash -A <путь_к_html>
```

Используем мой скрипт
```
$  python djbook2set.py
```
