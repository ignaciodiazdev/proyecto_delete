from django.shortcuts import render, redirect
from . import models, forms
# Create your views here.


def home(request):
    return render(request, "producto/index.html")


def productocategoria_list(request):
    consulta = request.GET.get("consulta", None)
    if consulta:
        print(consulta)
        query = models.ProductoCategoria.objects.filter(
            nombre__icontains=consulta)
    else:
        query = models.ProductoCategoria.objects.all()
    context = {"productos": query}
    return render(request, "producto/productocategoria_list.html", context)


def productocategoria_create(request):

    if request.method == "POST":
        form = forms.ProductoCategoriaForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("producto:home")
    else:
        form = forms.ProductoCategoriaForm()
    return render(request, "producto/productocategoria_create.html", context={"form": form})


def productocategoria_detail(request, pk: int):
    query = models.ProductoCategoria.objects.get(id=pk)
    return render(request, "producto/productocategoria_detail.html", context={"producto": query})


def productocategoria_update(request, pk: int):
    query = models.ProductoCategoria.objects.get(id=pk)
    if request.method == "POST":
        form = forms.ProductoCategoriaForm(request.POST, instance=query)
        if form.is_valid:
            form.save()
            return redirect("producto:productocategoria_list")
    else:
        form = forms.ProductoCategoriaForm(instance=query)
    return render(request, "producto/productocategoria_update.html", context={"form": form})


def productocategoria_delete(request, pk: int):
    query = models.ProductoCategoria.objects.get(id=pk)
    if request.method == "POST":
        query.delete()
        return redirect("producto:productocategoria_list")
    return render(request, "producto/productocategoria_delete.html", context={"producto": query})
