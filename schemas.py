from pydantic import BaseModel

class Book(BaseModel):
    titulo: str
    autor: str
    ano: int
    genero: str          # 4º atributo

