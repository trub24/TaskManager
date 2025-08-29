# Сервис для управления списком задач.

Для локального запуска бекенда:

Клонировать репозиторий и перейти в него в командной строке:

```
https://github.com/trub24/task_tracker.git
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
alembic upgrade head
```

Запустить проект:

```
python main.py
```

Для запуска dockerfile, выполните команды: 

```
docker build -t task_tracker .
```

```
docker run --name task_tracker --rm -p 8000:8000 task_tracker
```