from django.http import JsonResponse
from django.shortcuts import render
from transliterate import translit
from main.models import Translation


def translator(request):
    """Получает с URL значение word.
     translated_word принимает значение word и оборачивается в метод translit который переводит кириллицу в латиницу.
     result принимает translated_word в виде списка.
     После этого translated_word сохраняется в базе данных.
     return возвращает result обертанным в метод JsonResponse, который переобразовывает в json формат
     """
    word = request.GET.get('word')
    translated_word = translit(word, 'ru', reversed=True)
    result = {'data': translated_word}
    Translation.objects.create(word=translated_word)
    return JsonResponse(result)


def history(request):
    """
    Переменная n получает с URL значение n,а если значение не задано, подставляет 5.
     n присваиваем значение int, иначе если n задано выдаст ошибку, что n это стринговое значение.
     Переменной words принмает значение всех сохраненных слов, затаем берет поле и  переобразовывает в списое.
     :return возвращает список сохраненных слов.
    """
    n = request.GET.get('n', 5)
    n = int(n)
    words = Translation.objects.order_by('-id').all()[:n].values_list('word', flat=True)
    save_word = {'data': list(words)}
    return JsonResponse(save_word)


def index(request):
    """Главная странциа где будет отображаться index.html"""
    return render(request, 'index.html')

