import requests

def get_files_from_yandex_disk(public_key):
    """
    Получение списка файлов из Яндекс.Диска по публичному доступу.

    Args:
        public_key (str): публичный доступ

    Returns:
        list: список файлов, если запрос успешен, None в противном случае
    """
    url = f"https://cloud-api.yandex.net/v1/disk/public/resources?public_key={public_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['_embedded']['items']
    return None

def get_download_link(public_key, path):
    """
    Получение ссылки на скачивание файла из Яндекс.Диска
    по публичному доступу.

    Args:
        public_key (str): публичный доступ
        path (str): путь к файлу

    Returns:
        str: ссылка на скачивание файла, если не удалось - None
    """
    url = f"https://cloud-api.yandex.net/v1/disk/public/resources/download?public_key={public_key}&path={path}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('href')
    else:
        print(f"Ошибка при получении ссылки на скачивание: {response.status_code}")
        return None
