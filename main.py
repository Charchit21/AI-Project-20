
urgent_keywords = {
    'spoiled': 3.0,
    'mold': 3.0,
    'allergy': 3.5,
    'sick': 3.0,
    'emergency': 3.0,
    'ruined': 2.5,
    'refund': 1.5,
    'late': 1.0,
    'burnt': 1.5
}

dataset = [
    {"message": "The wedding cake arrived completely ruined and smashed!", "label": "URGENT"},
    {"message": "I found mold inside the chocolate croissant I bought today.", "label": "URGENT"},
    {"message": "Someone in my party has a severe nut allergy, is this safe?", "label": "URGENT"},
    {"message": "Can I order a dozen blueberry muffins for pickup tomorrow?", "label": "NORMAL"},
    {"message": "What time do you guys close on Sunday?", "label": "NORMAL"},
    {"message": "Do you make custom gluten-free birthday cakes?", "label": "NORMAL"},
    {"message": "The delivery driver was 2 hours late and the food was cold.", "label": "URGENT"},
    {"message": "Thank you so much for the wonderful cupcakes at our party!", "label": "NORMAL"}
]

def classify_message(message, threshold=1.0):
    score = 0.0
    words = message.lower().split()
    
    for word in words:
        clean_word = word.strip(".,!?")
        if clean_word in urgent_keywords:
            score += urgent_keywords[clean_word]
            
    if score >= threshold:
        return "URGENT"
    else:
        return "NORMAL"

def evaluate_sorter(test_data):
    """
    Sorts messages and counts the mistakes made by the sorter.
    """
    mistakes = 0
    print("==================================================")
    print("        BAKERY HELP DESK SORTER RESULTS           ")
    print("==================================================\n")
    
    for i, data in enumerate(test_data):
        message = data["message"]
        true_label = data["label"]
        
        predicted_label = classify_message(message)
        
        status = "MATCH" if predicted_label == true_label else "MISTAKE"
        if status == "MISTAKE":
            mistakes += 1
            
        print(f"Message {i+1}: \"{message}\"")
        print(f"  -> True: {true_label} | Predicted: {predicted_label} [{status}]")
        print("-" * 50)
        
    print(f"\nTotal Mistakes Made: {mistakes} out of {len(test_data)} messages.")

if __name__ == "__main__":
    evaluate_sorter(dataset)