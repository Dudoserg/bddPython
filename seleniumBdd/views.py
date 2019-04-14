from django.shortcuts import render


def base(request):
    print("asd")
    return render(request, 'seleniumBdd/base.html')