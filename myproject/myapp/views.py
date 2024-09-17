from django.shortcuts import render, redirect





def frente(request):
    return render(request, 'myapp/globals/frente.html')

def cadastrar(request):
    
    
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        cargo = request.POST.get('cargo')
        telefone = request.POST.get('telefone')
        print(nome, cpf, cargo, telefone)
        if nome and cpf and cargo and telefone:
            colaboradores.objects.create(
                nome=nome,
                cpf=cpf,
                cargo=cargo,
                telefone=telefone
                
            )
            print(nome, cpf, cargo, telefone)
            return redirect('colaboradores')

    
    return render(request, 'myapp/globals/cadastrar.html') 

def atualizar(request):
    return render(request, 'atualizar.html')

def colaboradores(request):
    colaboradores[0] = {"nome": "Joaquim","cpf": "543.321.156.23","cargo": "servente","telefone": "(49) 91359-1461"}
    return render(request, 'myapp/globals/colaboradores.html', {"colaboradores":colaboradores})