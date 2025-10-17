from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from .models import Cliente, Divida, Pagamento
from .forms import DividaForm

import json

def get_dividas(request):
    dividas = Divida.objects.all()

    cpf = request.GET.get('cpf_cliente')
    status = request.GET.get('status')
    valor_min = request.GET.get('valor_min')
    valor_max = request.GET.get('valor_max')

    if cpf:
        dividas = dividas.filter(cliente__cpf__icontains=cpf)
    if status:
        dividas = dividas.filter(status=status)
    if valor_min:
        dividas = dividas.filter(valor__gte=valor_min)
    if valor_max:
        dividas = dividas.filter(valor__lte=valor_max)

    return render(request, 'divida/pesquisar_divida.html', {'dividas': dividas})

def divida_manager(request, cod_divida=None):
    divida = None
    template = 'divida/cadastrar_divida.html'

    if cod_divida:
        divida = get_object_or_404(Divida, pk=cod_divida)
        if 'excluir' in request.POST and divida:
            divida.delete()
            messages.success(request, 'Dívida excluída com sucesso!')
            return redirect('pesquisar_divida')
        template = 'divida/atualizar_divida.html'
        
    if request.method == 'POST':
        form = DividaForm(request.POST, instance=divida)
        if form.is_valid():
            form.save()
            if divida:
                messages.success(request, 'Dívida atualizada com sucesso!')
                return redirect('pesquisar_divida')
            else:
                messages.success(request, 'Dívida cadastrada com sucesso!')
                return redirect('pesquisar_divida')
        else:
            return render(request, template, {
                'form': form,
                'erro': 'Erro ao salvar os dados.',
                'divida': divida
            })
    else:
        if divida:
            template = 'divida/atualizar_divida.html'
    
    form = DividaForm(instance=divida)
    return render(request, template, {
        'form': form,
        'divida': divida
    })

# Funções que apenas exibem páginas, sem lógica de CRUD
def index(request):
    return render(request, 'index.html')

def index_divida(request):
    return render(request, 'divida/index_divida.html')