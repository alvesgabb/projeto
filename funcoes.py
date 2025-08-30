
#funções parte 3


def lancar_nota(alunos,disciplinas):
    matricula = input("Digite a matrícula do aluno: ").strip()
    if matricula not in alunos:
        print("Aluno não encontrado.")
        return

    codigo = input("Digite o código da disciplina (ex: D01): ").strip().upper()
    if codigo not in disciplinas:
        print("Disciplina não encontrada.")
        return

    if codigo not in alunos[matricula]["disciplinas"]:
        print("Aluno não está matriculado nessa disciplina.")
        return

    nota = float(input("Digite a nota (0 a 10): "))
    if nota<0 or nota>10:
        print('Nota inválida. Deve estar entre 0 e 10.')
        return

    
    if codigo not in alunos[matricula]["notas"]:
        alunos[matricula]["notas"][codigo] = []
    alunos[matricula]["notas"][codigo].append(nota)

    print(f"Nota {nota} lançada para {alunos[matricula]['nome']} em {disciplinas[codigo]['nome']}.")


    
def exibir_boletim(alunos, disciplinas):
    matricula = input("Digite a matrícula do aluno: ").strip() 
    if matricula not in alunos:
        print("Aluno não encontrado.")
        return
    
    aluno = alunos[matricula]
    print(f"\nBoletim de {aluno['nome']}:")

    for cod in aluno["disciplinas"]:
        nome_disciplina = disciplinas[cod]["nome"]
        if cod in aluno["notas"]:
            notas = aluno["notas"][cod]
            print(f"- {nome_disciplina} ({cod}): {notas}")
        else:
            print(f"- {nome_disciplina} ({cod}): Sem notas lançadas.")



def  calcular_media_geral(alunos):
    matricula = input("Digite a matrícula do aluno: ").strip()
    if matricula not in alunos:
        print("Aluno não encontrado.")
        return None
    
    aluno = alunos[matricula]
    todas_notas = []
    
    for cod in aluno["notas"]:
        for nota in aluno["notas"][cod]:
         todas_notas.append(nota)
    
    if len(todas_notas)>0:
        media = sum(todas_notas) / len(todas_notas)
        print(f" Média geral de {aluno['nome']}: {media:.2f}")
        return media
    else:
        print("Nenhuma nota lançada para este aluno.")
        return None
    


def aprovado_em_todas(alunos):
    matricula = input("Digite a matrícula do aluno: ").strip()
    if matricula not in alunos:
        print("Aluno não encontrado.")
        return None

    aluno = alunos[matricula]
    todas_aprovadas = True

    for codigo_disciplina in aluno["disciplinas"]:
        if codigo_disciplina in aluno["notas"] and len(aluno["notas"][codigo_disciplina]) > 0:
            media = sum(aluno["notas"][codigo_disciplina]) / len(aluno["notas"][codigo_disciplina])
            status = "Aprovado" if media >= 6.0 else "Reprovado"
            print(f"{aluno['nome']} em {codigo_disciplina}: média {media:.2f} - {status}")
            if media < 6.0:
                todas_aprovadas = False
        else:
            print(f"{aluno['nome']} em {codigo_disciplina}: sem notas - Reprovado")
            todas_aprovadas = False

    if todas_aprovadas:
        print(f"\n{aluno['nome']} está aprovado em todas as disciplinas!")
    else:
        print(f"\n{aluno['nome']} não está aprovado em todas as disciplinas.")

    return todas_aprovadas
    
