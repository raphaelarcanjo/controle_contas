from django.urls import path
from contas import views

urlpatterns = [
    path('', views.index, name='index'),
    path('conta', views.conta, name='criar_conta'),
    path('conta/<int:conta_id>', views.conta, name='atualizar_conta'),
    path('excluir/<int:conta_id>', views.excluir, name='excluir_conta'),
    path('paga/<int:conta_id>', views.marcar_paga, name='marcar_paga'),
]