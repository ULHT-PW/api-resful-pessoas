
from django.shortcuts import get_object_or_404
from ninja import NinjaAPI
from .models import Pessoa
from .schemas import PessoaIn, PessoaOut
from typing import List

api = NinjaAPI(
    title="API das Pessoas",
    description="API para gerir pessoas",
    version="1.0.0",
)


# LISTAR
@api.get("pessoas/", response=List[PessoaOut])
def listar_pessoas(request):
    return Pessoa.objects.all()