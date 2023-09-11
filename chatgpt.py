import os
import json
from dotenv import load_dotenv
import openai

class Chatgpt:

    def get_answer(self, question):
        prompt = question

        load_dotenv()

        openai.api_key = os.getenv("CHAT_GPT3_API_KEY")
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=1500,
                temperature=0.5,
            )

            json_object = response
            json_string = json.dumps(json_object)

            parsed_json = json.loads(json_string)

            return parsed_json['choices'][0]['text']
        except:
            return
