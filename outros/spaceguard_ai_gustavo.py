import ollama


MODEL_NAME = "llama3.2:1b"


system_prompt = """
Você é um assistente de inteligência artificial especializado em monitoramento de missões espaciais.

Sua função é analisar dados simulados de uma missão espacial e responder de forma técnica, curta e objetiva em português.

Use somente os dados, os fatos objetivos e a lista de riscos presentes enviados pelo usuário.

Regras obrigatórias:
- A lista "Fatos objetivos" é a verdade da análise.
- A lista "Riscos presentes" é a única fonte para riscos.
- Nunca altere valores ou textos informados pelo usuário.
- Nunca troque o status operacional informado.
- Status operacional parcial significa atenção operacional, não risco crítico.
- Status operacional crítico significa risco operacional crítico.
- Não mencione astronautas, combustível, motor, mission control ou propulsão.
- Não mencione morte, ferimentos, tripulação, perda total da missão ou danos irreparáveis.
- Não invente causas prováveis.
- Não copie os fatos objetivos como uma lista na resposta.
- Responda sempre os 4 blocos solicitados, mesmo quando a resposta for curta.
- Nunca pare a resposta no bloco 1, 2 ou 3.

A resposta deve ser organizada exatamente nos seguintes blocos:
1. Status da Missão
2. Riscos Identificados
3. Previsão de Falha
4. Ações Recomendadas

Formato de cada bloco:
- Comece diretamente em "1. Status da Missão".
- Não escreva uma linha inicial repetindo os dados recebidos.
- Use no máximo 2 frases por bloco.
- Em "Riscos Identificados", liste somente os riscos presentes nos fatos objetivos.
- Em "Riscos Identificados", use somente a lista "Riscos presentes" enviada pelo usuário.
- Em "Riscos Identificados", inclua todos os itens da lista "Riscos presentes".
- Se "Riscos presentes" estiver como "nenhum", escreva: "Nenhum risco crítico identificado."
- O bloco 3 deve explicar uma possível falha com base apenas nos riscos presentes.
- O bloco 4 deve recomendar ações práticas para os riscos presentes.
- O bloco 4 deve incluir pelo menos uma ação para cada risco presente.
- Se houver 3 ou mais riscos presentes, o bloco 1 deve classificar a missão como estado crítico.
- Se houver 1 ou 2 riscos presentes, o bloco 1 deve classificar a missão como estado de atenção.
- Se não houver riscos presentes, o bloco 1 deve classificar a missão como operação normal.
- Para superaquecimento, recomende reduzir a temperatura para abaixo de 80 °C.
- Para energia baixa, recomende ativar modo de economia de energia.
- Para comunicação instável, recomende restabelecer ou reforçar o canal de comunicação.
- Para status operacional crítico, recomende revisar os subsistemas operacionais.
- Para vibração alta, recomende estabilizar a cápsula e investigar a origem da vibração.
"""


def montar_user_prompt(dados: dict) -> str:
    fatos = []
    riscos_presentes = []

    if dados["temperatura"] > 80:
        fatos.append("Temperatura crítica: acima de 80 °C.")
        riscos_presentes.append("Superaquecimento")
    elif dados["temperatura"] < 10:
        fatos.append("Temperatura crítica: abaixo de 10 °C.")
        riscos_presentes.append("Temperatura baixa")
    else:
        fatos.append("Temperatura dentro da faixa não crítica.")

    if dados["energia"] < 20:
        fatos.append("Energia baixa: abaixo de 20%.")
        riscos_presentes.append("Energia baixa")
    else:
        fatos.append("Energia não está em nível crítico.")

    if dados["comunicacao"] == "instável":
        fatos.append("Comunicação com risco: instável.")
        riscos_presentes.append("Comunicação instável")
    else:
        fatos.append("Comunicação estável.")

    if dados["status_operacional"] == "parcial":
        fatos.append("Status operacional informado: parcial, classificado como atenção operacional.")
        riscos_presentes.append("Atenção operacional")
    elif dados["status_operacional"] == "crítico":
        fatos.append("Status operacional informado: crítico, classificado como risco operacional crítico.")
        riscos_presentes.append("Status operacional crítico")
    else:
        fatos.append(f"Status operacional informado: {dados['status_operacional']}.")

    if dados["vibracao"] == "alta":
        fatos.append("Vibração alta: sinal de risco.")
        riscos_presentes.append("Vibração alta")
    else:
        fatos.append("Vibração não está em nível crítico.")

    riscos_texto = "\n".join(f"- {risco}" for risco in riscos_presentes) or "- nenhum"
    if riscos_presentes:
        instrucao_riscos = (
            "No bloco 2. Riscos Identificados, liste somente os itens da lista "
            "\"Riscos presentes\". Não inclua dados normais nesse bloco."
        )
    else:
        instrucao_riscos = (
            "No bloco 2. Riscos Identificados, escreva exatamente: "
            "\"Nenhum risco crítico identificado.\""
        )

    return f"""
Analise os seguintes dados simulados de uma missão espacial:

Temperatura: {dados['temperatura']} °C
Energia: {dados['energia']}%
Comunicação: {dados['comunicacao']}
Status operacional: {dados['status_operacional']}
Luminosidade: {dados['luminosidade']}
Vibração: {dados['vibracao']}

Fatos objetivos que devem ser respeitados na análise:
{chr(10).join(f"- {fato}" for fato in fatos)}

Riscos presentes:
{riscos_texto}

Com base nesses dados, gere uma análise completa da situação da missão.
Use os fatos objetivos como fonte principal.
Não reclassifique temperatura, energia ou comunicação se os fatos objetivos indicarem que estão normais.
Não altere o status operacional informado.
Não copie a lista de fatos objetivos na resposta.
Não adicione riscos que não estejam na lista "Riscos presentes".
{instrucao_riscos}
Obrigatoriamente escreva os blocos 1, 2, 3 e 4.
No bloco 3, descreva apenas falhas operacionais simuladas, como instabilidade do monitoramento, perda de confiabilidade ou interrupção parcial de subsistemas.
No bloco 3, não mencione morte, astronautas, tripulação, perda total da missão ou danos irreparáveis.
No bloco 4, inclua ações para todos os riscos presentes.
"""


def analisar_missao(dados: dict) -> str:
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": montar_user_prompt(dados)},
    ]

    response = ollama.chat(
        model=MODEL_NAME,
        messages=messages,
        options={
            "temperature": 0.2,
            "top_k": 20,
            "top_p": 0.8,
            "num_predict": 450,
            "num_ctx": 4096,
            "repeat_penalty": 1.1,
            "seed": 42,
        },
    )

    return response["message"]["content"]


def normalizar_texto(valor: str) -> str:
    texto = valor.strip().lower()
    correcoes = {
        "estavel": "estável",
        "instavel": "instável",
        "medio": "média",
        "critico": "crítico",
    }
    return correcoes.get(texto, texto)


def coletar_dados_missao() -> dict:
    print("=== SpaceGuard AI ===")
    print("Informe os dados atuais da missão.\n")

    temperatura = float(input("Temperatura (°C): "))
    energia = int(input("Energia (%): "))
    comunicacao = normalizar_texto(input("Comunicação (estável/instável): "))
    status_operacional = normalizar_texto(input("Status operacional (normal/parcial/crítico): "))
    luminosidade = int(input("Luminosidade: "))
    vibracao = normalizar_texto(input("Vibração (baixa/média/alta): "))

    return {
        "temperatura": temperatura,
        "energia": energia,
        "comunicacao": comunicacao,
        "status_operacional": status_operacional,
        "luminosidade": luminosidade,
        "vibracao": vibracao,
    }


if __name__ == "__main__":
    while True:
        dados_missao = coletar_dados_missao()
        print("\n=== Análise da IA ===\n")
        print(analisar_missao(dados_missao))

        continuar = input("\nDeseja realizar uma nova análise? (s/n): ").strip().lower()
        if continuar != "s":
            print("\nEncerrando SpaceGuard AI.")
            break
