# Paritet Test Task

Проект представляет собой веб-приложение, разработанное с использованием Django (бэкенд) и Vue.js (фронтенд).

## Структура проекта

```
├── frontend/           # Vue.js фронтенд приложение
├── images_manager/     # Django приложение для управления изображениями
├── test_task/         # Основной проект Django
├── templates/         # HTML шаблоны
├── manage.py         # Скрипт управления Django
└── requirements.txt  # Зависимости Python
```

## Требования

- Python 3.8+
- Node.js 14+
- npm или yarn

## Установка и запуск

### Бэкенд (Django)

1. Создайте и активируйте виртуальное окружение:
```bash
python -m venv .venv
source .venv/bin/activate  # для Linux/Mac
.venv\Scripts\activate     # для Windows
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Примените миграции:
```bash
python manage.py migrate
```

4. Запустите сервер разработки:
```bash
python manage.py runserver
```

### Фронтенд (Vue.js)

1. Перейдите в директорию frontend:
```bash
cd frontend
```

2. Установите зависимости:
```bash
npm install
# или
yarn install
```

3. Запустите сервер разработки:
```bash
npm run serve
# или
yarn serve
```

## Использование

После запуска обоих серверов:
- Бэкенд будет доступен по адресу: http://localhost:8000
- Фронтенд будет доступен по адресу: http://localhost:5173

## API Endpoints

### Управление изображениями

#### Загрузка изображения
- **URL**: `/api/images/upload/`
- **Метод**: `POST`
- **Описание**: Загрузка нового изображения с описанием
- **Тело запроса**:
  ```json
  {
    "image_data": "base64_encoded_image_string",
    "description": "Описание изображения"
  }
  ```

#### Получение списка изображений
- **URL**: `/api/images/list/`
- **Метод**: `GET`
- **Описание**: Получение списка всех загруженных изображений
- **Ответ**: Массив объектов изображений с полями:
  ```json
  {
    "id": "integer",
    "description": "string",
    "image_data": "string",
    "uploaded_at": "datetime"
  }
  ```

#### Удаление изображения
- **URL**: `/api/images/{id}/`
- **Метод**: `DELETE`
- **Описание**: Удаление изображения по его ID

### Документация API

API документация доступна в следующих форматах:
- Swagger UI: http://localhost:8000/api/docs/swagger/
- ReDoc: http://localhost:8000/api/docs/redoc/
- OpenAPI схема: http://localhost:8000/api/schema/

