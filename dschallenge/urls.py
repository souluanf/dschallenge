from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include, re_path
from dschallenge.views import ReadMeView
from aluno.views import PlaceListFilterByName, PlaceListFilterByCPF, PlaceListFilterByEmail, PlaceViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Disys Test :: By Luan 2020",
        default_version='v1',
        description="""O teste consiste em criar endpoints para: criar, listar, alterar, remover e filtrar estudantes;. 
      """,
        contact=openapi.Contact(email="souluan@live.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register('alunos', PlaceViewSet, basename='alunos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='place/login3.html'), name='login'),
    path('', ReadMeView.as_view(), name='home'),
    path('readme/', ReadMeView.as_view(), name='readme'),
    path('api/auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('api/v1.0/', include((router.urls, 'api-root'), namespace='api-root')),
    path('api/v1.0/alunos/busca/nome/<str:nome>', PlaceListFilterByName.as_view(), name='busca-nome'),
    path('api/v1.0/alunos/busca/cpf/<str:cpf>', PlaceListFilterByCPF.as_view(), name='busca-cpf'),
    path('api/v1.0/alunos/busca/email/<str:email>', PlaceListFilterByEmail.as_view(), name='busca-email'),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

admin.site.site_header = "Disys Test Admin"
admin.site.site_title = "Disys Test Admin Portal"
admin.site.index_title = "Bem vindo(a) a Disys Test"
