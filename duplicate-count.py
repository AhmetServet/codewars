def duplicate_count(text):
    duplicants = 0
    text = text.lower()

    for i in text:
        if text.count(i) > 1:
            duplicants += 1
            text = text.replace(i, "")

    
    return duplicants