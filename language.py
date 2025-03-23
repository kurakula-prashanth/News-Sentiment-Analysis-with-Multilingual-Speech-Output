LANGUAGE_CODES = {
    "1": {"name": "Telugu", "code": "te"},
    "2": {"name": "Hindi", "code": "hi"},
    "3": {"name": "English", "code": "en"},
    "4": {"name": "Malayalam", "code": "ml"},
    "5": {"name": "Tamil", "code": "ta"},
    "6": {"name": "Kannada", "code": "kn"}
}

def translate_sentiment_analysis(final_sentiment, language_code):
    """
    Translate the final sentiment analysis to the specified language
    
    Parameters:
    final_sentiment (str): The final sentiment analysis in English
    language_code (str): Language code
    
    Returns:
    str: Translated sentiment analysis
    """
    # Check for common patterns in sentiment analysis and translate them
    translated_sentiment = final_sentiment
    
    # For Telugu
    if language_code == "te":
        if "predominantly positive" in final_sentiment:
            return "వార్తలు ప్రధానంగా సానుకూలంగా ఉన్నాయి. " + \
                   final_sentiment.replace("Positive news about ", "").replace(" is particularly noteworthy.", " గురించి సానుకూల వార్తలు ప్రత్యేకంగా గమనార్హమైనవి.")
        elif "significant concerns" in final_sentiment:
            return "వార్తలు గణనీయమైన ఆందోళనలను చూపిస్తున్నాయి, ముఖ్యంగా " + \
                   final_sentiment.replace("Coverage shows significant concerns, particularly regarding ", "") + " విషయంలో."
        elif "cautiously positive" in final_sentiment:
            return "వార్తలు జాగ్రత్తగా సానుకూలంగా ఉన్నాయి, కొన్ని ఆందోళనలు " + \
                   final_sentiment.replace("Coverage is cautiously positive, with some concerns noted about ", "") + " గురించి గమనించబడ్డాయి."
        elif "leans negative" in final_sentiment:
            return "వార్తలు ప్రతికూలంగా మొగ్గు చూపుతున్నాయి, అయినప్పటికీ " + \
                   final_sentiment.replace("Coverage leans negative, though there are some positive developments in ", "") + " లో కొన్ని సానుకూల పరిణామాలు ఉన్నాయి."
        elif "mixed or neutral" in final_sentiment:
            return "వార్తలు మిశ్రమంగా లేదా తటస్థంగా ఉన్నాయి, " + \
                   final_sentiment.replace("Coverage is mixed or neutral, with balanced perspectives on ", "") + " పై సంతులిత దృక్కోణాలతో."
    
    # For Hindi
    elif language_code == "hi":
        if "predominantly positive" in final_sentiment:
            return "कवरेज मुख्य रूप से सकारात्मक है। " + \
                  final_sentiment.replace("Positive news about ", "").replace(" is particularly noteworthy.", " के बारे में सकारात्मक खबरें विशेष रूप से उल्लेखनीय हैं।")
        elif "significant concerns" in final_sentiment:
            return "कवरेज महत्वपूर्ण चिंताओं को दर्शाता है, विशेष रूप से " + \
                  final_sentiment.replace("Coverage shows significant concerns, particularly regarding ", "") + " के संबंध में।"
        elif "cautiously positive" in final_sentiment:
            return "कवरेज सावधानीपूर्वक सकारात्मक है, कुछ चिंताएं " + \
                  final_sentiment.replace("Coverage is cautiously positive, with some concerns noted about ", "") + " के बारे में नोट की गई हैं।"
        elif "leans negative" in final_sentiment:
            return "कवरेज नकारात्मक झुकाव वाला है, हालांकि " + \
                  final_sentiment.replace("Coverage leans negative, though there are some positive developments in ", "") + " में कुछ सकारात्मक विकास हैं।"
        elif "mixed or neutral" in final_sentiment:
            return "कवरेज मिश्रित या तटस्थ है, " + \
                  final_sentiment.replace("Coverage is mixed or neutral, with balanced perspectives on ", "") + " पर संतुलित दृष्टिकोण के साथ।"
    
    # For Malayalam
    elif language_code == "ml":
        if "predominantly positive" in final_sentiment:
            return "കവറേജ് പ്രധാനമായും പോസിറ്റീവാണ്. " + \
                final_sentiment.replace("Positive news about ", "").replace(" is particularly noteworthy.", " എന്നതിനെക്കുറിച്ചുള്ള പോസിറ്റീവ് വാർത്തകൾ പ്രത്യേകിച്ച് ശ്രദ്ധേയമാണ്.")
        elif "significant concerns" in final_sentiment:
            return "വാർത്താ കവറേജ് ഗണ്യമായ ആശങ്കകൾ കാണിക്കുന്നു, പ്രത്യേകിച്ച് " + \
                final_sentiment.replace("Coverage shows significant concerns, particularly regarding ", "") + " സംബന്ധിച്ച്."
        elif "cautiously positive" in final_sentiment:
            return "കവറേജ് ജാഗ്രതയോടെ പോസിറ്റീവാണ്, " + \
                final_sentiment.replace("Coverage is cautiously positive, with some concerns noted about ", "") + " എന്നതിനെക്കുറിച്ച് ചില ആശങ്കകൾ രേഖപ്പെടുത്തിയിട്ടുണ്ട്."
        elif "leans negative" in final_sentiment:
            return "കവറേജ് നെഗറ്റീവിലേക്ക് ചായുന്നു, എന്നിരുന്നാലും " + \
                final_sentiment.replace("Coverage leans negative, though there are some positive developments in ", "") + " എന്നതിൽ ചില പോസിറ്റീവ് പുരോഗതികളുണ്ട്."
        elif "mixed or neutral" in final_sentiment:
            return "കവറേജ് മിശ്രിതമോ നിഷ്പക്ഷമോ ആണ്, " + \
                final_sentiment.replace("Coverage is mixed or neutral, with balanced perspectives on ", "") + " എന്നതിനെക്കുറിച്ച് സന്തുലിതമായ കാഴ്ചപ്പാടുകളോടെ."

    # For Tamil
    elif language_code == "ta":
        if "predominantly positive" in final_sentiment:
            return "உள்ளடக்கம் பெரும்பாலும் நேர்மறையானது. " + \
                final_sentiment.replace("Positive news about ", "").replace(" is particularly noteworthy.", " பற்றிய நேர்மறை செய்திகள் குறிப்பிடத்தக்கவை.")
        elif "significant concerns" in final_sentiment:
            return "செய்தி உள்ளடக்கம் குறிப்பிடத்தக்க கவலைகளைக் காட்டுகிறது, குறிப்பாக " + \
                final_sentiment.replace("Coverage shows significant concerns, particularly regarding ", "") + " தொடர்பாக."
        elif "cautiously positive" in final_sentiment:
            return "உள்ளடக்கம் எச்சரிக்கையுடன் நேர்மறையாக உள்ளது, " + \
                final_sentiment.replace("Coverage is cautiously positive, with some concerns noted about ", "") + " பற்றி சில கவலைகள் குறிப்பிடப்பட்டுள்ளன."
        elif "leans negative" in final_sentiment:
            return "உள்ளடக்கம் எதிர்மறையாக சாய்கிறது, இருப்பினும் " + \
                final_sentiment.replace("Coverage leans negative, though there are some positive developments in ", "") + " இல் சில நேர்மறையான முன்னேற்றங்கள் உள்ளன."
        elif "mixed or neutral" in final_sentiment:
            return "உள்ளடக்கம் கலப்பு அல்லது நடுநிலையாக உள்ளது, " + \
                final_sentiment.replace("Coverage is mixed or neutral, with balanced perspectives on ", "") + " பற்றிய சமநிலையான கண்ணோட்டங்களுடன்."

    # For Kannada
    elif language_code == "kn":
        if "predominantly positive" in final_sentiment:
            return "ವರದಿಯು ಪ್ರಮುಖವಾಗಿ ಸಕಾರಾತ್ಮಕವಾಗಿದೆ. " + \
                final_sentiment.replace("Positive news about ", "").replace(" is particularly noteworthy.", " ಬಗ್ಗೆ ಸಕಾರಾತ್ಮಕ ಸುದ್ದಿಗಳು ವಿಶೇಷವಾಗಿ ಗಮನಾರ್ಹವಾಗಿವೆ.")
        elif "significant concerns" in final_sentiment:
            return "ವರದಿಯು ಗಣನೀಯ ಕಳವಳಗಳನ್ನು ತೋರಿಸುತ್ತದೆ, ವಿಶೇಷವಾಗಿ " + \
                final_sentiment.replace("Coverage shows significant concerns, particularly regarding ", "") + " ಕುರಿತು."
        elif "cautiously positive" in final_sentiment:
            return "ವರದಿಯು ಎಚ್ಚರಿಕೆಯಿಂದ ಸಕಾರಾತ್ಮಕವಾಗಿದೆ, " + \
                final_sentiment.replace("Coverage is cautiously positive, with some concerns noted about ", "") + " ಬಗ್ಗೆ ಕೆಲವು ಕಳವಳಗಳನ್ನು ಗಮನಿಸಲಾಗಿದೆ."
        elif "leans negative" in final_sentiment:
            return "ವರದಿಯು ನಕಾರಾತ್ಮಕತೆಯ ಕಡೆಗೆ ವಾಲುತ್ತದೆ, ಆದರೂ " + \
                final_sentiment.replace("Coverage leans negative, though there are some positive developments in ", "") + " ನಲ್ಲಿ ಕೆಲವು ಸಕಾರಾತ್ಮಕ ಬೆಳವಣಿಗೆಗಳಿವೆ."
        elif "mixed or neutral" in final_sentiment:
            return "ವರದಿಯು ಮಿಶ್ರಿತ ಅಥವಾ ತಟಸ್ಥವಾಗಿದೆ, " + \
                final_sentiment.replace("Coverage is mixed or neutral, with balanced perspectives on ", "") + " ಕುರಿತು ಸಮತೋಲಿತ ದೃಷ್ಟಿಕೋನಗಳೊಂದಿಗೆ."
        
        # Return original for English or if no translation available
        return final_sentiment

def translate_summary(processed_data, language_code):
    """
    Generate a summary in the specified language
    
    Parameters:
    processed_data (dict): The processed news data with sentiment analysis
    language_code (str): Language code
    
    Returns:
    str: Translated summary text
    """
    company_name = processed_data["Company"]
    
    # Get sentiment distribution
    distribution = processed_data["Comparative Sentiment Score"]["Sentiment Distribution"]
    positive_count = distribution["Positive"]
    negative_count = distribution["Negative"]
    neutral_count = distribution["Neutral"]
    
    # Get final sentiment analysis and translate it
    final_sentiment = processed_data["Final Sentiment Analysis"]
    translated_sentiment = translate_sentiment_analysis(final_sentiment, language_code)
    
    # Get common topics
    common_topics = processed_data["Comparative Sentiment Score"]["Topic Overlap"]["Common Topics"]
    topics_text = ', '.join(common_topics[:3]) if common_topics else "No common topics found"
    
    # Basic translations based on language code
    if language_code == "hi":  # Hindi
        if "No common topics found" in topics_text:
            topics_text = "कोई सामान्य विषय नहीं मिला"
            
        summary = f"""
        {company_name} के बारे में समाचार विश्लेषण:
        
        हमने {len(processed_data["Articles"])} समाचार लेखों का विश्लेषण किया है।
        
        सकारात्मक लेख: {positive_count}
        नकारात्मक लेख: {negative_count}
        तटस्थ लेख: {neutral_count}
        
        समग्र विश्लेषण: {translated_sentiment}
        
        मुख्य विषय: {topics_text}
        """
    elif language_code == "te":  # Telugu
        if "No common topics found" in topics_text:
            topics_text = "సామాన్య అంశాలు కనుగొనబడలేదు"
            
        summary = f"""
        {company_name} గురించి వార్తా విశ్లేషణ:
        
        మేము {len(processed_data["Articles"])} వార్తా కథనాలను విశ్లేషించాము.
        
        సానుకూల వార్తలు: {positive_count}
        ప్రతికూల వార్తలు: {negative_count}
        తటస్థ వార్తలు: {neutral_count}
        
        మొత్తం విశ్లేషణ: {translated_sentiment}
        
        ప్రధాన అంశాలు: {topics_text}
        """
    elif language_code == "ml":  # Malayalam
        if "No common topics found" in topics_text:
            topics_text = "പൊതുവായ വിഷയങ്ങളൊന്നും കണ്ടെത്തിയില്ല"
            
        summary = f"""
        {company_name} എന്നതിനെക്കുറിച്ചുള്ള വാർത്താ വിശകലനം:
        
        ഞങ്ങൾ {len(processed_data["Articles"])} വാർത്താ ലേഖനങ്ങൾ വിശകലനം ചെയ്തു.
        
        പോസിറ്റീവ് ലേഖനങ്ങൾ: {positive_count}
        നെഗറ്റീവ് ലേഖനങ്ങൾ: {negative_count}
        നിഷ്പക്ഷ ലേഖനങ്ങൾ: {neutral_count}
        
        സമഗ്ര വിശകലനം: {translated_sentiment}
        
        പ്രധാന വിഷയങ്ങൾ: {topics_text}
        """
    elif language_code == "ta":  # Tamil
        if "No common topics found" in topics_text:
            topics_text = "பொதுவான தலைப்புகள் எதுவும் கண்டுபிடிக்கப்படவில்லை"
            
        summary = f"""
        {company_name} பற்றிய செய்தி பகுப்பாய்வு:
        
        நாங்கள் {len(processed_data["Articles"])} செய்தி கட்டுரைகளை ஆய்வு செய்துள்ளோம்.
        
        நேர்மறை கட்டுரைகள்: {positive_count}
        எதிர்மறை கட்டுரைகள்: {negative_count}
        நடுநிலை கட்டுரைகள்: {neutral_count}
        
        ஒட்டுமொத்த பகுப்பாய்வு: {translated_sentiment}
        
        முக்கிய தலைப்புகள்: {topics_text}
        """
    elif language_code == "kn":  # Kannada
        if "No common topics found" in topics_text:
            topics_text = "ಯಾವುದೇ ಸಾಮಾನ್ಯ ವಿಷಯಗಳು ಕಂಡುಬಂದಿಲ್ಲ"
            
        summary = f"""
        {company_name} ಕುರಿತು ಸುದ್ದಿ ವಿಶ್ಲೇಷಣೆ:
        
        ನಾವು {len(processed_data["Articles"])} ಸುದ್ದಿ ಲೇಖನಗಳನ್ನು ವಿಶ್ಲೇಷಿಸಿದ್ದೇವೆ.
        
        ಸಕಾರಾತ್ಮಕ ಲೇಖನಗಳು: {positive_count}
        ನಕಾರಾತ್ಮಕ ಲೇಖನಗಳು: {negative_count}
        ತಟಸ್ಥ ಲೇಖನಗಳು: {neutral_count}
        
        ಒಟ್ಟಾರೆ ವಿಶ್ಲೇಷಣೆ: {translated_sentiment}
        
        ಪ್ರಮುಖ ವಿಷಯಗಳು: {topics_text}
        """
    else:  # English (default)
        summary = f"""
        News analysis for {company_name}:
        
        We have analyzed {len(processed_data["Articles"])} news articles.
        
        Positive articles: {positive_count}
        Negative articles: {negative_count}
        Neutral articles: {neutral_count}
        
        Overall analysis: {final_sentiment}
        
        Main topics: {topics_text}
        """
    
    return summary