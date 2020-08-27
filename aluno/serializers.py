from rest_framework import serializers
from aluno.models import Aluno


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = (
            'id', 'nome', 'sobrenome', 'sexo', 'cpf', 'email', 'telefone', 'nascimento', 'rua', 'numero', 'bairro',
            'cidade', 'uf', 'cep')

    def create(self, validated_data):
        place = Aluno.objects.create(**validated_data)
        return place
