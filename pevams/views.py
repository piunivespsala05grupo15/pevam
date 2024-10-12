from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Cadastro, ContatoEmergencia, Lotacao
from .forms import CadastroForm, ContatoEmergenciaForm, EventoCritico, LotacaoForm

def home(request):
    return render(request, 'sections/home.html')

@csrf_exempt
def cadastro(request):
    if request.method == 'POST':
        form_data = request.POST
        cadastro = Cadastro(
            numero_registro=form_data['numero_registro'],
            nome=form_data['nome'],
            lotacao=form_data['lotacao'],
            tipo_sanguineo=form_data['tipo_sanguineo'],
            plano_saude=form_data['plano_saude']
        )
        cadastro.save()

        return JsonResponse({'status': 'success', 'cadastro_id': cadastro.id})
    
    # Para o método GET, renderiza o template de cadastro
    return render(request, 'sections/cadastro.html')  # Substitua pelo caminho correto do seu template

@csrf_exempt
def contato_emergencia(request):
    if request.method == 'POST':
        cadastro_id = request.POST.get('cadastro_id')
        
        if not cadastro_id:
            return JsonResponse({'status': 'error', 'message': 'Cadastro ID não enviado.'})

        try:
            cadastro = Cadastro.objects.get(id=cadastro_id)  # Busca o agente (Cadastro) pelo ID
        except Cadastro.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Cadastro não encontrado.'})

        form = ContatoEmergenciaForm(request.POST)
        
        if form.is_valid():
            contato_emergencia = form.save(commit=False)
            contato_emergencia.cadastro = cadastro  # Relaciona o contato de emergência ao agente
            contato_emergencia.save()
            return JsonResponse({'status': 'success', 'message': 'Contato de emergência cadastrado com sucesso!'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Dados incompletos ou inválidos.'})

    return JsonResponse({'status': 'error', 'message': 'Método inválido.'})

class CadastrarEventoCritico(View):
    def get(self, request):
        return render(request, 'sections/cadastrar_evento_critico.html')

    def post(self, request):
        tipo_evento = request.POST.get('tipo_evento')

        if tipo_evento:
            evento_critico = EventoCritico(tipo_evento=tipo_evento)
            evento_critico.save()
            return JsonResponse({'status': 'success', 'message': 'Evento crítico cadastrado com sucesso!'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Tipo de evento não selecionado.'})
        

def cadastrar_lotacao(request):
    if request.method == 'POST':
        form = LotacaoForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o formulário no banco de dados
            return JsonResponse({'status': 'success', 'message': 'Lotação cadastrada com sucesso!'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    else:
        form = LotacaoForm()

    return render(request, 'sections/cadastrar_lotacao.html', {'form': form})