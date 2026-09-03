"""Modelo de dominio do cadastro de produtos."""


class Produto:
    """Representa um produto com nome, preco e quantidade."""

    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
        return (
            f"{self.nome} - Preco: R$ {self.preco:.2f} "
            f"- Quantidade: {self.quantidade}"
        )
