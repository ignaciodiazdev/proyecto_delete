from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models, forms
# Create your views here.


def home(request):
    return render(request, "producto/index.html")

# LIST
# def productocategoria_list(request):
#     consulta = request.GET.get("consulta", None)
#     if consulta:
#         print(consulta)
#         query = models.ProductoCategoria.objects.filter(
#             nombre__icontains=consulta)
#     else:
#         query = models.ProductoCategoria.objects.all()
#     context = {"productos": query}
#     return render(request, "producto/productocategoria_list.html", context)


class ProductoCategoriaList(ListView):
    model = models.ProductoCategoria
    # context_object_name = "productos"
    # template_name = "producto/productocategoria___list.html"

    def get_queryset(self) -> QuerySet:
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.ProductoCategoria.objects.filter(
                nombre__icontains=consulta)
            return object_list
        else:
            object_list = models.ProductoCategoria.objects.all()
            return object_list
    # NOTA:
    # 1) Por defecto el ListView busca el template que tenga el mismo nombre de la clase y agregado el "_list", osea que no es necesario poner el url, a no ser que quieras personalizarse y ahí se usa el template_name
    # 2) Por defecto el ListView manda el contexto con valor de nombre "object_list"

# CREATE
# def productocategoria_create(request):

#     if request.method == "POST":
#         form = forms.ProductoCategoriaForm(request.POST)
#         if form.is_valid:
#             form.save()
#             return redirect("producto:home")
#     else:
#         form = forms.ProductoCategoriaForm()
#     return render(request, "producto/productocategoria_create.html", context={"form": form})


class ProductoCategoriaCreate(CreateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    success_url = reverse_lazy("producto:home")

# UPDATE
# def productocategoria_update(request, pk: int):
#     query = models.ProductoCategoria.objects.get(id=pk)
#     if request.method == "POST":
#         form = forms.ProductoCategoriaForm(request.POST, instance=query)
#         if form.is_valid:
#             form.save()
#             return redirect("producto:productocategoria_list")
#     else:
#         form = forms.ProductoCategoriaForm(instance=query)
#     return render(request, "producto/productocategoria_update.html", context={"form": form})


class ProductoCategoriaUpdate(UpdateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")

# DETAIL
# def productocategoria_detail(request, pk: int):
#     query = models.ProductoCategoria.objects.get(id=pk)
#     return render(request, "producto/productocategoria_detail.html", context={"producto": query})


class ProductoCategoriaDetail(DetailView):
    model = models.ProductoCategoria
    # context_object_name = "producto"


# DELETE
# def productocategoria_delete(request, pk: int):
#     query = models.ProductoCategoria.objects.get(id=pk)
#     if request.method == "POST":
#         query.delete()
#         return redirect("producto:productocategoria_list")
#     return render(request, "producto/productocategoria_delete.html", context={"producto": query})


class ProductoCategoriaDelete(LoginRequiredMixin, DeleteView):
    model = models.ProductoCategoria
    # template_name = "producto/productocategoria_delete.html"
    success_url = reverse_lazy("producto:productocategoria_list")
    # NOTA:
    # 1) Por defecto el DeleteView busca el template que tenga el mismo nombre de la clase y agregado el "_confirm_delete.html"
