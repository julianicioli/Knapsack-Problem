FROM python:3.11-slim

WORKDIR /app

# Instala as dependências de sistema necessárias para compilar o mysqlclient
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    pkg-config \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia o arquivo de dependências e instala
COPY requisitos.txt .
RUN pip install --no-cache-dir -r requisitos.txt

# Copia todo o resto do código do projeto
COPY . .

# Comando que inicia a aplicação
CMD ["python", "main.py"]