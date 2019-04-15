from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from seleniumBdd.models import Material

@csrf_exempt
def base(request):
    print("asd")
    # print(request.GET['value'])
    materials = Material.objects.all()
    # materials.html
    return render(request, 'seleniumBdd/base.html', {'material': materials})

@csrf_exempt
def create_material(request):
    return render(request, 'seleniumBdd/create.html')


@csrf_exempt
def add_in_base(request):
    title = request.POST['title']
    img = request.POST['img']
    code = request.POST['code']
    balance = request.POST['balance']

    material = Material(title=title, code_material=code, img=img, balance=balance)
    material.save()
    return HttpResponse("Success!")


