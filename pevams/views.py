from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Policial, Local, Hospital
from .forms import PolicialForm, ContatoEmergenciaForm
from .geocoding import get_geocode

from django.http import HttpResponse
import qrcode
import io
import base64


def home(request):
    return render(request, 'sections/home.html', {'is_homepage': True})

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
    return render(request, 'sections/policial.html', {'is_homepage': False})

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
        return render(request, 'sections/local.html', {'is_homepage': False})
    
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
        return render(request, 'sections/hospital.html', {'is_homepage': False})


def criar_pevam(request):
    if request.method == 'POST':
        endereco = request.POST.get('endereco')
        policiais_ids = request.POST.getlist('policiais')
        policiais = Policial.objects.filter(id__in=policiais_ids)

        # Obter coordenadas a partir do endereço
        lat, lng = get_geocode(endereco)
        
        if not policiais.exists():
            return render(request, 'sections/criar_pevam.html', {
                'policiais': Policial.objects.all(),
                'selected_policiais': policiais_ids,
                'error_message': 'Por favor, selecione pelo menos um policial para a operação.',
                'is_homepage': False,
            })
            
        if lat is None or lng is None:
            return render(request, 'criar_pevam.html', {
                'policiais': policiais,
                'error_message': 'Não foi possível encontrar as coordenadas para o endereço fornecido. Por favor, verifique o endereço e tente novamente.',
                'is_homepage': False,
            })

        hospitais = Hospital.objects.all()
        
        if not hospitais.exists():
            return render(request, 'sections/criar_pevam.html', {
                'policiais': policiais,
                'error_message': 'Não há hospitais cadastrados no sistema. Por favor, cadastre pelo menos um hospital antes de continuar.',
                'is_homepage': False,
            })
            
        menor_distancia = None
        hospital_proximo = None
        for hospital in hospitais:
            distancia = calcular_distancia(lat, lng, hospital.latitude, hospital.longitude)
            if menor_distancia is None or distancia < menor_distancia:
                menor_distancia = distancia
                hospital_proximo = hospital
        
        maps_link = f'https://www.google.com/maps/dir/?api=1&origin={lat},{lng}&destination={hospital_proximo.latitude},{hospital_proximo.longitude}'
        
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(maps_link)
        qr.make(fit=True)
        img = qr.make_image(fill_color='black', back_color='white')
        buffer = io.BytesIO()
        img.save(buffer, format='PNG')
        qr_code_image = base64.b64encode(buffer.getvalue()).decode('utf-8')

        return render(request, 'sections/resultado.html', {
            'qr_code_image': qr_code_image,
            'hospital': hospital_proximo,
            'policiais': policiais,
            'maps_link': maps_link,
            'is_homepage': False,
        })

    else:
        policiais = Policial.objects.all()
        return render(request, 'sections/criar_pevam.html', {'policiais': policiais, 'selected_policiais': [], 'is_homepage': False})

def calcular_distancia(lat1, lng1, lat2, lng2):
    from math import radians, cos, sin, asin, sqrt
    # Converter graus para radianos
    lat1, lng1, lat2, lng2 = map(radians, [lat1, lng1, lat2, lng2])

    # Fórmula de Haversine
    dlat = lat2 - lat1
    dlng = lng2 - lng1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlng / 2) ** 2
    c = 2 * asin(sqrt(a))
    km = 6371 * c  # Raio médio da Terra em quilômetros
    return km