import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_banking_data(num_records=2000):
    np.random.seed(42)
    random.seed(42)
    
    # Dados básicos dos clientes
    ages = np.random.randint(18, 70, num_records)
    incomes = np.random.normal(5000, 2000, num_records)
    incomes = np.clip(incomes, 1000, 15000)
    
    # Score creditício (0-1000)
    credit_scores = np.random.normal(650, 150, num_records)
    credit_scores = np.clip(credit_scores, 300, 850)
    
    # Produtos financeiros
    products = ['Empréstimo Pessoal', 'Cartão de Crédito', 'Financiamento Veicular', 
                'Investimento', 'Consignado', 'Conta Corrente', 'Seguro', 'Previdência']
    
    # Regiões (foco em distribuição brasileira)
    states = ['SP', 'RJ', 'MG', 'RS', 'PR', 'BA', 'SC', 'GO', 'PE', 'CE']
    state_weights = [0.22, 0.09, 0.08, 0.06, 0.06, 0.05, 0.04, 0.04, 0.03, 0.03]
    
    # Canais de atendimento
    channels = ['Digital', 'Agência', 'Telefone', 'Correspondente Bancário']
    
    # Gerar dados
    data = []
    start_date = datetime(2022, 1, 1)
    
    for i in range(num_records):
        product = random.choice(products)
        state = random.choices(states, weights=state_weights, k=1)[0]
        channel = random.choice(channels)
        
        # Valor baseado no produto e renda
        if product == 'Empréstimo Pessoal':
            value = random.uniform(1000, incomes[i] * 10)
        elif product == 'Cartão de Crédito':
            value = random.uniform(500, incomes[i] * 0.3)
        elif product == 'Financiamento Veicular':
            value = random.uniform(15000, 80000)
        elif product == 'Investimento':
            value = random.uniform(1000, 50000)
        elif product == 'Consignado':
            value = random.uniform(1000, incomes[i] * 15)
        elif product in ['Seguro', 'Previdência']:
            value = random.uniform(500, 2000)
        else:
            value = random.uniform(0, 1000)
        
        # Status baseado no score creditício
        default_prob = max(0, min(1, (650 - credit_scores[i]) / 350))
        status = 'Inadimplente' if random.random() < default_prob * 0.3 else 'Adimplente'
        
        # Data aleatória nos últimos 2 anos
        random_date = start_date + timedelta(days=random.randint(0, 730))
        
        data.append({
            'Cliente_ID': i + 10000,
            'Idade': ages[i],
            'Renda_Mensal': round(incomes[i], 2),
            'Score_Credito': round(credit_scores[i]),
            'Produto': product,
            'Valor_Operacao': round(value, 2),
            'Estado': state,
            'Status': status,
            'Data_Operacao': random_date.strftime('%Y-%m-%d'),
            'Canal': channel,
            'Tempo_Relacionamento_Meses': random.randint(1, 120)
        })
    
    return pd.DataFrame(data)

# Gerar e salvar dados
if __name__ == "__main__":
    df = generate_banking_data(3000)
    df.to_csv('data/raw/dados_bancarios.csv', index=False, encoding='utf-8-sig')
    print("Dataset gerado com sucesso!")
    print(f"Shape: {df.shape}")