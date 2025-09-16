# Dashboard Bancário - Power BI

![Power BI](https://img.shields.io/badge/Power%20BI-Data%20Visualization-blue)
![Python](https://img.shields.io/badge/Python-Data%20Processing-yellow)
![DAX](https://img.shields.io/badge/DAX-Analytics-green)

Este projeto consiste em um **dashboard analítico desenvolvido no Power BI** para análise de operações bancárias simuladas, com foco em **performance por produto e região, monitoramento de inadimplência, segmentação de clientes e análise temporal**. O dataset foi gerado artificialmente com Python, simulando dados reais do setor bancário.

## Tecnologias Utilizadas

- **Power BI Desktop**: Visualização e análise de dados  
- **Python**: Geração do dataset simulado  
- **DAX**: Cálculos avançados e criação de KPIs  
- **Power Query**: Transformação e preparação dos dados  

## Estrutura de Pastas

projeto-powerbi-bancario/
│
├── data/
│ ├── raw/ # Dados brutos gerados
│ └── processed/ # Dados transformados
├── scripts/
│ └── data_generation.py # Script para gerar dados simulados
├── powerbi/
│ └── dashboard_bancario.pbix # Arquivo do Power BI
└── images/ # Imagens ou screenshots do dashboard

## Preparação do Ambiente

Crie o diretório e o ambiente virtual:

mkdir projeto-powerbi-bancario
cd projeto-powerbi-bancario
python -m venv venv

# Ativar ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependências
pip install pandas numpy matplotlib seaborn
