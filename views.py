from django.shortcuts import render, redirect
from .models import Denuncia, Empresa
from .forms import DenunciaForm
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response


@login_required
def index(request):
    return render(request, 'denuncias/index.html')

@login_required
def lista_denuncias(request):
    denuncias = Denuncia.objects.all  
    context = {
        'denuncias': denuncias
    }
    return render(request, 'denuncias/lista_denuncias.html', context)

@login_required
def nova_denuncia(request):
    if request.method == 'POST':
        form = DenunciaForm(request.POST, request.FILES)
        if form.is_valid():
            denuncia = form.save(commit=False)
            denuncia.usuario = request.user  # Associa o usuário autenticado
            denuncia.save()
            return redirect('lista_denuncias')
    else:
        form = DenunciaForm()
    return render(request, 'denuncias/nova_denuncia.html', {'form': form})

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Esta é uma rota protegida!"})