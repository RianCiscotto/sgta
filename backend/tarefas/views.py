from django.shortcuts import render

# Create your views here.
from .models import Tarefa
from django.http import JsonResponse


def listar_tarefas(request):
    tarefas = Tarefa.objects.all().values()
    return JsonResponse(list[any](tarefas), safe=False)

