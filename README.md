# _Solvit_Tracker
🌿 Habit Tracker (Трекер привычек)
Лаконичное асинхронное веб-приложение для отслеживания ежедневных привычек. Проект состоит из бэкенда на FastAPI + SQLAlchemy и современного SPA фронтенда в одном HTML-файле.
🛠 Технологический стек
Backend
Python 3.10+
FastAPI — асинхронный веб-фреймворк для создания REST API
SQLAlchemy 2.0 (AsyncIO) — ORM для работы с базой данных
SQLite / PostgreSQL — СУБД для хранения данных
Uvicorn — ASGI-сервер
Frontend
Vanilla JS (ES6+) — логика взаимодействия с API (fetch)
HTML5 & CSS3 (Flexbox/Grid, адаптивная верстка)
FontAwesome 6 — векторные иконки
⚙️ Быстрый старт
1. Клонирование репозитория и установка зависимостей
Bash
git clone https://github.com/your-username/habit-tracker.git
cd habit-tracker

# Создание и активация виртуального окружения
python -m venv venv
source venv/bin/activate  # Для macOS/Linux
# venv\Scripts\activate   # Для Windows

# Установка зависимостей
pip install -r requirements.txt
2. Запуск бэкенда
Запустите ASGI-сервер Uvicorn:
Bash
uvicorn main:app --reload
Сервер доступен по адресу: http://localhost:8000
Документация Swagger UI: http://localhost:8000/docs
💽 Инициализация Базы Данных
ВАЖНО! Перед началом работы с приложением необходимо инициализировать структуру базы данных.
В проекте предусмотрен специальный служебный эндпойнт для автоматического создания (или полного сброса) всех необходимых таблиц на основе описанных SQLAlchemy-моделей.
Выполните POST-запрос на эндпойнт /setup_database.
Сделать это можно двумя способами:
Через Swagger UI (Самый простой способ):
Перейдите в браузере по адресу: http://localhost:8000/docs
Найдите раздел «Установка Базы Данных 💽»
Раскройте POST /setup_database, нажмите Try it out → Execute.
Через cURL из терминала:
Bash
curl -X 'POST' 'http://localhost:8000/setup_database' -H 'accept: application/json'
Примечание: этот метод полностью пересоздает структуру таблиц (drop_all + create_all). Используйте его при первом запуске или когда требуется очистить БД.
🚀 Запуск Фронтенда
Фронтенд выполнен в виде единого автономного файла.
Убедитесь, что бэкенд запущен на http://localhost:8000.
Откройте файл index.html напрямую в любом браузере (или воспользуйтесь расширением Live Server в VS Code).
📌 API Эндпойнты
Метод	Эндпойнт	Описание
POST	/setup_database	Инициализация / сброс таблиц в базе данных
GET	/habits	Получить список всех привычек
POST	/habits	Создать новую привычку
GET	/habits/{habit_id}	Получить привычку по ID
PUT	/habits/{habit_id}	Обновить имя и описание привычки по ID
PATCH	/habits/{habit_id}/toggle	Переключить статус выполнения (checking)
DELETE	/habits/{habit_id}	Удалить привычку по ID
📝 Структура модели Привычки (Habit)
JSON
{
  "id": 1,
  "name": "Утренняя зарядка",
  "description": "15 минут легкой растяжки",
  "date_created_habit": "2026-07-24",
  "checking": false
}
