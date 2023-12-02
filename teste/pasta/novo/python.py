class Carro:
    cor = 'branco'
    marca = 'volks'
    modelo = 'gol'

    def ligar_motor(self):
        print('vrum ;vrum')
    
    def cor_do_carro(self):
        print(self.cor)


carrinho = Carro()
carrinho.cor = 'vermelho'
carrinho.marca = 'audi'

print(carrinho.marca)
carrinho.ligar_motor()
carrinho.cor_do_carro()

print('\n'+'#'*10, 'NOVO OBJETO', '#'*10 + '\n')

novo_carro = Carro()
print(novo_carro.marca)
novo_carro.ligar_motor()
novo_carro.cor_do_carro()
