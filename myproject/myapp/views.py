from django.shortcuts import render, redirect
from myapp.models import Colaborador




def frente(request):
    return render(request, 'myapp/globals/frente.html')

def cadastrar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        cargo = request.POST.get('cargo')
        telefone = request.POST.get('telefone')
        if nome and cpf and cargo and telefone:
            Colaborador.objects.create(
                nome=nome,
                cpf=cpf,
                cargo=cargo,
                telefone=telefone
            )
            return redirect(colaboradores)

    
    return render(request, 'myapp/globals/cadastrar.html') 

def atualizar(request):
    return render(request, 'atualizar.html')

def colaboradores(request):
    colaborador = Colaborador.objects.all()
    return render(request, 'myapp/globals/colaboradores.html', {"colaboradores":colaborador})