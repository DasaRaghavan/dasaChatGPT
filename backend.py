import openai

from constants import OPEN_AI_API


class Chatbot:
    def __init__(self):
        openai.api_key = OPEN_AI_API
        # client = openai.OpenAI(api_key=OPEN_AI_API)

    def get_response(self, user_input, persona):
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {'role': 'user', 'content': user_input},
                {'role': 'system', 'content': persona}
            ],
            max_tokens=4000,
            temperature=0.7,
            user='Dasa'
        ).choices[0].message.content
        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Tell me a the best marathon joke",
                                    "one liner response")
    print(response)
