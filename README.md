# 🌿 Habit Tracker

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/SQLAlchemy-2.0-CC292B?style=for-the-badge&logo=sqlalchemy&logoColor=white" alt="SQLAlchemy">
  <img src="https://img.shields.io/badge/JavaScript-Vanilla-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JS">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5">
</p>

> **Habit Tracker** — это легкое, современное асинхронное веб-приложение для отслеживания ежедневных привычек. Проект реализован с использованием классической архитектуры: **FastAPI REST API** на бэкенде и динамический **Single Page Application (SPA)** фронтенд в едином HTML-файле.

---

## 🛠 Технологический стек

### **Backend**
* **Python 3.10+**
* **FastAPI** — асинхронный фреймворк для быстрого создания RESTful API
* **SQLAlchemy 2.0 (AsyncIO)** — ORM для работы с базой данных
* **Pydantic v2** — валидация данных и сериализация
* **Uvicorn** — асинхронный ASGI-сервер

### **Frontend**
* **Vanilla JavaScript (ES6+)** — отправка асинхронных запросов через `fetch`
* **CSS3 & Flexbox/Grid** — адаптивная верстка
* **FontAwesome 6** — векторная иконографика

---

## ⚙️ Быстрый старт

### 1. Клонирование репозитория и установка зависимостей

```bash
# Клонируйте репозиторий
git clone [https://github.com/your-username/habit-tracker.git](https://github.com/your-username/habit-tracker.git)
cd habit-tracker

# Создайте и активируйте виртуальное окружение
python -m venv venv

# Для macOS / Linux:
source venv/bin/activate

# Для Windows:
venv\Scripts\activate

# Установите зависимости
pip install -r requirements.txt
```

### 2. Запуск бэкенда
Запустите сервер разработки Uvicorn:
```bash
uvicorn src.main:app --reload
```
### **Backend**
* **Python 3.10+**
* **FastAPI** — асинхронный фреймворк для быстрого создания RESTful API
* **SQLAlchemy 2.0 (AsyncIO)** — ORM для работы с базой данных
* **Pydantic v2** — валидация данных и сериализация
* **Uvicorn** — асинхронный ASGI-сервер

После запуска сервер будет доступен по следующим адресам:
* **🌐 API Server:** ```http://localhost:8000```
* **📑 Interactive OpenAPI (Swagger) Docs:** ```http://localhost:8000/docs```

### 💽 Инициализация Базы Данных

[!IMPORTANT]
Перед началом работы с приложением обязательно выполните инициализацию БД!
Без выполнения этого шага таблицы в базе данных не будут созданы, и эндпойнты работы с привычками будут возвращать ошибку сервера.

В проекте реализован служебный эндпойнт для автоматического создания (или полная пересборки) метаданных базы данных.

Отправьте POST-запрос на эндпойнт ```/setup_database``` одним из удобных способов:

## Способ 1: Через Swagger UI (Рекомендуется)

0. Перейдите по адресу http://localhost:8000/docs.
1. Раскройте тег ```Установка Базы Данных 💽```.
2. Нажмите Try it out ➔ Execute.
   
## Способ 2: Через cURL

```Bash
curl -X 'POST' 'http://localhost:8000/setup_database' -H 'accept: application/json'
```

[!WARNING]
Данный метод выполняет ```drop_all``` и ```create_all```. Вызов метода полностью очищает существующую БД и создает структуру с нуля!

### 🚀 Запуск Фронтенда
Фронтенд полностью автономен и не требует сборки (Webpack/Vite не нужны).
0. Убедитесь, что сервер FastAPI запущен и принимает запросы на ```http://localhost:8000```.
1. Откройте файл ```index.html``` прямо в вашем браузере (двойным кликом или через расширение Live Server в VS Code).
   
### 📌 Документация REST API

| Метод | HTTP Эндпойнт | Тег / Раздел | Описание |
| :---: | :--- | :--- | :--- |
| `POST` | `/setup_database` | `Установка Базы Данных 💽` | Инициализация / Сброс таблиц базы данных |
| `GET` | `/habits` | `Привычки 🚬` | Получить список всех привычек |
| `POST` | `/habits` | `Привычки 🚬` | Добавить новую привычку |
| `GET` | `/habits/{habit_id}` | `Привычки 🚬` | Получить подробную информацию о привычке по ID |
| `PUT` | `/habits/{habit_id}` | `Привычки 🚬` | Обновить название и описание привычки |
| `PATCH` | `/habits/{habit_id}/toggle` | `Привычки 🚬` | Переключить статус выполнения (`checking`) |
| `DELETE` | `/habits/{habit_id}` | `Привычки 🚬` | Удалить привычку по ID |

### 📝 Схема данных (Habit Model)
Пример JSON-объекта сущности Привычка:

```
JSON
{
  "id": 1,
  "name": "Утренний кросс",
  "description": "Пробежать 3 км в легком темпе",
  "date_created_habit": "2026-07-24",
  "checking": false
}
```
