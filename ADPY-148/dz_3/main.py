import requests
from bs4 import BeautifulSoup
import re

# Определяем список ключевых слов
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

# URL страницы со свежими статьями
URL = 'https://habr.com/ru/articles/'

def fetch_habr_articles(url, keywords):
    """
    Парсинг статей с Habr по ключевым словам
    """
    # Заголовки для имитации браузера
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"❌ Ошибка при загрузке страницы: {e}")
        return []

    # Используем html.parser
    soup = BeautifulSoup(response.text, 'html.parser')

    # Находим все статьи на странице
    articles = soup.find_all('article')
    
    if not articles:
        print("⚠️ Статьи не найдены. Возможно, изменилась структура страницы.")
        return []

    result = []

    for article in articles:
        try:
            # Извлекаем заголовок
            title_tag = article.find('h2') or article.find('h1')
            if not title_tag:
                continue
            title = title_tag.get_text(strip=True)

            # Ищем ссылку на статью
            # Ищем тег a с классом, который обычно используется для ссылок на статьи
            link_tag = None
            
            # Пробуем найти ссылку на статью разными способами
            # 1. Ищем a с классом tm-title__link (часто используется на Habr)
            link_tag = article.find('a', class_=re.compile(r'tm-title__link|post__title_link'))
            
            # 2. Если не нашли, ищем любую ссылку внутри h2
            if not link_tag:
                h2 = article.find('h2')
                if h2:
                    link_tag = h2.find('a', href=True)
            
            # 3. Если всё ещё не нашли, ищем первую ссылку в статье
            if not link_tag:
                link_tag = article.find('a', href=True)
            
            if not link_tag:
                continue
                
            link = link_tag.get('href')
            # Формируем полную ссылку
            if link.startswith('/'):
                link = 'https://habr.com' + link

            # Извлекаем дату
            date_tag = article.find('time')
            date_text = date_tag.get_text(strip=True) if date_tag else 'Дата не указана'

            # Извлекаем текст превью
            preview_text = article.get_text(' ', strip=True)

            # Проверяем наличие ключевых слов
            combined_text = (title + ' ' + preview_text).lower()
            found_keywords = [kw for kw in keywords if kw.lower() in combined_text]

            # Если найдено хотя бы одно ключевое слово
            if found_keywords:
                result.append({
                    'title': title,
                    'link': link,
                    'date': date_text,
                    'keywords': found_keywords
                })

        except Exception as e:
            print(f"⚠️ Ошибка при обработке статьи: {e}")
            continue

    return result

def main():
    print("🔍 Начинаем парсинг Habr...")
    print(f"📝 Ключевые слова: {', '.join(KEYWORDS)}")
    print("-" * 80)

    articles = fetch_habr_articles(URL, KEYWORDS)

    print("\n" + "=" * 80)
    print("📋 РЕЗУЛЬТАТЫ:")
    print("=" * 80)

    if articles:
        print(f"✅ Найдено статей: {len(articles)}")
        print("-" * 80)
        
        for i, article in enumerate(articles, 1):
            # Вывод в формате: <дата> – <заголовок> – <ссылка>
            print(f"{i}. {article['date']} – {article['title']}")
            print(f"   🔗 {article['link']}")
            print(f"   📌 Ключевые слова: {', '.join(article['keywords'])}")
            print("-" * 80)
    else:
        print("❌ Статьи с указанными ключевыми словами не найдены.")
        print("💡 Попробуйте изменить ключевые слова или проверить соединение с интернетом.")

if __name__ == '__main__':
    main()
