from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, мл': 1,
        'соль, ч.л.': 1,
    },
    'pasta': {
        'макароны, г': 30,
        'сыр, г': 5,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def colculator(requests, dish):
    servings = int(requests.GET.get("servings", 1))
    print(servings)

    d_dish = DATA.get(dish)
    context = {
        "recipe": d_dish,
        "servings": servings
    }

    return render(requests, "calculator/index.html", context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
