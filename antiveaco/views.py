from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Divida
from .forms import DividaForm

# View para LISTAR e BUSCAR todas as dívidas
def lista_dividas(request):
    busca = request.GET.get('busca')
    dividas = Divida.objects.all()
    if busca:
        dividas = dividas.filter(
            Q(cliente__nome__icontains=busca) |
            Q(cliente__cpf__icontains=busca) |
            Q(status__icontains=busca)
        )
    context = {'dividas': dividas}
    return render(request, 'divida/lista_dividas.html', context)

# View para ADICIONAR uma nova dívida
def adicionar_divida(request):
    if request.method == 'POST':
        form = DividaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dívida cadastrada com sucesso!')
            return redirect('lista_dividas')
    else:
        form = DividaForm()

    context = {'form': form}
    return render(request, 'divida/cadastrar_divida.html', context)

# View para EDITAR uma dívida existente
def editar_divida(request, cod_divida):
    divida = get_object_or_404(Divida, pk=cod_divida)
    if request.method == 'POST':
        form = DividaForm(request.POST, instance=divida)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dívida atualizada com sucesso!')
            return redirect('lista_dividas')
    else:
        form = DividaForm(instance=divida)

    context = {'form': form, 'divida': divida}
    return render(request, 'divida/cadastrar_divida.html', context)

# View para DELETAR uma dívida
def deletar_divida(request, cod_divida):
    divida = get_object_or_404(Divida, pk=cod_divida)
    if request.method == 'POST':
        divida.delete()
        messages.success(request, 'Dívida excluída com sucesso!')
        return redirect('lista_dividas')

    context = {'divida': divida}
    return render(request, 'divida/confirmar_exclusao.html', context)