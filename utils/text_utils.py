import re

def clean_prompt(text):
    # Ta bort [ljud] och (beskrivningar)
    text = re.sub(r'\[.*?\]|\(.*?\)', '', text)
    # Ta bort citattecken och dubbla tecken
    text = text.replace('“', '').replace('”', '').replace('"', '').replace("'", '')
    # Ta bort IP-relaterade och farliga ord
    banned = ['Garfield', 'Shrek', 'SpongeBob', 'Naruto', 'Marvel', 'Detective', 'Purr-secco']
    for word in banned:
        text = text.replace(word, '')
    # Förenkla: ta första meningen
    if '.' in text:
        text = text.split('.')[0]
    # Trimma
    return re.sub(r'\s+', ' ', text).strip()
