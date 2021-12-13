#

from . import views
from django.urls import path 
from django.views.generic import TemplateView 
from website.views import IndexTemplateView
from website.views import FuncionarioListView
from website.views import FuncionarioDeleteView
from website.views import FuncionarioCreateView
from website.views import FuncionarioUpdateView



app_name = 'website' 

# urlpatterns = [
#     # path('funcionarios/<int:ano>/', views.funcionarios_por_ano),
# ]

urlpatterns = [
    # path('', TemplateView.as_view(template_name="index.html")),
    path('', IndexTemplateView.as_view(), name="index"),

    path('funcionario/cadastrar', FuncionarioCreateView.as_view(),name="cadastra_funcionario"),
    
    path('funcionarios/', FuncionarioListView.as_view(),name="lista_funcionarios"),

    # {id} para busca
    path('funcionario/<pk>', FuncionarioUpdateView.as_view(),name="atualiza_funcionario"),
    # {slug} para busca 
    # path('funcionario/<slug>', FuncionarioUpdateView.as_view()),
    path('funcionario/excluir/<pk>', FuncionarioDeleteView.as_view(),name="deleta_funcionario"),
    
] 

