"""Desenvolva um sistema de gerenciamento de estoque para uma loja de roupas. O sistema deve permitir o cadastro de produtos, realizar vendas, adicionar novos estoques e gerar relatórios sobre a quantidade de cada produto disponível e o total de vendas realizadas."""
'''estoque:produto,quantidade /funções: add_produto/venda/exibir_produto/total_vendas
'''

class Estoque:
    def __init__(self):
        self.produtos = []

    def add_produto(self,produto, qnt):
        self.produtos.append({'Produto': produto, 'Quantidade': qnt, 'Disponibilidade': True})
    
    def vender_prod(self, nome_produto, qnt_venda):
        for p in self.produtos:
            if p['produto'] == nome_produto:
                if p['qnt'] >= qnt_venda:
                    p['qnt'] -= qnt_venda
                    print(f"{qnt_venda} unidade(s) de {nome_produto} vendida(s).")
                    if p['qnt'] == 0:
                        p['disponibilidade'] = False
                else:
                    print(f"Quantidade insuficiente de {nome_produto} para venda.")
                return
        print(f"Produto {nome_produto} não encontrado no estoque.")

    def exibir_produto(self):
        return [f"Produto: {p['produto']}, Quantidade: {p['qnt']}, Disponibilidade: {p['disponibilidade']}" for p in self.produtos]

estoque = Estoque('Camisa', 5)
estoque.add_produto()
estoque.exibir_produto

    

       
    