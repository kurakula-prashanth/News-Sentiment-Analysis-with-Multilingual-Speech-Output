import requests

def fetch_news_data(api_url, company_name):
    """
    Fetch news data for a company from the API
    
    Parameters:
    api_url (str): API endpoint URL
    company_name (str): Name of the company to analyze
    
    Returns:
    tuple: (success (bool), data/error_message (dict/str))
    """
    try:
        response = requests.post(
            f"{api_url}/news",
            json={"company_name": company_name}
        )
        
        if response.status_code == 200:
            data = response.json()
            return True, data["processed_data"]
        else:
            return False, f"Error: {response.json().get('detail', 'Failed to retrieve data')}"
    except Exception as e:
        return False, f"Connection error: {str(e)}"

def generate_audio_summary(api_url, processed_data, language_code):
    """
    Generate audio summary in the specified language
    
    Parameters:
    api_url (str): API endpoint URL
    processed_data (dict): Processed news data
    language_code (str): Language code for the summary
    
    Returns:
    tuple: (success (bool), data/error_message (dict/str))
    """
    try:
        response = requests.post(
            f"{api_url}/audio",
            json={
                "processed_data": processed_data,
                "language_code": language_code
            }
        )
        
        if response.status_code == 200:
            return True, response.json()
        else:
            return False, f"Error: {response.json().get('detail', 'Failed to generate audio')}"
    except Exception as e:
        return False, f"Connection error: {str(e)}"