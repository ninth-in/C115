def processar_resposta(matricula):
    if matricula == '1':
        disciplina = input('Olá,Joao. Insira o codigo da disciplina: ')
        if disciplina == 'C001':
            avaliacao = input("Insira o numero da avalicao: ")
            if avaliacao == '1':
                print(f'Sua nota na avaliacao {avaliacao} na disciplina {disciplina} é 90')
            elif avaliacao == '2':
                print(f'Sua nota na avaliacao {avaliacao} na disciplina {disciplina} é 80')
        elif disciplina == 'C002':
            avaliacao = input("Insira o numero da avalicao: ")
            if avaliacao == '1':
                print(f'Sua nota na avaliacao {avaliacao} na disciplina {disciplina} é 60')
            elif avaliacao == '2':
                print(f'Sua nota na avaliacao {avaliacao} na disciplina {disciplina} é 90')

    elif matricula == '2':
        disciplina = input('Olá,Maria. Insira o codigo da disciplina: ')
        if disciplina == 'C001':
            avaliacao = input("Insira o numero da avalicao: ")
            if avaliacao == '1':
                print(f'Sua nota na avaliacao {avaliacao} na disciplina {disciplina} é 85')
            elif avaliacao == '2':
                print(f'Sua nota na avaliacao {avaliacao} na disciplina {disciplina} é 80')
        elif disciplina == 'C002':
            avaliacao = input("Insira o numero da avalicao: ")
            if avaliacao == '1':
                print(f'Sua nota na avaliacao {avaliacao} na disciplina {disciplina} é 60')
            elif avaliacao == '2':
                print(f'Sua nota na avaliacao {avaliacao} na disciplina {disciplina} é 95')

for i in range(1):
    matricula = input("Bom dia! Insira a matricula do aluno: ")
    processar_resposta(matricula)
