FROM python:3.13-slim

WORKDIR /app

# Устанавливаем необходимые системные зависимости для сборки и работы приложения.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential \
    && rm -rf /var/lib/apt/lists/*

# Копируем файлы, необходимые для установки зависимостей,
COPY pyproject.toml requirements.txt /app/

# и устанавливаем их в виртуальном окружении.
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы приложения в контейнер.
COPY . /app

ENV PYTHONUNBUFFERED=1
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
