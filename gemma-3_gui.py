from llama_cpp import Llama
import gradio as gr

# Path to your GGUF model
MODEL_PATH = "/home/ben/llm_local/models/gemma-3-1b-it-q4_k_m.gguf"

llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=4096,
    n_threads=6,        # Physical cores
    n_gpu_layers=0,     # CPU-only
)

SYSTEM_PROMPT = (
    "You are a concise, technical assistant. "
    "Answer clearly and accurately."
)

def generate_response(message, history):
    messages = []

    # System message for instruction stability
    messages.append({
        "role": "system",
        "content": SYSTEM_PROMPT
    })

    # Reconstruct conversation history
    for user_msg, assistant_msg in history:
        messages.append({
            "role": "user",
            "content": user_msg
        })
        messages.append({
            "role": "assistant",
            "content": assistant_msg
        })

    # Current user input
    messages.append({
        "role": "user",
        "content": message
    })

    response = llm.create_chat_completion(
        messages=messages,
        max_tokens=512,
        temperature=0.7,
        top_p=0.95,
    )

    return response["choices"][0]["message"]["content"]

gr.ChatInterface(
    fn=generate_response,
    title="gemma-3 Local Chat",
    description="Offline chat with gemma-3-1b-it-q4_k_m using llama.cpp bindings."
).launch(inbrowser=True)
