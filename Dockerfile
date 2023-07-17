FROM python:3.11

RUN mkdir /app

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR app

# Копируем requirements.txt для установки зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Копируем все файлы проекта в рабочую директорию контейнера
COPY . .

# Запускаем приложение
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]