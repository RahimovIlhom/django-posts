import requests
from bs4 import BeautifulSoup


def fetch_flickr_data(url):
    """
    Fetches and parses data from a Flickr URL.
    Returns a dictionary with image, title, and artist, or None if parsing fails.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        sourcecode = BeautifulSoup(response.text, 'html.parser')

        image = sourcecode.select_one('meta[content^="https://live.staticflickr.com/"]')
        title = sourcecode.select_one('h1.photo-title')
        artist = sourcecode.select_one('a.owner-name')

        if image and title and artist:
            return {
                'ok': True,
                'data':
                    {
                        'image': image['content'],
                        'title': title.text.strip(),
                        'artist': artist.text.strip()
                    }
                }
        return {'ok': False, 'data': None}
    except requests.RequestException as e:
        return {'ok': False, 'data': f'{e}'}
