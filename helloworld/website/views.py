from django.urls import reverse_lazy

from django.shortcuts import render
from helloworld.models import Funcionario  

from django.views.generic import TemplateView
from django.views.generic import ListView 
from django.views.generic import UpdateView 
from django.views.generic import CreateView
from django.views.generic import DeleteView

from website.forms import InsereFuncionarioForm


# Create your views here.

class IndexTemplateView(TemplateView):
    template_name = "website/index.html" 

class FuncionarioListView(ListView):
    template_name = "website/lista.html"
    model = Funcionario
    context_object_name = "funcionarios" 

# class FuncionarioUpdateView(UpdateView):
#     template_name = "atualiza.html" 
#     model = Funcionario
#     fields = [
#         'nome',
#         'sobrenome',
#         'cpf',
#         'tempo_de_servico',
#         'remuneracao'
#     ]

class FuncionarioUpdateView(UpdateView):
    template_name="website/atualiza.html"
    model = Funcionario
    fields = '__all__'
    context_object_name = 'funcionario'
    success_url = reverse_lazy("website:lista_funcionarios")


    def get_object(self,queryset=None):
        funcionario = None

        pk = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg) 

        if pk is not None:
            # Busca pelo ID
            funcionario = Funcionario.objetos.filter(pk=pk).first()

        elif slug is not None:
            # pega o slug do Model
            campo_slug = self.get_slug_field() 

            # Busca pelo slug 
            funcionario = Funcionario.objetos.filter(**{campo_slug:slug}).first()

        return funcionario

class FuncionarioDeleteView(DeleteView):
    template_name = "website/exclui.html" 
    model = Funcionario 
    context_object_name = 'funcionario' 
    success_url = reverse_lazy("website:lista_funcionarios")

class FuncionarioCreateView(CreateView):
    template_name="website/cria.html"
    model = Funcionario
    form_class = InsereFuncionarioForm
    success_url = reverse_lazy("website:lista_funcionarios")



