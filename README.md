# Sistema Integrado de Gestão Energética da Colônia (Fase 3)

Este repositório contém o código-fonte desenvolvido para a Fase 3 do projeto acadêmico de Gestão da Colônia. O objetivo do sistema é monitorar os recursos energéticos da colônia, prever a geração de energia a partir do vento e tomar decisões automatizadas para economizar energia e garantir o funcionamento do Suporte à Vida.

## Funcionalidades do Sistema

1. **Organização de Dados**: Estruturação dos dados operacionais e dos subsistemas em dicionários e listas nativas em Python, divididos por nível de importância.
2. **Análise de Eficiência**: Comparação simples entre a geração e o consumo atual para indicar sobra ou falta de energia.
3. **Decisão Automatizada**: Aplicação de regras condicionais (operadores booleanos) para desligar equipamentos secundários (laboratório, iluminação externa) e priorizar o Suporte à Vida quando a bateria estiver baixa.
4. **Previsão por Regressão Linear**: Cálculo da reta de regressão simples ($y = a \cdot x + b$) por Mínimos Quadrados sem uso de bibliotecas externas para estimar a geração eólica com base na velocidade do vento.

## Como Executar o Projeto

1. Baixar o arquivo `sistema_colonia.py`.
2. Abrir o terminal ou a IDE de sua preferência.
3. Executar o script com o comando `python sistema_colonia.py`.

## Exemplo de Entrada e Saída

### Entrada de Teste:
* **Nível da Bateria**: 40%
* **Geração Atual**: 45.0 kW
* **Consumo Atual**: 70.0 kW
* **Vento Previsto**: 11.0 m/s

### Saída Esperada no Terminal:

```text
============================================================
      SISTEMA INTEGRADO DE GESTÃO DA COLÔNIA - FASE 3
============================================================

--- 1. ANÁLISE DE EFICIÊNCIA ENERGÉTICA ---
Geração Atual: 45.0 kW | Consumo Atual: 70.0 kW
Diagnóstico: ALERTA: Consumo maior que a geração! Deficit de 25.0 kW.

--- 2. TOMADA DE DECISÃO AUTOMATIZADA ---
Nível de Bateria: 40.0%
-> MODO ECONOMIA ATIVADO: Reduzir consumo de energia imediatamente.
-> AÇÃO: Desligando sistemas não essenciais: laboratorio_pesquisa, iluminacao_externa, estufa_secundaria.
-> MANTER LIGADO: Priorizando Suporte à Vida: oxigenio, aquecimento, pressurizacao.

--- 3. PREVISÃO DE GERAÇÃO FUTURA (REGRESSÃO) ---
Entrada: Velocidade do vento prevista = 11.0 m/s
Saída: Previsão de geração eólica ≈ 27.5 kW
============================================================
```
