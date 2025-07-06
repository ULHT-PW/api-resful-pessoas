from django.shortcuts import get_object_or_404
from ninja import NinjaAPI
from .models import Pessoa
from .schemas import PessoaIn, PessoaOut
from typing import List

api = NinjaAPI()

# LISTAR
@api.get("pessoas/", response=List[PessoaOut])
def listar_pessoas(request):
    return Pessoa.objects.all()


# VER UMA
@api.get("pessoas/{id}/", response=PessoaOut)
def ver_uma_pessoa(request, id: int):
    pessoa = get_object_or_404(Pessoa, id=id)
    return pessoa


# CRIAR
@api.post("pessoas/", response=PessoaOut)
def criar_uma_pessoa(request, data: PessoaIn):
    pessoa = Pessoa.objects.create(**data.dict())
    return 201, pessoa


# ATUALIZAR
@api.put("pessoas/{id}/", response=PessoaOut)
def atualizar_uma_pessoa(request, id: int, data: PessoaIn):
    pessoa = get_object_or_404(Pessoa, id=id)
    for attr, value in data.dict().items():
        setattr(pessoa, attr, value)
    pessoa.save()
    return pessoa


# APAGAR
@api.delete("pessoas/{id}/")
def apagar_uma_pessoa(request, id: int):
    pessoa = get_object_or_404(Pessoa, id=id)
    pessoa.delete()
    return 204, None
