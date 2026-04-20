from django.shortcuts import render
from .models import Tarefa
from django.http import JsonResponse

def listar_tarefas(request):
    tarefas = Tarefa.objects.all().values(
        'titulo',
        'status',
        'descricao',
        'data_criacao',
        'data_entrega',
        'usuario_responsavel__nome' 
    )
    return JsonResponse(list(tarefas), safe=False)


