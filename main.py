# print("Hello World!")

import random
import os

def basic_gpt(prompt, word_list):
    # Extract keywords from the prompt
    keywords = prompt.lower().split()
    
    # Prioritize words from prompt and word_list
    response_words = []
    for _ in range(random.randint(5, 10)):
        if keywords and random.random() < 0.5:
            response_words.append(random.choice(keywords))
        else:
            response_words.append(random.choice(word_list))
    
    return " ".join(response_words)

def learn_and_save(user_input, word_list, filename="word_list.txt"):
    # Learn new words from user input
    new_words = user_input.lower().split()
    word_list.extend(word for word in new_words if word not in word_list)

    # Save updated word list to file
    with open(filename, "w") as f:
        f.write("\n".join(word_list))

    return word_list

def load_word_list(filename="word_list.txt"):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return f.read().splitlines()
    else:
        return ["hello", "world", "python", "coding", "computer", "science", "data", "AI", "machine", "learning"]

# Main execution
word_list = load_word_list()

while True:
    user_prompt = input("Enter a prompt (or 'q' to quit): ")
    if user_prompt.lower() == 'q':
        break
    
    generated_text = basic_gpt(user_prompt, word_list)
    print(generated_text)
    
    word_list = learn_and_save(user_prompt, word_list)