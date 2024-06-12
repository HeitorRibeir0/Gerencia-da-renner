"""Desenvolva um sistema de gerenciamento de estoque para uma loja de roupas. O sistema deve permitir o cadastro de produtos, realizar vendas, adicionar novos estoques e gerar relatórios sobre a quantidade de cada produto disponível e o total de vendas realizadas."""
'''ESTOQUE tem que ter uma lista com os itens no estoque, onde tem que ter o nome do item, e a quantidade. FUNÇÕES: cadastro, realizar venda, total de vendas.
'''

class Estoque:
    def __init__(self,produto,qnt):
        self.produto = produto
        self.qnt = qnt
        self.produtos = []
        self.disponivel = True

    def add_prod(self,produto):
        self.produtos.append(produto)

    def disponibilidade(self):
        return 'Disponível' if self.disponivel else 'Indisponível'
    
    def exibir_produto(self):
        lista_produtos = ', '.join(self.produtos)
        disponibilidades = self.disponibilidade()
        return f'Produtos:\n{lista_produtos} {disponibilidades} {self.qnt}'
    
class Item_Estoque(Estoque):
    def __init__(self,tipo,tamanho,cor):
        self.tipo = tipo
        self.tamanho = tamanho
        self.cor = cor
        self.roupas = []

    

estoque = Estoque('Camisa')
item1 = Item_Estoque('Camisa','G','Preta')
roupa1.cadastrar_prod('Camisa Preta G')
print(roupa1.exibir_produto())

       
    