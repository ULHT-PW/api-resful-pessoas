from ninja import NinjaAPI
from .models import Pessoa
from .schemas import PessoaIn, PessoaOut, ErrorSchema
from typing import List
from django.shortcuts import get_object_or_404


api = NinjaAPI(
    title="API RESTful das Pessoas",
    description="API para gerir pessoas, com operações completas sobre os dados",
    version="1.0.0"
)


# LISTAR RECURSOS

# Metodo HTTP: GET
# endpoint: pessoas/
# status possiveis: 
# - 200 OK

@api.get(
        'pessoas/', 
        response=List[PessoaOut],
        tags=["Pessoas"],
        description="Lista todas as pessoas"
)
def lista_pessoas(request, sort: str = None, idade: int = None, nome: str = None):
    
    pessoas = Pessoa.objects.all()
    
    if sort in ('nome', 'idade', '-nome', '-idade'):
        pessoas = pessoas.order_by(sort)

    if idade:
        pessoas = pessoas.filter(idade=idade)

    if nome:
        pessoas = pessoas.filter(nome__icontains=nome)

    return pessoas # por omissão, retorna status 200




# BUSCAR UM RECURSO

# Metodo HTTP: GET
# endpoint: pessoas/{id}
# status possiveis: 
# - 200 OK
# - 404 Not Found 

@api.get(
    "pessoas/{id}",
    response= {
        200:PessoaOut,
        404:ErrorSchema
    },
    tags=["Pessoas"]
)
def buscar_pessoa(request, id:int):
    return 200, get_object_or_404(Pessoa, id=id)


# CRIAR NOVO RECURSO

# Metodo HTTP: POST
# endpoint: pessoas/
# status possiveis: 
# - 201 Created
# - 400 Bad request

@api.post(
    "pessoas/",
    response={
        201: PessoaOut,
        400: ErrorSchema
    },
    tags=["Pessoas"]
)
def criar_pessoa(request, data: PessoaIn):
    pessoa = Pessoa.objects.create(**data.dict())
    return 201, pessoa 



# SUBSTITUIR RECURSO

# Metodo HTTP: PUT
# endpoint: pessoas/{id}
# status possiveis: 
# - 200 OK
# - 400 Bad request
# - 404 Not Found

@api.put(
    "pessoas/{id}",
    response={
        200:PessoaOut,
        400:ErrorSchema,
        404:ErrorSchema
    },
    tags=["Pessoas"]
)
def substituir_dados_pessoa(request, id:int, data:PessoaIn):
    pessoa = get_object_or_404(Pessoa, id=id)
    # pessoa.nome = data.nome
    # pessoa.idade = data.idade

    for atributo, valor in data.dict().items():
        setattr(pessoa, atributo, valor)

    pessoa.save()

    return 200, pessoa


# APAGAR 

# Metodo HTTP: DELETE
# endpoint: pessoas/{id}
# status possiveis: 
# - 204 No Content
# - 404 Not Found

@api.delete(
    "pessoas/{id}",
    response={
        204:None,
        404:ErrorSchema
    },
    tags=["Pessoas"]
)
def apaga_pessoa(request, id:int):
    pessoa = get_object_or_404(Pessoa, id=id)
    pessoa.delete()

    return 204, None
