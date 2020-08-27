from django.contrib import admin
from aluno.models import Aluno


@admin.register(Aluno)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_nome_completo', 'cpf', 'email', 'telefone', 'get_endereco', 'criado_em', 'atualizado_em')
    list_filter = ('nome', 'email', 'cpf')

    def get_nome_completo(self, obj):
        return f'{obj.nome} {obj.sobrenome}'

    get_nome_completo.short_description = 'nome completo'

    def get_endereco(self, obj):
        return f'{obj.rua},{obj.numero}, {obj.bairro}, {obj.cidade} - {obj.uf}, {obj.cep}'

    get_endereco.short_description = 'endereço'
