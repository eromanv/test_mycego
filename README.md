# Django Yandex Disk File Downloader

Этот проект позволяет пользователям получать доступ к файлам с Яндекс.Диска с помощью публичного ключа и загружать их. Приложение предоставляет простой интерфейс, где пользователи могут ввести публичную ссылку на Яндекс.Диск и получить список доступных файлов для загрузки.

## Функциональность

- Получение списка файлов с Яндекс.Диска по публичному ключу.
- Загрузка файлов напрямую из списка.
- Простой и адаптивный интерфейс на базе Bootstrap.

## Установка

1. **Клонируйте репозиторий:**

    ```bash
    git clone https://github.com/ваш-username/django-yandex-disk-downloader.git
    ```

2. **Перейдите в директорию проекта:**

    ```bash
    cd django-yandex-disk-downloader
    ```

3. **Создайте и активируйте виртуальное окружение:**

    ```bash
    python3 -m venv env
    source env/bin/activate  # Для Windows используйте `env\Scripts\activate`
    ```

4. **Установите необходимые зависимости:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Примените миграции:**

    ```bash
    python manage.py migrate
    ```

6. **Запустите сервер разработки:**

    ```bash
    python manage.py runserver
    ```

7. **Откройте приложение в браузере:**

    Перейдите по адресу `http://127.0.0.1:8000/`, чтобы начать работу с приложением.

## Использование

1. Введите публичную ссылку (публичный ключ) от Яндекс.Диска в форму.
2. Нажмите кнопку "Получить список файлов".
3. Отобразится список файлов, каждый из которых будет иметь кнопку для скачивания.
4. Нажмите "Скачать", чтобы загрузить нужный файл.

## Детали проекта
Фреймворк: Django
Фронтенд: Bootstrap 5
Внешний API: Публичный API Яндекс.Диска

Автор: Егоров Роман
