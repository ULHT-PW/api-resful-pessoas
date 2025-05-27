from ninja import Schema

class PessoaIn(Schema):
    nome: str 
    idade: int

class PessoaOut(Schema):
    id: int
    nome: str
    idade: int
    
class ErrorSchema(Schema):
    detail: str
