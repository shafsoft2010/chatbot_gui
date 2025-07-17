
import tkinter as tk
from tkinter import scrolledtext
import random

# Predefined responses
responses = {
    "hi": "Hello! How can I assist you today?",
    "hello": "Hi there! What can I do for you?",
    "what is your name": "I'm your friendly Python chatbot.",
    "how are you": "I'm just code, but I'm running fine!",
    "what can you do": "I can answer basic questions and have a simple chat.",
    "bye": "Goodbye! Have a great day!",
}

default_responses = [
    "I'm not sure how to respond to that.",
    "Can you rephrase that?",
    "Let's talk about something else.",
]

def get_response(user_input):
    return responses.get(user_input.lower(), random.choice(default_responses))

def send():
    user_input = entry.get()
    chat_window.insert(tk.END, "You: " + user_input + '\n')
    response = get_response(user_input)
    chat_window.insert(tk.END, "Bot: " + response + '\n\n')
    entry.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Simple Python Chatbot")
root.geometry("400x500")

chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, state='normal')
chat_window.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

send_button = tk.Button(root, text="Send", command=send)
send_button.pack()

root.mainloop()
