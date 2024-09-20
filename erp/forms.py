from django import forms

from erp.models import Funcionario, Produto


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'
        labels = {
            'remuneracao': 'Remuneração',
            'cpf': 'CPF'
        }
        # fields = [
        #     'nome',
        #     'sobrenome',
        #     'cpf',
        #
        # ]


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
        labels = {
            'descricao': 'Descrição',
            'preco': 'Preço'
        }
