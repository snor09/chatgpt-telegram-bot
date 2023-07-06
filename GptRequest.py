import openai
from enum import Enum
import time
import datetime
import rx
from rx import operators as ops
from rx.scheduler import threadpoolscheduler


class RequestType(Enum):
    IMAGE = 1
    TEXT = 2

class GptRequest:
    pass

    def initialize(self, api_key):
        print("Initializing openai")
        openai.api_key = api_key

    def test(self, iteration) :
        models = openai.Model.list()
        print(datetime.datetime.now())    
        return rx.of(f"modello: {models.data[0].id}") # type: ignore
    
    def gptRequest(self, prompt):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = [{"role": "user", "content": prompt}]
        )
        response = completion.choices[0].message.content # type: ignore
        return rx.of(response)