def soma(n1, n2):
    soma = n1 + n2
    print(f'{n1} + {n2} = {soma}')
            
def subtração(n1, n2):
    diferença = n1 - n2
    print(f'{n1} - {n2} = {diferença}')
            
def multiplicação(n1, n2):
    produto = n1 * n2
    print(f'{n1} * {n2} = {produto}')    
            
def divisão(n1, n2):
    quociente = n1 / n2
    print(f'{n1} / {n2} = {quociente}')
            
def potenciação(n1, n2):
    potencia = n1 ** n2
    print(f'{n1} ** {n2} = {potencia}')
    
def calculate():
    print('''Por favor, digite a operação matemática que você deseja: 
    + para adição
    - para subtração
    * para multiplicação
    / para divisão
    ** para potenciação
    ''')
    
    choice = input('Sua escolha: ').strip()
    
    if choice in '+-**/':
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
            
        if choice == '+':
            soma(n1, n2)
            
        elif choice == '-':
            subtração(n1, n2)

        elif choice == '*':
            multiplicação(n1, n2)

        elif choice == '/':
            divisão(n1, n2)

        elif choice == '**':        
            potenciação(n1, n2)

    else:
        print('Você provavelmente digitou algo errado, tente novamente.')
        calculate()

def again():
    choice_again = input('Deseja continuar fazendo contas? ').upper().strip()[0]
    if choice_again == 'S':
        pass
    elif choice_again == 'N':
        exit()
    else:
        print('Resposta inválida!')
        again()
        
while True:
    calculate()
    again()