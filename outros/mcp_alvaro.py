""""
Nomes:
Alan Junio Araujo de Souza RM: 574112
Gustavo Zibini Belizario RM: 561376

Turma:
1CCPZ - 2026

"""

"""
Sistema de Estimativa de Consumo Médio Mensal de Energia Elétrica Residencial
"""


def criar_base_equipamentos():
    """
    Base de dados pré-definida com equipamentos elétricos comuns,
    suas respectivas categorias e potências nominais em Watts (W).
    """
    return [
        {"id": 1, "nome": "Geladeira (2 portas/Frost Free)", "categoria": "Cozinha", "potencia_w": 250},
        {"id": 2, "nome": "Micro-ondas", "categoria": "Cozinha", "potencia_w": 1200},
        {"id": 3, "nome": "Fogão Elétrico / Cooktop (boca)", "categoria": "Cozinha", "potencia_w": 1500},
        {"id": 4, "nome": "Cafeteira Elétrica", "categoria": "Cozinha", "potencia_w": 800},
        {"id": 5, "nome": "Chuveiro Elétrico", "categoria": "Banheiro", "potencia_w": 5500},
        {"id": 6, "nome": "Secador de Cabelo", "categoria": "Banheiro", "potencia_w": 1400},
        {"id": 7, "nome": "Ar-Condicionado (9.000 BTUs)", "categoria": "Climatização", "potencia_w": 1000},
        {"id": 8, "nome": "Ventilador de Teto/Mesa", "categoria": "Climatização", "potencia_w": 100},
        {"id": 9, "nome": "Televisor LED (43 a 55 pol)", "categoria": "Sala/Geral", "potencia_w": 120},
        {"id": 10, "nome": "Computador / Notebook", "categoria": "Escritório", "potencia_w": 150},
        {"id": 11, "nome": "Lâmpada LED", "categoria": "Iluminação", "potencia_w": 10},
        {"id": 12, "nome": "Máquina de Lavar Roupa", "categoria": "Lavanderia", "potencia_w": 1000},
        {"id": 13, "nome": "Ferro de Passar Roupas", "categoria": "Lavanderia", "potencia_w": 1200},
    ]


def cadastrar_imovel():
    """Coleta as informações básicas de identificação do imóvel."""
    print("\n" + "=" * 55)
    print("           CADASTRO DO IMÓVEL RESIDENCIAL")
    print("=" * 55)

    nome_responsavel = input("Nome do responsável/proprietário: ").strip()
    identificacao = input("Identificação/Apelido do imóvel (ex: Casa Principal, Sítio): ").strip()
    endereco = input("Endereço/Localização: ").strip()

    return {
        "responsavel": nome_responsavel if nome_responsavel else "Não informado",
        "identificacao": identificacao if identificacao else "Residência",
        "endereco": endereco if endereco else "Não informado"
    }


def exibir_catalogo(base_equipamentos):
    """Exibe a tabela de equipamentos cadastrados na base."""
    print("\n" + "-" * 68)
    print(f"{'ID':<4} | {'Equipamento':<35} | {'Categoria':<15} | {'Potência (W)'}")
    print("-" * 68)
    for eq in base_equipamentos:
        print(f"{eq['id']:<4} | {eq['nome']:<35} | {eq['categoria']:<15} | {eq['potencia_w']:>6} W")
    print("-" * 68)


def calcular_consumo_mensal_kwh(potencia_w, quantidade, horas_por_dia, dias_mes=30):
    """
    Calcula o consumo mensal estimado em kWh.
    Fórmula: (Potência (W) * Quantidade * Horas/dia * Dias) / 1000
    """
    return (potencia_w * quantidade * horas_por_dia * dias_mes) / 1000.0


def selecionar_equipamentos(base_equipamentos):
    """Permite selecionar equipamentos da base ou cadastrar novos itens."""
    equipamentos_selecionados = []
    mapa_equipamentos = {eq["id"]: eq for eq in base_equipamentos}

    while True:
        exibir_catalogo(base_equipamentos)
        print("\nOpções:")
        print(" [ID] - Digite o número do equipamento para adicioná-lo")
        print(" [N]  - Cadastrar um novo equipamento personalizado")
        print(" [0]  - Finalizar seleção e gerar relatório")

        escolha = input("\nEscolha uma opção: ").strip().lower()

        if escolha == "0":
            if not equipamentos_selecionados:
                print("Aviso: Nenhum equipamento foi selecionado.")
                continuar = input("Deseja realmente sair sem itens? (s/n): ").strip().lower()
                if continuar == "s":
                    break
                else:
                    continue
            break

        elif escolha == "n":
            print("\n--- Cadastro de Novo Equipamento ---")
            nome = input("Nome do equipamento: ").strip()
            categoria = input("Categoria (ex: Cozinha, Lazer): ").strip()
            try:
                potencia = float(input("Potência nominal em Watts (W): "))
                novo_id = len(base_equipamentos) + 1
                novo_item = {
                    "id": novo_id,
                    "nome": nome,
                    "categoria": categoria if categoria else "Outros",
                    "potencia_w": potencia
                }
                base_equipamentos.append(novo_item)
                mapa_equipamentos[novo_id] = novo_item
                print(f" Equipamento '{nome}' cadastrado com sucesso com ID {novo_id}!")
            except ValueError:
                print(" Erro: Potência inválida. Digite apenas valores numéricos.")
            continue

        else:
            try:
                equip_id = int(escolha)
                if equip_id not in mapa_equipamentos:
                    print(" ID de equipamento inválido!")
                    continue

                equip = mapa_equipamentos[equip_id]
                print(f"\nSelecionado: {equip['nome']} ({equip['potencia_w']} W)")
                qtd = int(input("Quantidade deste equipamento: "))
                horas = float(input("Tempo médio de uso diário por aparelho (em horas/dia): "))

                if qtd <= 0 or horas < 0 or horas > 24:
                    print(" A quantidade deve ser > 0 e as horas diárias entre 0 e 24.")
                    continue

                consumo_item = calcular_consumo_mensal_kwh(equip["potencia_w"], qtd, horas)

                equipamentos_selecionados.append({
                    "nome": equip["nome"],
                    "categoria": equip["categoria"],
                    "potencia_w": equip["potencia_w"],
                    "quantidade": qtd,
                    "horas_dia": horas,
                    "consumo_mensal_kwh": consumo_item
                })

                print(f" Adicionado com sucesso! Consumo: {consumo_item:.2f} kWh/mês.")

            except ValueError:
                print(" Entrada inválida. Digite o número correspondente.")

    return equipamentos_selecionados


def exibir_relatorio(imovel, equipamentos):
    """Gera o relatório com o consumo por equipamento e total do imóvel."""
    print("\n" + "=" * 75)
    print("         RELATÓRIO DE ESTIMATIVA DE CONSUMO ENERGÉTICO RESIDENCIAL")
    print("=" * 75)
    print(f" Imóvel:      {imovel['identificacao']}")
    print(f" Responsável: {imovel['responsavel']}")
    print(f" Endereço:    {imovel['endereco']}")
    print("=" * 75)

    if not equipamentos:
        print("Nenhum equipamento foi cadastrado para este imóvel.")
        print("=" * 75)
        return

    print(f"{'Equipamento':<30} | {'Qtd':<4} | {'Uso (h/dia)':<11} | {'Pot.(W)':<8} | {'Consumo (kWh/mês)'}")
    print("-" * 75)

    consumo_total_kwh = 0.0
    for item in equipamentos:
        consumo_total_kwh += item["consumo_mensal_kwh"]
        print(
            f"{item['nome']:<30} | {item['quantidade']:<4} | {item['horas_dia']:<11.1f} | {item['potencia_w']:<8.0f} | {item['consumo_mensal_kwh']:>14.2f} kWh")

    print("-" * 75)
    print(f"{'CONSUMO TOTAL MÉDIO ESTIMADO:':<58} {consumo_total_kwh:>14.2f} kWh/mês")
    print(f"{'MÉDIA DIÁRIA ESTIMADA:':<58} {consumo_total_kwh / 30.0:>14.2f} kWh/dia")
    print("=" * 75)
    print("Observação: Considerado mês padrão de 30 dias.")
    print("=" * 75 + "\n")


def main():
    print("\n" + "#" * 65)
    print(" SISTEMA DE DIMENSIONAMENTO ENERGÉTICO RESIDENCIAL")
    print("#" * 65)

    base_equipamentos = criar_base_equipamentos()
    imovel = cadastrar_imovel()
    equipamentos_selecionados = selecionar_equipamentos(base_equipamentos)
    exibir_relatorio(imovel, equipamentos_selecionados)


if __name__ == "__main__":
    main()