import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a math and programming expert"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-4-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Computer Science assistant")

demo.launch(share=True)
