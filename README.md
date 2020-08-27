<div align="center">
<a href="https://brazil.disys.com" target="_blank">
    <img src="https://brazil.disys.com/wp-content/uploads/2019/03/DISYS-logo-blue1.png" height="100px" alt="Disys"/>
</a>

<h3>Backend Developer Challenge</h3>

<a href="https://www.python.org" target="_blank">
  <img src="https://img.shields.io/badge/devel-Python-brightgreen" alt="Python"/>
</a>

<a href="https://travis-ci.com" target="_blank">
  <img src="https://img.shields.io/badge/ci-Travis-brightgreen" alt="Travis CI"/>
</a>

<a href="https://www.django-rest-framework.org" target="_blank">
  <img src="https://img.shields.io/badge/api-DRF-brightgreen" alt="Django Rest Framework"/>
</a>

<a href="https://www.djangoproject.com" target="_blank">
  <img src="https://img.shields.io/badge/main--framework-Django-brightgreen" alt="Django"/>
</a>

<a href="https://www.docker.com" target="_blank">
  <img src="https://img.shields.io/badge/deploy-Docker|Heroku-brightgreen" alt="Docker"/>
</a>

<a href="https://docs.conda.io/en/latest/miniconda.html" target="_blank">
  <img src="https://img.shields.io/badge/venv-Conda-brightgreen" alt="Conda"/>
</a>

<a href="https://docs.pytest.org/en/latest" target="_blank">
  <img src="https://img.shields.io/badge/coverage-PyTest-brightgreen" alt="PyTest"/>
</a>

<a href="https://opensource.org/licenses/MIT" target="_blank">
  <img src="https://img.shields.io/badge/license-MIT-brightgreen" alt="MIT"/>
</a>

</div>

## TL;DR
##### Front End da Aplicação: https://dschallenge.herokuapp.com/
##### Documentação da API  com Postman : https://documenter.getpostman.com/view/10016660/Szf54V1F?version=latest
##### Teste de Integração Contínua: https://travis-ci.com/github/souluanf/dschallenge
##### Repositório Github: https://github.com/souluanf/dschallenge

## Execução local
### Obtendo o código

```
$ git clone https://github.com/souluanf/dschallenge.git
```

### 1 - Utilizando o Docker
<pre>
$ cd < path/diretório/clonado >
$ docker build . -t dschallenge
$ docker run -d -p 8030:8030 dschallenge
</pre>
Aponte o browser para http://localhost:8030

### 2 -  Sem a utilização do docker

Crie um ambiente virtual com seu gerenciador favorito (conda, pyenv, virtualenv, etc);

Ative o ambiente criado e instale as dependências
<pre><code> $ pip install -r requirements.txt </code></pre>

Execute o servidor com o comando:

<pre><code> $ python manager.py runserver </code></pre>

Aponte o browser para http://localhost:8000

###  Credenciais padrão
<table>
    <thead>
        <tr class="table100-head">
            <th class="column1">USER</th>
            <th class="column2">PASSWORD</th>
        </tr>
    </thead>
    <tbody>
            <tr>
                <td class="column1">test</td>
                <td class="column2">dstest1234</td>
            </tr>
    </tbody>
</table>


##Cobertura (Pytest)

Em função do tempo a opção foi fazer o minimo de teste possível somente para demonstrar a técnica.
O pacote utilizado para o testes foi o pytest: https://docs.pytest.org/en/latest/
