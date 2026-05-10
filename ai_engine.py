import google.generativeai as genai
from database import add_expense, get_all_expenses

genai.configure(api_key="")

# Описуємо функції для моделі
tools = [add_expense, get_all_expenses]

model = genai.GenerativeModel(
    model_name='models/gemini-3.1-flash-lite',
    tools=tools,
    system_instruction="Ти фінансовий помічник. Якщо користувач каже про витрату, виклич add_expense. Якщо питає аналітику, виклич get_all_expenses і проаналізуй дані."
)

chat = model.start_chat(enable_automatic_function_calling=True)

def ask_ai(prompt):
    response = chat.send_message(prompt)
    return response.text