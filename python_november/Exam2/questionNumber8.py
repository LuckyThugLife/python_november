# Представления  взаимодействуют с моделями и шаблонами.
# Они получают данные из моделей, передают их в шаблоны и возвращают ответ клиенту.
# Отличие шаблонов от файлов HTML  в том, что шаблоны содержат  синтаксис,
# который позволяет вставлять динамический контент.
# В шаблонах можно использовать переменные, циклы, условные операторы и
# другие динамические конструкции,
# Файлы HTML,  являются статическими файлами, которые содержат только HTML-код.


from django.shortcuts import render


def my_view(request):
    my_variable = 'Hello, World!'
    context = {'my_variable': my_variable}
    return render(request, 'my_template.html', context)

# мы создали переменную my_variable со значением 'Hello, World!'.
# после создали словарь context, с переменной my_variable.
# передаем этот словарь в функцию render, которая отображает шаблон my_template.html.
#
# В шаблоне my_template.html используем переменную my_variable,



<!DOCTYPE html>
<html>
<head>
    <title>My Template</title>
</head>
<body>
    <h1>{{ my_variable }}</h1>
</body>
</html>


#  используем специальный синтаксис {{ my_variable }}
# для вставки значения переменной my_variable в HTML-код.