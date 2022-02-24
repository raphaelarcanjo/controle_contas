from django.shortcuts import redirect, render
from django.contrib import messages
from contas.models import Contas


def index(request):
    contas = Contas.objects.all()

    data = {
        'title': "Home",
        'contas': contas
    }

    return render(request, 'index.html', data)

def conta(request, conta_id=None):
    conta = None

    if request.method == 'POST':
        conta = Contas(
            id = request.POST['id'] or None,
            titulo = request.POST['titulo'],
            valor = request.POST['valor'],
            data_vencimento = request.POST['vencimento'],
            data_pagamento = request.POST['pagamento'] or None,
            recorrente = True if 'recorrente' in request.POST else False,
            paga = True if 'paga' in request.POST else False,
        )
        try:
            conta.save()
            return redirect('index')
        except Exception as err:
            messages.error(request, 'Ocorreu um erro ao tentar salvar')
            print(err)
            return redirect('/conta/' + request.POST['id'])

    if conta_id:
        conta = Contas.objects.get(id=conta_id)

    data = {
        'title': "Criar",
        'conta': conta
    }

    return render(request, 'conta.html', data)

def excluir(request, conta_id):
    try:
        Contas.objects.filter(id=conta_id).delete()
    except Exception as err:
        messages.error(request, 'Ocorreu um erro ao tentar excluir')
        print(err)
    return redirect('index')

def marcar_paga(request, conta_id):
    conta = Contas.objects.filter(id=conta_id).values().get()
    alterar_paga = not conta['paga']
    try:
        Contas.objects.filter(id=conta_id).update(paga=alterar_paga)
    except Exception as err:
        messages.error(request, 'Ocorreu um erro ao tentar salvar')
        print(err)
    return redirect('index')