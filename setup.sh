#!/bin/bash

# =========================================

# Setup automático para o projeto Video Cleaner

# Autor: Vinícius

# =========================================

echo "==== Iniciando configuração do ambiente ===="

# Verifica se o Python 3 está instalado

if ! command -v python3 &>/dev/null; then
echo "Python3 não encontrado. Instalando..."
sudo apt update && sudo apt install -y python3 python3-venv python3-pip
fi

# Verifica se o FFmpeg está instalado

if ! command -v ffprobe &>/dev/null; then
echo "FFmpeg não encontrado. Instalando..."
sudo apt update && sudo apt install -y ffmpeg
fi

# Cria o ambiente virtual

if [ ! -d "venv" ]; then
echo "Criando ambiente virtual..."
python3 -m venv venv
else
echo "Ambiente virtual já existe."
fi

# Ativa o ambiente virtual

source venv/bin/activate

# Instala dependências

echo "Instalando dependências..."
pip install --upgrade pip
pip install -r requirements.txt

# Executa o programa principal

echo "==== Ambiente configurado com sucesso ===="
echo "Executando o programa..."
python main.py
