import telebot
import random
import schedule
import time
from datetime import datetime, timedelta

# Configurações
TOKEN = 'SEU_TOKEN_AQUI'  # Seu token aqui
CANAL_ID = 'SEU_CANAL_ID_AQUI'  # Seu canal aqui

bot = telebot.TeleBot(TOKEN)

# Lista de ativos e direções
ativos = [
    "EUR/USD", "GBP/JPY", "USD/JPY", "AUD/JPY", "GBP/USD", "USD/CHF", "EUR/JPY"
]

direcoes = [
    "🟢 CALL (COMPRA)",
    "🔴 PUT (VENDA)"
]

estrategias = [
    "Análise de Tendência 📈",
    "Suporte e Resistência 🛡️",
    "Rompimento de Velas 🔥",
    "Padrão de Velas 📊"
]

# Função para criar sinal
def criar_sinal():
    ativo = random.choice(ativos)
    direcao = random.choice(direcoes)
    estrategia = random.choice(estrategias)
    minutos_futuros = random.choice([5, 10, 15])
    horario_entrada = (datetime.now() + timedelta(minutes=minutos_futuros)).strftime("%H:%M")

    mensagem = f"""🚀 NOVO SINAL DE OPÇÕES BINÁRIAS 🚀

🪙 Ativo: {ativo}
🕒 Entrada prevista: {horario_entrada}
🎯 Direção: {direcao}

⚠️ Gale 1 permitido
⚡ Estratégia: {estrategia}

⏳ Validade: {minutos_futuros} minutos após o horário!

📢 Gerado automaticamente por @SeuCanal"""
    return mensagem

# Função principal para enviar sinal
def enviar_sinal():
    mensagem = criar_sinal()
    bot.send_message(CANAL_ID, mensagem)
    print("Sinal enviado (normal)")

    # Chance de ativar Modo Turbo (30%)
    if random.random() < 0.3:
        time.sleep(5)  # espera 5 segundos para mandar o segundo
        mensagem_turbo = criar_sinal()
        bot.send_message(CANAL_ID, mensagem_turbo)
        print("🚀 MODO TURBO ativado! Segundo sinal enviado.")

# Agendamento aleatório (5, 10 ou 15 minutos)
def agendar_sinal():
    intervalo = random.choice([5, 10, 15])
    schedule.every(intervalo).minutes.do(enviar_sinal)

# Primeiro agendamento
agendar_sinal()

# Loop infinito
while True:
    schedule.run_pending()
    time.sleep(1)