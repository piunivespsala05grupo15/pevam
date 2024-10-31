from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Policial, Local, Hospital
from .forms import PolicialForm, ContatoEmergenciaForm

def home(request):
    return render(request, 'sections/home.html')

@csrf_exempt
def policial(request):
    if request.method == 'POST':
        form_data = request.POST
        policial = Policial(
            numero_registro=form_data['numero_registro'],
            nome=form_data['nome'],
            lotacao=form_data['lotacao'],
            tipo_sanguineo=form_data['tipo_sanguineo'],
            plano_saude=form_data['plano_saude'],
            numero_plasau=form_data['numero_plasau']
        )
        policial.save()

        return JsonResponse({'status': 'success', 'policial_id': policial.id})    
    return render(request, 'sections/policial.html')

@csrf_exempt
def contato_emergencia(request):
    if request.method == 'POST':
        policial_id = request.POST.get('policial_id')
        
        if not policial_id:
            return JsonResponse({'status': 'error', 'message': 'Cadastro ID não enviado.'})

        try:
            policial = Policial.objects.get(id=policial_id)
        except Policial.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Cadastro não encontrado.'})

        form = ContatoEmergenciaForm(request.POST)
        
        if form.is_valid():
            contato_emergencia = form.save(commit=False)
            contato_emergencia.policial = policial
            contato_emergencia.save()
            return JsonResponse({'status': 'success', 'message': 'Contato de emergência cadastrado com sucesso!'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Dados incompletos ou inválidos.'})

    return JsonResponse({'status': 'error', 'message': 'Método inválido.'})

def local(request):
    if request.method == "POST":
        logradouro = request.POST.get("logradouro")
        numero = request.POST.get("numero")
        complemento = request.POST.get("complemento", "")
        bairro = request.POST.get("bairro")
        cidade = request.POST.get("cidade")
        cep = request.POST.get("cep")
        latitude = request.POST.get("latitude")
        longitude = request.POST.get("longitude")

        local = Local(
            logradouro=logradouro,
            numero=numero,
            complemento=complemento,
            bairro=bairro,
            cidade=cidade,
            cep=cep,
            latitude=float(latitude),
            longitude=float(longitude)
        )
        local.save()

        return JsonResponse({"success": True, "message": "Endereço salvo com sucesso!"})
    else:
        return render(request, 'sections/local.html')
    
from django.http import JsonResponse
from .models import Hospital

def hospital(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        logradouro = request.POST.get("logradouro")
        numero = request.POST.get("numero")
        complemento = request.POST.get("complemento", "")
        bairro = request.POST.get("bairro")
        cidade = request.POST.get("cidade")
        cep = request.POST.get("cep")
        latitude = request.POST.get("latitude")
        longitude = request.POST.get("longitude")
        telefone = request.POST.get("telefone")

        hospital = Hospital(
            nome=nome,
            logradouro=logradouro,
            numero=numero,
            complemento=complemento,
            bairro=bairro,
            cidade=cidade,
            cep=cep,
            latitude=float(latitude),
            longitude=float(longitude),
            telefone=telefone
        )
        hospital.save()

        return JsonResponse({"success": True, "message": "Hospital salvo com sucesso!"})
    else:
        return render(request, 'sections/hospital.html')
