import requests

def get_files_from_yandex_disk(public_key):
    url = f"https://cloud-api.yandex.net/v1/disk/public/resources?public_key={public_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['_embedded']['items']
    return None

def get_download_link(public_key, path):
    url = f"https://cloud-api.yandex.net/v1/disk/public/resources/download?public_key={public_key}&path={path}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('href')
    return None
