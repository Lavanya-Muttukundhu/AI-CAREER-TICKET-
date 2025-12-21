from textblob import TextBlob

def categorize_ticket(user_input):
    analysis = TextBlob(user_input)
    sentiment = analysis.sentiment.polarity  # Range is -1 (angry) to 1 (happy)
    
    user_input = user_input.lower()
    
    # Advanced Category Logic
    if any(word in user_input for word in ["login", "password", "account", "access"]):
        category = "Access & Security"
    elif any(word in user_input for word in ["slow", "bug", "crash", "error", "broken"]):
        category = "Technical Issue"
    elif any(word in user_input for word in ["refund", "bill", "price", "payment"]):
        category = "Billing"
    else:
        category = "General Inquiry"

    # AI Priority Logic based on Sentiment
    if sentiment < -0.3: # User sounds frustrated
        priority = "Urgent (High Sentiment Trigger)"
    elif "emergency" in user_input or "down" in user_input:
        priority = "High"
    else:
        priority = "Medium"

    return category, priority
    