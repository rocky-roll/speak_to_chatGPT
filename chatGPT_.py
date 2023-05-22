#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#    author='@rocky_roll,
#    license='GNU GPLv3'
#

import queue

import openai

from encrypt import key_decript


class ChatGPT:
    def login_openai():
        queue_ = queue.Queue()
        status_ = False
        try:
            key_decript_ = key_decript().decode('utf-8')
            openai.api_key = key_decript_
            models = openai.Model.list()
            status_ = True
            print("ChatGPT API en Python")
        except Exception as e:
            status_ = False
            print(f"Hubo un error al conectar con ChatGPT API en Python {e}")
            pass
        queue_.put_nowait(status_)

    def main_GPT(content):
        try:
            # Contexto del asistente
            context = {"name": "chatGPT",
                       "role": "system",
                       "content": "Eres un asistente muy útil, eres de género femenino, das repuestas con un '30%' de ironía y con un '10%' de sarcasmo, con humor, breves."}  # No uses Emojis y cuando llegues a los 147 caracteres sin espacios tenes que poner un punto aparte."}
            messages = [context]

            messages.append({"role": "user", "content": content})
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                temperature=0.9,
                max_tokens=140,
                top_p=1,
                frequency_penalty=0.5,
                presence_penalty=0,
                messages=messages)

            response_content = response.choices[0].message.content
            messages.append({"role": "assistant", "content": response_content})
            print(f"{response_content}")

        except Exception as e:
            print(f"Hubo un error {e}")
            pass
        return response_content
# ChatGPT.login_openai()
