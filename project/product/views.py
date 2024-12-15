from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product
from .filters import ProductFilter
from .forms import ProductForm, ProductCrForm
from .models import News
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductsList(ListView):
    model = Product
    # Поле, которое будет использоваться для сортировки объектов
    ordering = 'name'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'products.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'products'
    paginate_by = 12


class ProductSearch(ListView):
    model = Product
    ordering = 'name'
    template_name = 'search.html'
    context_object_name = 'products'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class ProductDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Product
    # Используем другой шаблон — product.html
    template_name = 'product.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'product'


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        form.save()
        return HttpResponseRedirect('/products')

    form = ProductForm()
    return render(request, 'product_edit.html', {'form': form})


# Добавляем новое представление для создания товаров.
class ProductCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    # Указываем нашу разработанную форму
    form_class = ProductCrForm
    # модель товаров
    model = Product
    # и новый шаблон, в котором используется форма.
    template_name = 'product_create.html'
    success_url = reverse_lazy('product_list')


class ProductUpdate(LoginRequiredMixin, UpdateView):
    raise_exception = True
    form_class = ProductForm
    model = Product
    template_name = 'product_edit.html'


class ProductDelete(LoginRequiredMixin, DeleteView):
    raise_exception = True
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')


class News(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = News
    # Поле, которое будет использоваться для сортировки объектов
    ordering = 'name'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'default.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'news'


class NewsDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = News
    # Используем другой шаблон — product.html
    template_name = 'product.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'news'


def news(request):
    return render(request, 'flatpages/news.html')



