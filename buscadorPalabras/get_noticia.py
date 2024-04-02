import requests
from bs4 import BeautifulSoup

# cambiamos el user-agent para que no nos bloquee la web
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.3'
}

def get_noticia(url = 'https://elpais.com/mexico/2024-01-16/mexico-mantiene-los-altos-niveles-de-violencia-y-registra-30523-asesinatos-en-2023.html'):
  """ 
    Obtiene el texto de una noticia de la web, solo funciona para la web de el pais
    args:
      url: str - url de la noticia
    return:
      str - texto de la noticia 
  """

  # Realizamos la petición a la web
  response = requests.get(url, headers=headers)

  # si no obtenemos una respuesta correcta
  if response.status_code != 200:
    print('Error al obtener la noticia')
    return None
  
  soup = BeautifulSoup(response.text, 'lxml')

  # obtenemos las noticias con xpath //div[@data-dtm-region="articulo_cuerpo"]
  news = soup.find('div', attrs={'data-dtm-region': 'articulo_cuerpo'})

  if news is None:
    print('Error al obtener la noticia')
    return None
  
  # guardamos el texto de la noticia en un archivo con codificación utf-8
  with open('noticia.txt', 'w', encoding='utf-8') as file:
    file.write(news.text)

  return news.text


if __name__ == "__main__":
  text = get_noticia()
  print(text)
