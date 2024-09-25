from django.http import HttpResponse
from django.shortcuts import render

from .forms import MovieForm
from .models import MovieInfo

# Create your views here.


def create(request):
    form = MovieForm()
    if request.POST:
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
        # movie_info = MovieInfo(title=title, year=year, summary=summary)
        # movie_info.save()
    return render(request, 'create.html', {'frm': form})


def list(request):
    movie_data = MovieInfo.objects.all()
    print(movie_data)
    return render(request, 'list.html', {'movies': movie_data})


def edit(request):
    return render(request, 'edit.html')


# def print_hello(request):
#     name = {"name": "Arjun"}
#     movies = {
#         "movies": [
#             {
#                 'title': 'Deadpool and Woverine',
#                 'year': 2024
#             },
#              {
#                 'title': 'Deadpool and Woverine4 2',
#                 'year': 2025
#             }
#         ]
#     }
#     return render(request, 'hello.html', movies)
