import os
import openai
from dotenv import load_dotenv
import tiktoken
import gptrim

# load local .env
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def count_tokens(text: str,) -> int:
    encoding = tiktoken.get_encoding("cl100k_base")
    tokens = encoding.encode(text)
    return len(tokens)

def askgpt(question, chat_log=None, trim=True, token_history=None):
    if chat_log is None:
        chat_log = [{
            'role':'system',
            'content': 'You are a helpful, upbeat and funny assistant.'
        }]
    
    chat_log.append({'role': 'user', 'content': question})

    response = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=chat_log)
    answer = response.choices[0].message.content
    trimmed_answer = answer if trim else gptrim.trim(answer)
    chat_log.append({'role': 'assistant', 'content': gptrim.trim(trimmed_answer)})

    if token_history is None:
        return answer, chat_log

    token_history.append({'default': count_tokens(answer), 'trimmed': count_tokens(trimmed_answer)})

    return answer, chat_log, token_history

def main():
    chat_log = None
    token_history = []

    while True:
        question = input("What is your question?\n> ")
        trimmed_input = gptrim.trim(question)

        token_history.append({'default': count_tokens(question), 'trimmed': count_tokens(trimmed_input)})

        answer, chat_log, token_history = askgpt(trimmed_input, chat_log, trim=True, token_history=token_history)

        total_default_tokens = sum([i['default'] for i in token_history])
        total_trimmed_tokens = sum([i['trimmed'] for i in token_history])
        print('Default token total:', total_default_tokens)
        print('Trimmed token total:', total_trimmed_tokens)
        print('Token saved (%): {:.2f}%'.format((total_default_tokens - total_trimmed_tokens)/total_default_tokens*100))
        print()
        print(answer + '\n')

if __name__=='__main__':
    main()