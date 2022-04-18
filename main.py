from random import choice

def formatar(tamanho):  
    print('='*(tamanho +len('Senha gerada: ')))

def gerador(tamanho):
    charMaiusculo = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U','V', 'W', 'X', 'Y', 'Z']
    charMinusculo = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']
    charEspeciais = ['&', '*', '@', ':', ',', '.', '/', '!', '?', ';', '"', '=', '%', '$', '#', '_', "'", '(', ')', '^', '{', '}', '[', ']']
    senha = ''
    aux = tamanho

    for i in range(0, tamanho):
        if aux <= 0: break
        aux -= 1
        senha += choice(charMinusculo)
        if aux <= 0: break
        aux -= 1
        senha += choice(charMaiusculo) 
        if aux <= 0: break
        aux -= 1 
        senha += choice(charEspeciais) 
    return senha

if __name__ == '__main__':
    while True:
        try:
            print('='*30)
            tamanho = int(input('Digite o tamanho da senha desejada: '))

            if tamanho <= 0:
                print('Digite um tamanho maior que 0.')
            else:
                formatar(tamanho)
                print(f'Senha gerada: {gerador(tamanho)}')
                formatar(tamanho)

                print('Deseja gerar outra senha?')
                print('1. Sim')
                print('2. Não')
                escolha = int(input('Escolha: '))

                if escolha == 2:
                    break                 
        except:
            print('Ocorreu um erro. Tente novamente.')
