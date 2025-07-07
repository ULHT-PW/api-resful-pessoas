
from django.shortcuts import get_object_or_404
from ninja import NinjaAPI
from .models import Pessoa
from .schemas import PessoaIn, PessoaOut, ErrorSchema
from typing import List

api = NinjaAPI(
    title="API RESTful das Pessoas",
    description="API para gerir pessoas com operações completas sobre os dados",
    version="1.0.0",
)


# LISTAR
@api.get("pessoas/", response=List[PessoaOut])
def listar_pessoas(request):
    return Pessoa.objects.all()


@api.get("pessoas/{pessoa_id}/", 
         response={200: PessoaOut, 404: ErrorSchema})
def get_pessoa(request, pessoa_id: int):
    
    return 200, get_object_or_404(Pessoa, id=pessoa_id)
