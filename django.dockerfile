# syntax=docker/dockerfile:1
FROM python:3.11-slim

WORKDIR /app

# Set PYTHONPATH if you have apps in /src
ENV PYTHONPATH="${PYTHONPATH}:/app/src"

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    netcat \
    curl \
    nano \
    tree \
    zip \
    unzip \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "bluemoon_mailer.wsgi:application", "--bind", "0.0.0.0:8000"]
