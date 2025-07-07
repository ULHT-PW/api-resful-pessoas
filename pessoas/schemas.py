from ninja import Schema

class PessoaIn(Schema):
    nome: str
    idade: int


class PessoaOut(PessoaIn):
    id: int


class ErrorSchema(Schema):
    detail: str