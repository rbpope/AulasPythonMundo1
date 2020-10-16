nome = str(input('Como é o nome do aluno: '))
n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
n3 = float(input('Digite a terceira nota do aluno: '))
m = float((n1 + n2 + n3) / 3)
ma = float(7.0)
if m >= ma:
    print('='*50)
    print(f'{nome}, sua média foi {m:.2f} e você está Aprovado, Boas Férias!!!')
    print('='* 50)
if float(5.0) <= m < ma:
    print('=' * 50)
    print(f'{nome}, sua média foi {m:.2f}. Vamos fazer recuperação!!!')
    print('='* 50)
if  m < float(5.0):
    print('=' * 50)
    print(f'{nome}, sua média foi {m:.2f} e você foi Reprovado!!!')
    print('='* 50)
