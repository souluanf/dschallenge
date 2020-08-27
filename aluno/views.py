from rest_framework.generics import ListAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from .serializers import AlunoSerializer
from .models import Aluno


class PlaceListFilterByName(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AlunoSerializer
    queryset = Aluno.objects.all()

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Aluno.objects.none()

        nome = self.kwargs['nome']
        queryset = Aluno.objects.filter(nome=nome)
        return queryset


class PlaceListFilterByCPF(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AlunoSerializer
    queryset = Aluno.objects.all()

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Aluno.objects.none()

        cpf = self.kwargs['cpf']
        queryset = Aluno.objects.filter(cpf=cpf)
        return queryset


class PlaceListFilterByEmail(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AlunoSerializer
    queryset = Aluno.objects.all()

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Aluno.objects.none()

        email = self.kwargs['email']
        queryset = Aluno.objects.filter(email=email)
        return queryset


class PlaceViewSet(GenericViewSet,
                   mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):
    permission_classes = (IsAuthenticated,)
    serializer_class = AlunoSerializer
    queryset = Aluno.objects.all()
