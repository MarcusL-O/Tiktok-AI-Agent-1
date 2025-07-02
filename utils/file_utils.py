import requests

def save_image_from_url(url, path):
    response = requests.get(url)
    with open(path, 'wb') as f:
        f.write(response.content)
