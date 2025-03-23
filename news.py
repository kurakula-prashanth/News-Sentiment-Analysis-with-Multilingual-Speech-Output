import requests
from bs4 import BeautifulSoup

def get_news_articles(query, num_articles=10):
    """
    Scrape news articles from Bing search results
    
    Parameters:
    query (str): The search query, typically a company name
    num_articles (int): Maximum number of articles to retrieve
    
    Returns:
    list: List of dictionaries containing article information
    """
    search_url = f"https://www.bing.com/news/search?q={query}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }
    response = requests.get(search_url, headers=headers)
    
    if response.status_code != 200:
        print("Failed to retrieve news articles")
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = []
    seen_titles_and_summaries = set()  # Track combinations of title and summary
    
    for item in soup.select(".news-card")[:num_articles]:
        # Extract the title text from the <a> tag with class="title"
        title_tag = item.select_one("a.title")
        if title_tag:
            title = title_tag.text.strip()
            link = title_tag["href"] if title_tag.has_attr("href") else None
        else:
            # Fallback for other potential title elements
            title_tag = item.select_one("a")
            title = title_tag.text.strip() if title_tag else "No title available"
            link = title_tag["href"] if title_tag and title_tag.has_attr("href") else None
        
        summary_tag = item.select_one(".snippet")
        
        if title and link:
            summary = summary_tag.text.strip() if summary_tag else "No summary available"
            
            # Create a combined unique key of title + summary
            unique_key = (title, summary)
            
            # Check if the combination has been seen before to avoid duplicates
            if unique_key not in seen_titles_and_summaries:
                seen_titles_and_summaries.add(unique_key)
                # Using capitalized keys for consistency
                articles.append({"Title": title, "Link": link, "Summary": summary})
    
    return articles