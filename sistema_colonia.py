"""
SISTEMA INTEGRADO DE GESTÃO ENERGÉTICA DA COLÔNIA
Fase 3 - Projeto Acadêmico

Este sistema organiza os dados da colônia, prevê a geração energética
com base na velocidade do vento (usando regressão linear simples) e toma
decisões automatizadas para priorizar o Suporte à Vida e otimizar o consumo.
"""

# 1. Estrutura e organização dos dados

def pegar_dados_colonia():
    """
    Organiza os dados da colônia em dicionários e listas.
    Representa o estado atual dos recursos e a hierarquia dos subsistemas.
    """
    dados = {
        "status_operacional": {
            "energia_bateria": 40.0,      # Nível da bateria em porcentagem (%)
            "geracao_atual": 45.0,        # Geração de energia atual (kW)
            "consumo_atual": 70.0,        # Consumo total da colônia (kW)
            "reserva_emergencia": 100.0   # Reserva de emergência em kW
        },
        "subsistemas_hierarquia": {
            "sistema_energetico": {
                "fontes": ["solar", "eolica"],
                "armazenamento": "baterias_central"
            },
            "suporte_vida": {
                "essencial": True,
                "sistemas": ["oxigenio", "aquecimento", "pressurizacao"]
            },
            "sistemas_secundarios": {
                "essencial": False,
                "sistemas": ["laboratorio_pesquisa", "iluminacao_externa", "estufa_secundaria"]
            }
        },
        "historico_climatico": {
            "velocidade_vento": [8.0, 10.0, 12.0, 14.0, 16.0],      # Velocidade em m/s
            "energia_eolica_gerada": [20.0, 25.0, 30.0, 35.0, 40.0]  # Energia em kW
        }
    }
    return dados


# 2. Modelagem matemática e previsão (regressão linear)

def calcular_regressao(x, y):
    """
    Calcula os coeficientes 'a' (inclinação) e 'b' (intercepto) da reta y = a*x + b
    utilizando a fórmula dos Mínimos Quadrados.
    Feito sem o uso de bibliotecas externas.
    """
    n = len(x)
    if n == 0 or n != len(y):
        return 0, 0

    soma_x = sum(x)
    soma_y = sum(y)
    
    soma_xy = 0
    soma_x2 = 0
    for i in range(n):
        soma_xy += x[i] * y[i]
        soma_x2 += x[i] ** 2

    # Fórmula da regressão linear simples
    a = (n * soma_xy - soma_x * soma_y) / (n * soma_x2 - (soma_x ** 2))
    b = (soma_y - a * soma_x) / n

    return a, b


def prever_geracao_eolica(vento_futuro, historico_x, historico_y):
    """
    Aplica o modelo de regressão para estimar quanta energia será gerada
    com base no vento previsto.
    """
    a, b = calcular_regressao(historico_x, historico_y)
    previsao = a * vento_futuro + b
    return round(previsao, 2)


# 3. Análise de eficiência energética

def checar_eficiencia(geracao, consumo):
    """
    Compara a geração e o consumo atual da colônia para emitir diagnósticos simples.
    """
    if consumo > geracao:
        diferenca = consumo - geracao
        return f"ALERTA: Consumo maior que a geração! Deficit de {diferenca:.1f} kW."
    elif geracao > consumo:
        excedente = geracao - consumo
        return f"SUGESTÃO: Armazenar energia excedente de {excedente:.1f} kW nas baterias."
    else:
        return "ESTÁVEL: Geração e consumo perfeitamente equilibrados."


# 4. Lógica de decisão e regras automatizadas

def tomar_decisao(energia_bateria, consumo, geracao, subsistemas):
    """
    Aplica regras condicionais booleanas priorizando a manutenção do Suporte à Vida
    e desligando os sistemas não essenciais em momentos de escassez.
    """
    decisoes = []

    # Regra principal: Se a bateria estiver abaixo de 50% E o consumo for maior que a geração
    if energia_bateria < 50 and consumo > geracao:
        decisoes.append("MODO ECONOMIA ATIVADO: Reduzir consumo de energia imediatamente.")
        
        sistemas_desligar = ", ".join(subsistemas['sistemas_secundarios']['sistemas'])
        decisoes.append(f"AÇÃO: Desligando sistemas não essenciais: {sistemas_desligar}.")
        
        sistemas_manter = ", ".join(subsistemas['suporte_vida']['sistemas'])
        decisoes.append(f"MANTER LIGADO: Priorizando Suporte à Vida: {sistemas_manter}.")

    elif energia_bateria < 20:
        decisoes.append("ALERTA CRÍTICO: Nível de bateria extremamente baixo! Entrando em protocolo de emergência.")
    else:
        decisoes.append("OPERAÇÃO NORMAL: Níveis de energia dentro da margem de segurança.")

    return decisoes


# 5. Execução principal

def executar_sistema():
    print("=" * 60)
    print("      SISTEMA INTEGRADO DE GESTÃO DA COLÔNIA - FASE 3")
    print("=" * 60)

    # Carregar a base de dados
    dados = pegar_dados_colonia()
    status = dados["status_operacional"]
    historico = dados["historico_climatico"]
    subsistemas = dados["subsistemas_hierarquia"]

    # 1. Análise de Eficiência
    print("
--- 1. ANÁLISE DE EFICIÊNCIA ENERGÉTICA ---")
    print(f"Geração Atual: {status['geracao_atual']} kW | Consumo Atual: {status['consumo_atual']} kW")
    diagnostico = checar_eficiencia(status["geracao_atual"], status["consumo_atual"])
    print(f"Diagnóstico: {diagnostico}")

    # 2. Tomada de Decisão Automatizada
    print("
--- 2. TOMADA DE DECISÃO AUTOMATIZADA ---")
    print(f"Nível de Bateria: {status['energia_bateria']}%")
    decisoes = tomar_decisao(
        status["energia_bateria"], 
        status["consumo_atual"], 
        status["geracao_atual"],
        subsistemas
    )
    for dec in decisoes:
        print(f"-> {dec}")

    # 3. Previsão de Energia (Regressão Linear)
    print("
--- 3. PREVISÃO DE GERAÇÃO FUTURA (REGRESSÃO) ---")
    vento_input = 11.0
    previsao_energia = prever_geracao_eolica(
        vento_input, 
        historico["velocidade_vento"], 
        historico["energia_eolica_gerada"]
    )
    print(f"Entrada: Velocidade do vento prevista = {vento_input} m/s")
    print(f"Saída: Previsão de geração eólica ≈ {previsao_energia} kW")
    print("=" * 60)


if __name__ == "__main__":
    executar_sistema()
