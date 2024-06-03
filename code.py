import re

def extract_emails_with_keywords(file_path, keywords):
    # Compile the email regex pattern
    email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
    
    # Read the file content
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Find all emails in the content
    emails = email_pattern.findall(content)
    
    # Extract surrounding text for each email and check for keywords
    keyword_emails = []
    for email in emails:
        # Find the position of the email in the content
        start_pos = content.find(email)
        
        # Define a window of text around the email to search for keywords
        window_start = max(0, start_pos - 100)  # Adjust the window size as needed
        window_end = min(len(content), start_pos + 100)
        window_text = content[window_start:window_end]
        
        # Check if any of the keywords are in the window text
        if any(keyword.lower() in window_text.lower() for keyword in keywords):
            keyword_emails.append(email)
    
    return keyword_emails

# Example usage
file_path = 'sample.txt'
keywords = ['project', 'meeting', 'deadline']
emails_with_keywords = extract_emails_with_keywords(file_path, keywords)
print(emails_with_keywords)
