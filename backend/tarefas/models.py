from django.db import models

# Create your models here.

    
class Tarefa(models.Model):
    STATUS_CHOICES = [
        {'ABERTA','Aberta'},
        {'EM_ANDAMENTO','Em andamento'},
        {'CONCLUIDA','Concluída'},
        {'CANCELADA','Cancelada'},
        {'URGENTE','Urgente'},
        {'NAO_URGENTE','Cancelada'},
    ]
    
    titulo = models.CharField(max_length=255)
    
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices = STATUS_CHOICES, default='ABERTA')
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_entrega = models.DateField()
    usuario_responsavel = models.ForeignKey(
        'usuarios.Usuario', 
        on_delete=models.SET_NULL,  
        null=True, 
        blank=True, 
        related_name='usuarios'
        
)
    
    def __str__(self):
        return self.titulo
    
    
    


    
    