# Nomes: Enzo De Nadai Vieira RM: 569985
# Gustavo Zibini Belizario RM: 561376
# Tuma: 1CCPZ - 2026


containers_C = [
    98, 655, 603, 667, 986, 719, 531, 568, 716, 335, 301, 257, 690, 790, 427, 557, 307, 187, 167, 684,
    194, 705, 549, 457, 759, 697, 284, 699, 902, 525, 349, 318, 606, 286, 341, 149, 205, 609, 547, 583,
    271, 375, 632, 861, 648, 973, 917, 235, 876, 733, 781, 921, 126, 644, 347, 576, 128, 799, 631, 176,
    793, 820, 146, 83, 201, 958, 225, 830, 171, 936, 214, 229, 730, 591, 764, 999, 433, 119, 651, 622,
    173, 620, 804, 944, 92, 253, 841, 312, 867, 825, 121, 401, 594, 598, 111, 475, 154, 590, 526, 518,
    947, 461, 409, 539, 563, 714, 183, 14, 870, 392, 358, 447, 905, 278, 742, 449, 504, 482, 438, 384,
    132, 72, 808, 888, 160, 615, 406, 246, 396, 934, 470, 672, 663, 754, 274, 586, 913, 678, 270, 455,
    332, 691, 116, 296, 414, 454, 352, 155, 491, 910, 361, 932, 287, 788, 756, 105, 137, 571, 845, 198,
    889, 261, 862, 681, 552, 536, 241, 874, 339, 512, 773, 365, 293, 704, 739, 443, 960, 266, 323, 995,
    712, 856, 978, 725, 208, 245, 928, 981, 517, 319, 139, 835, 240, 748, 64, 812, 420, 381, 203, 823
]


# ====================================
# MISSÃO 1 - DIAGNÓSTICO DA CARGA
# ====================================

def analisar_carga(lista):

    menor = maior = lista[0]

    for item in lista:
        if item < menor:
            menor = item
        elif item > maior:
            maior = item

    return len(lista), menor, maior


# ===========================================
# MISSÃO 2 - LOCALIZAÇÃO DE EMERGÊNCIA
# ===========================================
def busca_linear(lista, codigo):

    comparacoes = 0
    for i in range(len(lista)):
        comparacoes += 1
        if lista[i] == codigo:
            return i, comparacoes
    return -1, comparacoes


# ===============================
# MISSÃO 3 - SELECTION SORT
# ===============================
def ordenar(lista):
    n = len(lista)
    comp = mov = 0

    for i in range(n - 1):
        menor = i
        for j in range(i + 1, n):
            comp += 1
            if lista[j] < lista[menor]:
                menor = j

        if menor != i:
            lista[i], lista[menor] = lista[menor], lista[i]
            mov += 1

    return lista, comp, mov

# =================================
# MISSÃO 4 - BUSCA OTIMIZADA
# =================================
def busca_binaria(lista, codigo):

    inicio = 0
    fim = len(lista) - 1
    comparacoes = 0

    while inicio <= fim:
        meio = (inicio + fim) // 2

        # 1ª comparação: igualdade
        comparacoes += 1
        if lista[meio] == codigo:
            return meio, comparacoes

        # 2ª comparação: ordem de grandeza
        comparacoes += 1
        if lista[meio] < codigo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1, comparacoes


# ===================================
# MISSÃO 5 - Relatório da estação
# ===================================
if __name__ == "__main__":
    # Missão 1: Análise da carga
    qtd, menor, maior = analisar_carga(containers_C)

    # Missão 3: Ordenação com Selection Sort
    lista_ordenada, comp_ord, mov_ord = ordenar(containers_C[:])

    codigo_existente = 999

    # Execução das buscas
    pos_linear_existente, comp_linear_existente = busca_linear(containers_C, codigo_existente)
    pos_binaria_existente, comp_binaria_existente = busca_binaria(lista_ordenada, codigo_existente)

    # ====================================
    # MISSÃO 5 - RELATÓRIO DA ESTAÇÃO
    # ====================================
    print("========== CENTRAL DE TRIAGEM ==========")
    print(f"Quantidade de contêineres: {qtd}")
    print(f"Menor código: {menor}")
    print(f"Maior código: {maior}")
    print()
    print("---------- ORDENAÇÃO ----------")
    print("Algoritmo: Selection Sort")
    print(f"Comparações: {comp_ord}")
    print(f"Movimentações: {mov_ord}")
    print()
    print("---------- BUSCAS ----------")
    print(f"Código procurado: {codigo_existente}")
    print(f"Busca Linear - Posição: {pos_linear_existente} | Comparações: {comp_linear_existente}")
    print(f"Busca Binária - Posição: {pos_binaria_existente} | Comparações: {comp_binaria_existente}")
    print("========================================")

    # Testes complementares com código INEXISTENTE (conforme solicitado na Missão 2 e 4)
    print("\n--- Testes Adicionais (Elemento Inexistente) ---")
    codigo_inexistente = 9999
    pos_lin_inex, comp_lin_inex = busca_linear(containers_C, codigo_inexistente)
    pos_bin_inex, comp_bin_inex = busca_binaria(lista_ordenada, codigo_inexistente)
    print(f"Código procurado (Inexistente): {codigo_inexistente}")
    print(f"Busca Linear - Posição: {pos_lin_inex} | Comparações: {comp_lin_inex}")
    print(f"Busca Binária - Posição: {pos_bin_inex} | Comparações: {comp_bin_inex}")