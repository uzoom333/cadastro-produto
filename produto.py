"""Modelo de dominio do cadastro de produtos."""


class Produto:
    """Representa um produto com nome e preco."""

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} - Preco: R$ {self.preco:.2f}"
