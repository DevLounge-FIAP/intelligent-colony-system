from modules.modulos import Colonia, Modulo, SistemaSolar, SistemaEolico, SistemaReserva
from rules.regras import verificar_colonia
from forecast.previsao import (previsao_energia_eolica, previsao_energia_solar,
                                plotar_grafico_historico_eolica, plotar_grafico_historico_solar,
                                plotar_grafico_previsao_eolica, plotar_grafico_previsao_solar)
from forecast.analise_energetica import analise_energetica_eolica, analise_energetica_solar

colonia = Colonia()
telemetria_configurada = False

while True:
    print("===============")
    print("Menu Principal")
    print("===============")
    print("[1] - Configuração (Módulos, Sistemas e Telemetria)")
    print("[2] - Regras")
    print("[3] - Previsão")
    print("[0] - Sair")

    match input("Escolha: "):
        case "0":
            print("Programa encerrado!")
            break
        
        case "1":
            while True:
                print("=============")
                print("Menu Configuração")
                print("=============")
                print("[1] - Cadastrar Módulo")
                print("[2] - Cadastrar Sistema de Energia")
                print("[3] - Configurar vento e Radiação Solar")
                print("[4] - Mostrar Módulos Cadastrados")
                print("[5] - Mostrar Sistemas Cadastrados")
                print("[0] - Voltar ao menu Principal")

                match input("Escolha: "):
                    case "0":
                        break

                    case "1":
                        id_nome = input("ID do Módulo (Exemplo: 'MED-01'): ")
                        tipo = input("Categoria do módulo (Exemplo: 'Medico'): ")
                        funcao = input("Descrição da função (Exemplo: 'Suporte à Vida'): ")
                        try:
                            criticidade = int(input("Criticidade do Módulo de 1 a 5: "))
                            while criticidade < 1 or criticidade > 5:
                                criticidade = int(input("Criticidade do Módulo de 1 a 5: "))
                            consumo = int(input("Energia consumida por hora: "))
                            while consumo < 0:
                                consumo = int(input("Consumo deve ser um valor positivo: "))
                        except ValueError:
                            print("Entrada inválida. Digite apenas números inteiros.")
                            continue

                        novo_modulo = Modulo(id_nome, tipo, funcao, criticidade, consumo)
                        colonia.modulos.append(novo_modulo)
                        print(f"O Módulo {id_nome} Foi Cadastrado!")

                    case "2":
                        print("[1] - Sistema Solar")
                        print("[2] - Sistema Eólico")
                        print("[3] - Sistema Reserva")

                        tipo_sistema = input("Tipo do Sistema: ")
                        nome = input("Nome do Sistema: ")

                        try:
                            if tipo_sistema == "1":
                                capacidade_max = int(input("Capacidade maxima de geração do sistema (Max 30): "))
                                while capacidade_max < 0 or capacidade_max > 30:
                                    capacidade_max = int(input("Capacidade maxima do sistema deve estar entre 1-30: "))
                                geracao_atual = int(input("Geração atual do sistema: "))
                                while geracao_atual < 0 or geracao_atual > capacidade_max:
                                    geracao_atual = int(input("Geração atual do sistema deve respeitar a capacidade maxima: "))

                            elif tipo_sistema == "2":
                                capacidade_max = int(input("Capacidade maxima de geração do sistema (Max 20): "))
                                while capacidade_max < 0 or capacidade_max > 20:
                                    capacidade_max = int(input("Capacidade maxima do sistema deve estar entre 1-20: "))
                                geracao_atual = int(input("Geração atual do sistema: "))
                                while geracao_atual < 0 or geracao_atual > capacidade_max:
                                    geracao_atual = int(input("Geração atual do sistema deve respeitar a capacidade maxima: "))

                            elif tipo_sistema == "3":
                                capacidade_max = int(input("Capacidade maxima do sistema (Max 50): "))
                                while capacidade_max < 0 or capacidade_max > 50:
                                    capacidade_max = int(input("Capacidade maxima do sistema deve estar entre 1-50: "))
                                geracao_atual = int(input("Geração atual do sistema: "))
                                while geracao_atual < 0 or geracao_atual > capacidade_max:
                                    geracao_atual = int(input("Geração atual do sistema deve respeitar a capacidade maxima: "))
                            else:
                                print("Opção inválida.")
                                continue
                        except ValueError:
                            print("Entrada inválida. Digite apenas números inteiros.")
                            continue

                        match tipo_sistema:
                            case "1":
                                sistema = SistemaSolar(nome, capacidade_max, geracao_atual)
                            case "2":
                                sistema = SistemaEolico(nome, capacidade_max, geracao_atual)
                            case "3":
                                sistema = SistemaReserva(nome, capacidade_max, geracao_atual)
                            
                        colonia.sistemas.append(sistema)
                        print(f"Sistema {nome} Foi Cadastrado!")
                    
                    case "3":
                        try:
                            telemetria_configurada = True
                            colonia.vento = float(input("Velocidade do vento (m/s) [0 a 30]: "))
                            while colonia.vento < 0 or colonia.vento > 30:
                                colonia.vento = float(input("Velocidade do vento (m/s) [0 a 30]: "))
                            colonia.radiacao_solar = int(input("Radiação Solar (%) [0 a 100]: "))
                            while colonia.radiacao_solar < 0 or colonia.radiacao_solar > 100:
                                colonia.radiacao_solar = int(input("Radiação Solar (%) [0 a 100]: "))
                            print("Vento e Radiação Solar Atualizados!")
                        except ValueError:
                            telemetria_configurada = False
                            print("Entrada inválida. Digite apenas números.")
                    
                    case "4":
                        if not colonia.modulos:
                            print("Nenhum Módulo Cadastrado!")
                        else:
                            for m in colonia.modulos:
                                print(m)
                    
                    case "5":
                        if not colonia.sistemas:
                            print("Nenhum Sistema Cadastrado!")
                        else:
                            for s in colonia.sistemas:
                                print(f"{s.nome} | Tipo: {s.__class__.__name__} | Geração: {s.geracao_atual} kWh | Máx: {s.capacidade_max} kWh")

                    case _:
                        print("Opção Inválida!")

        case "2":
            if len(colonia.modulos) < 2 or not colonia.sistemas or not telemetria_configurada:
                print("ERRO: Cadastre pelo menos 2 módulos, 1 sistema e configure a telemetria no Menu de Configuração antes de prosseguir.")
                continue

            while True:
                print("============")
                print("Menu Regras")
                print("============")
                print("[1] - Executar Análise de Regras")
                print("[0] - Voltar")

                match input("Escolha: "):
                    case "0":
                        break

                    case "1":
                        recomendacoes = verificar_colonia(colonia)
                        for rec in recomendacoes:
                            print(f"\nTipo: {rec['tipo']}")
                            print(f"Mensagem: {rec['mensagem']}")
                            print(f"Prioridade: {rec['prioridade']}")
                            if "modulos_ativos" in rec:
                                ativos = ", ".join(rec["modulos_ativos"]) or "nenhum"
                                desligados = ", ".join(rec["modulos_desligados"]) or "nenhum"
                                print(f"Módulos ativos: {ativos}")
                                print(f"Módulos desligados: {desligados}")
                                print(f"Energia restante no plano: {rec['energia_restante_modulos']:.2f}")
                    
                    case _:
                        print("Opção Inválida")

        case "3":
            if len(colonia.modulos) < 2 or not colonia.sistemas or not telemetria_configurada:
                print("ERRO: Cadastre pelo menos 2 módulos, 1 sistema e configure a telemetria no Menu de Configuração antes de prosseguir.")
                continue

            while True:
                print("===============")
                print("MENU PREVISÃO")
                print("===============")
                print("1 - Previsão eólica (usar telemetria atual)")
                print("2 - Previsão solar (usar telemetria atual)")
                print("3 - Gráfico histórico eólico")
                print("4 - Gráfico histórico solar")
                print("0 - Voltar")

                match input("Escolha: "):
                    case "0":
                        break

                    case "1":
                        vento = colonia.vento
                        energia = previsao_energia_eolica(vento)
                        print(f"\nVelocidade do Vento Atual: {vento} m/s")
                        print(f"Previsão de geração eólica: {energia:.2f} kWh")
                        
                        print("\n--- Análise de Suficiência Energética (Eólica) ---")
                        alertas_eolicos = analise_energetica_eolica(colonia)
                        for r in alertas_eolicos:
                            print(f"[{r['prioridade']}] {r['tipo']}: {r['mensagem']}")
                        print("--------------------------------------------------\n")
                        
                        plotar_grafico_previsao_eolica(vento)

                    case "2":
                        radiacao = colonia.radiacao_solar
                        energia = previsao_energia_solar(radiacao)
                        print(f"\nRadiação Solar Atual: {radiacao}%")
                        print(f"Previsão de geração solar: {energia:.2f} kWh")
                        
                        print("\n--- Análise de Suficiência Energética (Solar) ---")
                        alertas_solares = analise_energetica_solar(colonia)
                        for r in alertas_solares:
                            print(f"[{r['prioridade']}] {r['tipo']}: {r['mensagem']}")
                        print("-------------------------------------------------\n")
                        
                        plotar_grafico_previsao_solar(radiacao)

                    case "3":
                        plotar_grafico_historico_eolica()

                    case "4":
                        plotar_grafico_historico_solar()

                    case _:
                        print("Opção invalida.")

        case _:
            print("Opção inválida.")