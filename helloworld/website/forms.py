from helloworld.models import Funcionario

from django import forms 

class InsereFuncionarioForm(forms.ModelForm): 

    # chefe = forms.BooleanField(
    # label='Chefe?',
    # required=True,
    # )

    # biografia = forms.CharField(
    #     label = 'Biografia',
    #     required = False,
    #     widget = forms.TextArea
    # )

    class Meta: 
        model = Funcionario 

        fields = [
        'nome',
        'sobrenome',
        'cpf',
        'tempo_de_servico',
        'remuneracao',
        'tempo_de_servico'
        ]

        exclude = [
            
        ]



