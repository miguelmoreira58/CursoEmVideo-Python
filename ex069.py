
maior_de_idade=0
homem=0
mulheres_com_menos_de_vinte=0

while True:
    
    idade = int(input('Digite a idade: '))
    
    if idade > 0:

        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]

        if sexo in 'Ff' or sexo in 'Mm':

            if idade >= 18:
                maior_de_idade += 1

            if sexo in 'Mm':
                homem += 1

            if sexo in 'Ff' and idade < 20:
                mulheres_com_menos_de_vinte +=1

            continuar_ou_parar = str(input('\nPessoa Cadastrada!\nO usuário deseja continuar? [S/N]: ')).strip().upper()[0]

            if continuar_ou_parar in 'Ss':
                print('\nContinuando')
            elif continuar_ou_parar in 'Nn':
                print('\n')
                if maior_de_idade >= 2:
                    print(f'{maior_de_idade} pessoas tem mais de 18 anos.')
                elif maior_de_idade > 0:
                    print(f'{maior_de_idade} pessoa tem mais de 18 anos.')
                else:
                    print(f'Nenhuma pessoa cadastrada tem mais de 18 anos.')

                if homem >= 2:
                    print(f'{homem} homens foram cadastrados.')
                elif homem > 0:
                    print(f'{homem} homem foi cadastrado.')
                else:
                    print('Nenhum homem foi cadastrado.')

                if mulheres_com_menos_de_vinte >= 2:
                    print(f'{mulheres_com_menos_de_vinte} mulheres tem menos de 20 anos.')
                elif mulheres_com_menos_de_vinte > 0:
                    print(f'{mulheres_com_menos_de_vinte} mulher tem menos de 20 anos.')
                else:
                    print(f'Nenhuma mulher com menos de 20 anos foi cadastrada.')
                
                print('\nEncerrando...')
                break
            else:
                print('Continuando')
        else:
            print('\nSexo inválido.')
    else:
        print('\nIdade inválida.')