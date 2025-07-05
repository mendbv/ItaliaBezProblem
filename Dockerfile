# Dockerfile

# Используем базовый образ Python
FROM python:3.10-slim-buster

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем requirements.txt и устанавливаем Python зависимости
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Копируем весь проект в рабочую директорию контейнера
# Это включает папки main/, italia_bez_problem/, static/, media/, locale/ и т.д.
COPY . .

# Собираем статические файлы для продакшена
# Они будут собраны из папок 'static/' приложений и 'STATICFILES_DIRS'
# в директорию, указанную в STATIC_ROOT (/app/staticfiles_collected)
RUN python manage.py collectstatic --noinput

# Открываем порт, на котором будет работать Gunicorn
EXPOSE 8000

# Запускаем Gunicorn как основной процесс приложения
CMD ["gunicorn", "italia_bez_problem.wsgi:application", "--bind", "0.0.0.0:8000"]
