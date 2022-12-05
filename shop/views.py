from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect

from .models import Item, Purchase


def list_item(request):
    xz = Item.objects.all()
    context = {
        'xz': xz,
    }
    return render(request, 'list_item.html', context)


def detail_item(request, id):
    xzx = get_object_or_404(Item, id=id)
    context = {
        'xzx': xzx,
    }
    return render(request, 'detail_item.html', context)
