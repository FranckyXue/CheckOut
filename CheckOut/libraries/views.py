# Create your views here.
from urllib import request

from django.shortcuts import render, get_object_or_404
from .models import Library
from django.core.paginator import Paginator

def library_list(request):
    library_list = Library.objects.all().order_by('BRANCH')  # 添加.order_by('BRANCH')
    print(library_list)
    paginator = Paginator(library_list, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'libraries/index.html', {'page_obj': page_obj})


def library_detail(request, library_id):
    library = get_object_or_404(Library, pk=library_id)
    return render(request, 'libraries/library_detail.html', {'library': library})
