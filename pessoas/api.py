from django.shortcuts import get_object_or_404
from ninja import NinjaAPI, Query
from .models import Pessoa
from .schemas import PessoaIn, PessoaOut, ErrorSchema
from typing import List, Optional

api = NinjaAPI(
    title="API RESTful Pessoas",
    description="API para gestão de pessoas com operações completas sobre os dados.",
    version="1.0.0",
    urls_namespace='pessoas'
)


# listar
@api.get("pessoas/", 
         response={200: List[PessoaOut]}, 
         tags=["Pessoas"], 
         description="Lista todas as pessoas")
def listar_pessoas(request,  
                 sort: str = None, 
                 idade: int = None,
                 nome: str = None,
                 offset: int = 0,
                 limit: int = 3 ):
    
    pessoas = Pessoa.objects.all()[offset:offset+limit]
    
    if idade:
        pessoas = pessoas.filter(idade=idade)

    if nome:
        pessoas = pessoas.filter(nome__icontains=nome)

    if sort in ('nome', 'idade', '-nome', '-idade'):
        pessoas.order_by(sort)
    
    return 200, pessoas


# ver um
@api.get("pessoas/{pessoa_id}/", 
         response={200: PessoaOut}, 
         tags=["Pessoas"],
         description="Ver dados de uma pessoa"
         )
def ver_uma_pessoa(request, pessoa_id:int):
    return 200, get_object_or_404(Pessoa, id=pessoa_id)
    

# criar
@api.post("pessoas/", 
          response={201: PessoaOut}, 
          tags=["Pessoas"],
          description="Criar uma nova pessoa")
def criar_uma_pessoa(request, data: PessoaIn):
    return 201, Pessoa.objects.create(**data.dict())


# atualizar
@api.put("pessoas/{pessoa_id}/", 
         response=PessoaOut, 
         tags=["Pessoas"],
         description="Substituir os dados duma pessoa")
def atualizar_uma_pessoa(request, pessoa_id: int, data: PessoaIn):
    pessoa = Pessoa.objects.filter(id=pessoa_id).update(**data.dict())   # update é de QuerySet, pelo que devemos usar filter
    return Pessoa.objects.get(id=pessoa_id)


# apagar
@api.delete("pessoas/{pessoa_id}/", 
         response={204: None, 404: ErrorSchema}, 
         tags=["Pessoas"],
         description="Apagar uma pessoa")
def apagar_uma_pessoa(request, pessoa_id: int):

    pessoa = get_object_or_404(Pessoa, id=pessoa_id)
    pessoa.delete()
    return 204, None


