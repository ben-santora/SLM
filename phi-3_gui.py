from llama_cpp import Llama
import gradio as gr

MODEL_PATH = "/home/ben/llm_local/models/phi-3-mini-4k-instruct-q4_k_m.gguf"

llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=4096,
    n_threads=4,
    n_gpu_layers=0
)

def generate_response(message, history):
    messages = []
    for user_msg, bot_msg in history:
        messages.append({"role": "user", "content": user_msg})
        messages.append({"role": "assistant", "content": bot_msg})
    messages.append({"role": "user", "content": message})
    
    response = llm.create_chat_completion(
        messages=messages,
        max_tokens=512,
        temperature=0.7,
        stop=["<|end|>"]
    )
    return response["choices"][0]["message"]["content"]

gr.ChatInterface(
    generate_response,
    title="Phi-3-mini Local Chat",
    description="Offline chat with Phi-3-mini (Q4_K_M) on your Debian machine."
).launch(inbrowser=True)
