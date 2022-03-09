from bs4 import BeautifulSoup
import lxml
from more_itertools import strip
import requests
from csv import writer


try:
    url = requests.get('https://music.apple.com/us/playlist/top-100-global/pl.d25f5d1181894928af76c85c967f8f31')
    url.raise_for_status()
    content = url.text

    soup = BeautifulSoup(content, 'lxml')

    all_music = soup.find('div', class_='header-and-songs-list')
    music_cards = all_music.find_all('div', class_ = 'songs-list-row songs-list-row--web-preview web-preview songs-list-row--two-lines songs-list-row--song')

    with open('apple_musicchart.csv', 'w', encoding='utf8', newline='') as f:
        the_writer = writer(f)
        headers = ['Song Title', 'Ranking', 'Artist', 'Album', 'Duration']
        the_writer.writerow(headers)
    
        for music_card in music_cards:
            title = music_card.find('div', class_='songs-list-row__song-name').text
            rank = music_card.find('div', class_ = 'songs-list-row__rank').text
            artist = music_card.find('div', class_ = 'songs-list__song-link-wrapper').a.text
            album = music_card.find('div', class_ ='songs-list__col songs-list__col--album typography-body').a.text.strip()
            duration = music_card.find('div', class_='songs-list__col songs-list__col--time typography-body').time.text.strip()
            
            music_info = [title, rank, artist, album, duration]
            the_writer.writerow(music_info)
    

except Exception as e:
    print(e)