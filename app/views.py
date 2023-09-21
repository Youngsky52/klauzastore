from django.shortcuts import render, get_object_or_404

from app.models import Produit


# Create your views here.


def index(request):
    pro = Produit.objects.all()
    if request.method == "GET":
        name = request.GET.get('sear')
        if name is not None:
            pro = Produit.objects.filter(name__icontains=name)
        else:
            pro = Produit.objects.all()

    return render(request, 'app/index.html', context={'pro':pro })


def detail(request, id):
    inf = get_object_or_404(Produit, id=id)

    return render(request, 'app/detail.html', context={'inf':inf})
