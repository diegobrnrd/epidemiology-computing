import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# ==========================================
# 1. Parâmetros e Condições Iniciais
# ==========================================

N = 500000                   # População total da simulação
R0_estimado = 2.5            # Número Básico de Reprodução (R0)
tempo_incubacao = 5.2        # Tempo médio de incubação em dias
tempo_infeccioso = 10.0      # Tempo médio de infecção em dias

# Cálculo das taxas diárias
sigma = 1.0 / tempo_incubacao   # Taxa de progressão de Exposto para Infectado
gamma = 1.0 / tempo_infeccioso  # Taxa de recuperação
beta = R0_estimado * gamma      # Taxa de transmissão

# Condições iniciais
I0 = 10              # Casos iniciais importados/infecciosos
E0 = 20              # Pessoas já expostas ao vírus
R_inicial = 0               # Zero recuperados no dia 0
S0 = N - I0 - E0 - R_inicial # O restante da população é suscetível

y0 = (S0, E0, I0, R_inicial)

# Tempo de simulação (200 dias para ver a curva completa)
dias_simulacao = 200
t = np.linspace(0, dias_simulacao, dias_simulacao + 1)

# ==========================================
# 2. Definição do Modelo Matemático SEIR
# ==========================================

def modelo_seir(y, t, N, beta, sigma, gamma):
    S, E, I, R = y
    
    # Equações diferenciais
    dSdt = -beta * S * I / N
    dEdt = (beta * S * I / N) - (sigma * E)
    dIdt = (sigma * E) - (gamma * I)
    dRdt = gamma * I
    
    return dSdt, dEdt, dIdt, dRdt

# ==========================================
# 3. Execução e Plotagem
# ==========================================

# Resolvendo o sistema de equações diferenciais
solucao = odeint(modelo_seir, y0, t, args=(N, beta, sigma, gamma))
S, E, I, R = solucao.T

# Configuração do gráfico
plt.figure(figsize=(10, 6))
plt.plot(t, S, label='Suscetíveis', color='#2ca02c', linewidth=2)
plt.plot(t, E, label='Expostos', color='#ff7f0e', linestyle='--', linewidth=2)
plt.plot(t, I, label='Infectados', color='#d62728', linewidth=2)
plt.plot(t, R, label='Recuperados', color='#1f77b4', linewidth=2)

plt.title('Dinâmica de Propagação da COVID-19 (Modelo SEIR)', fontsize=14)
plt.xlabel('Dias desde o início do surto', fontsize=12)
plt.ylabel('Número de Indivíduos', fontsize=12)
plt.legend(loc='center right')
plt.grid(True, linestyle=':', alpha=0.7)
plt.tight_layout()
plt.show()

# ==========================================
# 4. Saída de Dados no Console
# ==========================================
print("=== Resumo dos Parâmetros da Simulação ===")
print(f"População Total (N): {N:,}".replace(',', '.'))
print(f"Número Básico de Reprodução (R0): {R0_estimado}")
print(f"Taxa de Transmissão (beta): {beta:.4f}")
print(f"Taxa de Incubação (sigma): {sigma:.4f} ({tempo_incubacao} dias)")
print(f"Taxa de Recuperação (gamma): {gamma:.4f} ({tempo_infeccioso} dias)")
print("==========================================")