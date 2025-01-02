### RPG TO-DO LIST
from tabulate import tabulate

tarefas = []
areas = []

print("Bem vindo!")

def criar_area():
    nova_area = input("Nome da Nova area: ")
    if nova_area: ### Atributos de area: Nome, Nivel, Meta, Experiencia, quantidade de tarefas e id 
        meta = input("Meta da Área: ")
        tarefas_areas = 0
        area = {
            "ID": len(areas),
            "Nome": nova_area,
            "Tarefas": tarefas_areas,
            "Nivel": 0,
            "Meta": meta,
            "Exp": 0,
        }
        areas.append(area)
    else:
        print("Área Invalida")

def mostrar_areas():
    if len(areas) > 0:
        tabela = tabulate(areas, headers="keys", tablefmt="grid")
        print(tabela)
    else:
        print("Você não tem Areas")

def remover_area():
    if len(areas) > 0:
        mostrar_areas()
        tarefas_removidas = []
        indice = int(input("Número da Área que você deseja remover: "))
        tarefas_ex = input("Deseja Excluir as tarefas dessa Área? [S/N] ").upper()
        if tarefas_ex == "S":
            if len(tarefas) > 0:  ## Removendo tarefas
                for i in range(len(tarefas) - 1, -1, -1):
                    if tarefas[i]["Area"] == areas[indice]["Nome"]:
                        tarefas_removidas.append(tarefas[i])
                        tarefas.pop(i)
                        print("Tarefas Removidas")
                if len(tarefas) > 0: ## Ajeitar loop que fica fora do index 
                    if len(tarefas_removidas) > len(tarefas):
                        for i in range(0, len(tarefas_removidas)):
                            if tarefas[i]["ID"] >= tarefas_removidas[i]["ID"]:
                                tarefas[i]["ID"] -= 1
                         
        if tarefas_ex == "N":
            print("ATENÇÃO: TAREFAS QUE NÃO TEM AREA NÃO CONTAM PARA EXPERIENCIA OU SUBIR DE NIVEL")
            resp = input(f"Realmente Deseja excluir a Área {areas[indice -1]['Nome']} e não excluir as tarefas? [S/N]").upper()
            if resp == "S":
                if len(tarefas) > 0:
                    for i in range(0, len(tarefas)):
                        if tarefas[i]["Area"] == areas[indice]["Nome"]:
                            tarefas[i]["Area"] = "S/ Área"
            if resp == "N": 
                if len(tarefas) > 0:
                    for i in range(len(tarefas) - 1, -1, -1):
                        if tarefas[i]["Area"] == areas[indice]["Nome"]:
                            tarefas_removidas.append(tarefas[i])
                            tarefas.pop(i)
                            print("TAREFAS REMOVIDAS")
        print(f"Área: {areas[indice]['Nome']} Removida")
        areas.pop(indice)


def mostrar_tarefa():
    if len(tarefas) > 0:
        tabela = tabulate(tarefas, headers="keys", tablefmt="grid")
        print(tabela)
    else:
        print("Você ainda não tem Tarefas. Adicione uma selecionando a Opção 1")

def adicionar_tarefa():
    if len(areas) > 0:
        nova_tarefa = input("Digite o nome da Nova tarefa: ")
        if nova_tarefa:
            mostrar_areas()
            area = int(input("Numero da Área da Tarefa: "))
            for i in range(0,len(areas)):
                if (area) == i:
                    area = areas[i]["Nome"]
            tempo = (input("Tempo estimado para conclusão da Tarefa:[0 para indefinido] "))
            dif = int(input("Dificuldade: [1]- facil, [2]- medio, [3]- dificil, [4]- Desafiador "))
            match(dif):
                case 1:
                    dificuldade = "Fácil"
                case 2:
                    dificuldade = "Médio"
                case 3:
                    dificuldade = "Difícil"
                case 4:
                    dificuldade = "Desafiador"
            tarefa = {
                "ID": len(tarefas) + 1,
                "Nome": nova_tarefa,
                "Area": area,
                "Tempo": tempo,
                "Dificuldade": dificuldade,
            }
            tarefas.append(tarefa) 
            area_tarefa = tarefa["Area"]
            for i in range(0,len(areas)):
                if area_tarefa == areas[i]["Nome"]:
                    areas[i]["Tarefas"] += 1 
            print(f"Tarefa: {nova_tarefa} Adicionada")
        else:
            print("Tarefa Invalida")
    else:
        print("Adicione uma Área antes de adicionar uma tarefa")

def editar_tarefas():
    if len(tarefas) > 0:
        mostrar_tarefa()
        print("")
        indice = int(input("Qual Tarefa você quer editar: "))
        chave = int(input("Oque você quer editar: [1]- Nome, [2]- Área, [3]- Tempo, [4]- Dificuldade"))
        match(chave):
            case 1:
                novo_nome = input("Digite o novo nome: ")
                tarefas[indice - 1]["Nome"] = novo_nome
            case 2:
                nova_area = input("Digite o Número da Área: ")
                tarefas[indice - 1]["Area"] = nova_area
            case 3:
                novo_tempo = input("Digite o novo Tempo: ")
                tarefas[indice - 1]["Tempo"] = novo_tempo
            case 4:
                dif= int(input("Dificuldade: [1]- facil, [2]- medio, [3]- dificil, [4]- Desafiador  "))
                match(dif):
                    case 1:
                        nova_dificuldade = "Fácil"
                    case 2:
                        nova_dificuldade = "Médio"
                    case 3:
                        nova_dificuldade ="Difícil"
                    case 4:
                        nova_dificuldade = "Desafiador"
        tarefas[indice - 1]["Dificuldade"] = nova_dificuldade
        print(f"Tarefa {tarefas[indice - 1]['Nome']} Editada")
    else:
        print("Você não tem tarefas para editar.")

def remover_tarefa():
    if len(tarefas) > 0:
        mostrar_tarefa()
        print()
        indice = int(input("Digite o número da tarefa: "))
        print(f"Tarefa {tarefas[indice - 1]['Nome']} removida")
        ## Loop para redefinir o id das tarefas
        for i in range(0,len(tarefas)):
            if tarefas[i]["ID"] >= (indice + 1):
                tarefas[i]["ID"] -= 1
        ## Removendo tarefa da Area
        area_tarefa = tarefas[indice - 1]["Area"]
        for i in range(0,len(areas)):
            if area_tarefa == areas[i]["Nome"]:
                areas[i]["Tarefas"] -= 1 
        tarefas.pop(indice - 1)
    else:
        print("Você não tem Tarefas para remover")

def concluir_tarefas():
    if len(tarefas) > 0:
        mostrar_tarefa()
        indice = int(input("Digite número da tarefa que você quer completar: "))
        dif = tarefas[indice -1]["Dificuldade"]
        experiencia = 0
        match(dif):
            case "Fácil":
                experiencia = 10
            case "Médio":
                experiencia = 15
            case "Difícil":
                experiencia = 20
            case "Desafiador":
                experiencia = 25 
        ## Loop para ganho de experiencia
        for i in range(0,len(tarefas)): 
            if areas[i]["Nome"] == tarefas[indice - 1]["Area"]: 
                areas[i]["Tarefas"] -= 1
                areas[i]["Exp"] += experiencia
                if areas[i]["Exp"] >= 100:
                    areas[i]["Exp"] = 0
                    up_level = 1
                    areas[i]["Nivel"] = areas[i]["Nivel"] + up_level
            if areas[i]["Nome"] == tarefas[indice - 1]["Area"]:
                break 
        ## Loop para redefinir o id das tarefas
        for i in range(0,len(tarefas)):
            if tarefas[i]["ID"] >= (indice + 1):
                tarefas[i]["ID"] -= 1
        print(f"Tarefas {tarefas[indice - 1]['Nome']} concluida! Faltam apenas {len(tarefas) - 1} para concluir")
        tarefas.pop(indice - 1)
    else:
        print("Você não tem tarefas para completar. Adicione uma tarefa na opção 1")

def iniciar_menu():
    ativo = True 
    while ativo:
        print("########### MENU ##############")
        print("1. Adicionar Áreas       5. Mostrar Tarefas")
        print("2. Mostrar Áreas         6. Concluir Tarefas")
        print("3. Adicionar Tarefa      7. Editar Tarefas")
        print("4. Remover Tarefa        8. Sair")
        print("                         9.Remover Area")
        escolha = int(input("Opção: "))
        if escolha == 1:
            criar_area()
        if escolha == 2:
            mostrar_areas()
        if escolha == 3:
            adicionar_tarefa()
        if escolha == 4:
            remover_tarefa()
        if escolha == 5:
            mostrar_tarefa()
        if escolha == 6:
            concluir_tarefas()
        if escolha == 7:
            editar_tarefas()
        if escolha == 8:
            print("Encerrando sistema")
            ativo = False
        if escolha == 9:
            remover_area()

iniciar_menu()
