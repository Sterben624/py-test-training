import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

class WebScraper:
    def _fetch_page(self, url: str, timeout = 10) -> str:
        """Fetch the content of a web page."""
        try:
            response = requests.get(url, timeout=timeout)
            
            # Перевіряємо статус-код вручну
            if response.status_code == 200:
                return response.text
            elif response.status_code == 404:
                raise FileNotFoundError(f"Page not found: {url}")
            elif response.status_code == 403:
                raise PermissionError(f"Access forbidden: {url}")
            elif response.status_code >= 500:
                raise RuntimeError(f"Server error ({response.status_code}): {url}")
            else:
                raise ValueError(f"HTTP error ({response.status_code}): {url}")
                
        except requests.exceptions.Timeout:
            raise TimeoutError(f"Request to {url} timed out")
        except requests.exceptions.ConnectionError:
            raise ConnectionError(f"Failed to connect to {url}")
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Request failed: {url} - {str(e)}")
        
    def find_elements(self, url: str, tag: str) -> list:
        """Find all elements by tag in the HTML content."""
        html_content = self._fetch_page(url)
        if not html_content:
            raise ValueError("No content fetched from the URL")
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup.find_all(tag) 
    
    def find_urls(self, url: str) -> list:
        """Find all URLs in the HTML content."""
        html_content = self._fetch_page(url)
        if not html_content:
            raise ValueError("No content fetched from the URL")
        soup = BeautifulSoup(html_content, 'html.parser')
        list_of_urls = []
        for link in soup.find_all('a', href=True):
            href = link['href']  # Error Only PyLance
            if href and (href.startswith('http://') or href.startswith('https://')):
                list_of_urls.append(href)
        return list_of_urls

if __name__ == "__main__":
    url = "https://www.iana.org/help/example-domains"
    scraper = WebScraper()
    list_of_urls = scraper.find_urls(url)
    print(list_of_urls)

"""
TODO
Функція для витягування тексту з конкретних CSS-селекторів або XPath-виразів.
Метод для завантаження контенту сторінки з обробкою таймаутів та повторних спроб при невдачах.
Варто додати функцію для витягування метаданих сторінки: заголовок, опис, ключові слова.
Потрібен метод для обробки форм на сторінці та витягування інформації про поля форм.
Функція для роботи з таблицями HTML - витягування даних з рядків та стовпців.
Метод для збереження отриманих даних у різних форматах: JSON, CSV, простий текст.
Важливо передбачити обробку помилок: timeout, connection errors, HTTP errors (404, 500),
неправильний HTML. Це дасть можливість вивчити mock-об'єкти для імітації HTTP-відповідей та тестування без реальних мережевих запитів.
"""
