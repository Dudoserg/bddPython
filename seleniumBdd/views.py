from django.shortcuts import render


def base(request):
    print("asd")
    return render(request, 'seleniumBdd/base.html')


def create_material(request):
    return render(request, 'seleniumBdd/create.html')