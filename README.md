# _Solvit_Tracker
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
# venv\Scripts\activate

# Установите зависимости
pip install -r requirements.txt
