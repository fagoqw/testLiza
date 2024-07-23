from django.shortcuts import render, redirect
from .models import Comic, Panel
from django.contrib.auth.decorators import login_required


@login_required
def comic_create(request):
    if request.method == 'POST':
        pass
    else:
        pass


@login_required
def comic_edit(request, pk):
    comic = Comic.objects.get(pk=pk)
    if request.method == 'POST':
        pass
    else:
        pass


@login_required
def comic_detail(request, pk):
    comic = Comic.objects.get(pk=pk)
    return render(request, 'comics/comic_detail.html', {'comic': comic})


@login_required
def panel_add(request, pk):
    comic = Comic.objects.get(pk=pk)
    if request.method == 'POST':
        pass
    else:
        pass


@login_required
def panel_edit(request, pk, panel_pk):
    comic = Comic.objects.get(pk=pk)
    panel = Panel.objects.get(pk=panel_pk)
    if request.method == 'POST':
        pass
    else:
        pass


@login_required
def panel_delete(request, pk, panel_pk):
    comic = Comic.objects.get
