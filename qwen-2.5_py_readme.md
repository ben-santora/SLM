```markdown
# Qwen2.5 Local Chat (llama.cpp + Gradio)

This repository contains a minimal, educational Python chat interface for running **Qwen 2.5 instruction-tuned GGUF models** locally using `llama_cpp` and Gradio.  
The intent is not to replace full-featured frontends such as Jan.ai or LM Studio, but to provide a transparent, close-to-the-metal reference that makes the mechanics of local inference visible and understandable.

## Why this exists

Most local AI frontends hide critical details behind layers of abstraction: prompt framing, role handling, chat history reconstruction, and sampling controls. This script keeps those elements explicit and readable, making it useful as both a learning tool and a baseline implementation.

Typical use cases include:

- Understanding how Qwen instruction models interpret chat structure
- Experimenting with sampling parameters and context behavior
- Embedding local LLM inference directly into Python workflows
- Building small, reproducible, offline tools without external services

## Features

- Direct use of `llama_cpp` with no server or REST layer
- Explicit reconstruction of chat history on every turn
- Stable system prompt for instruction anchoring
- Minimal, readable code intended for experimentation
- Fully offline operation using local GGUF models

## Requirements

- Python 3.10 or newer
- A local GGUF model (tested with `qwen-2.5-1.5b-instruct-q4_k_m.gguf`)
- Sufficient RAM for the selected context size

Python dependencies can be installed with:

    pip install llama-cpp-python gradio

Ensure that `llama-cpp-python` is built with CPU support appropriate for your hardware.

## Script Overview

The script follows a straightforward and explicit flow:

1. Loads the GGUF model using `llama_cpp.Llama`
2. Defines a concise system prompt to anchor behavior
3. Reconstructs full chat history as user/assistant message pairs
4. Appends the current user input
5. Calls `create_chat_completion`
6. Returns the generated response to Gradio for display

All prompt structure, roles, and sampling parameters are visible and easy to modify.

## Example Script

    from llama_cpp import Llama
    import gradio as gr

    MODEL_PATH = "/home/ben/llm_local/models/qwen-2.5-1.5b-instruct-q4_k_m.gguf"

    llm = Llama(
        model_path=MODEL_PATH,
        n_ctx=4096,
        n_threads=4,
        n_gpu_layers=0,
    )

    SYSTEM_PROMPT = (
        "You are a concise, technical assistant. "
        "Answer clearly and accurately."
    )

    def generate_response(message, history):
        messages = []

        messages.append({
            "role": "system",
            "content": SYSTEM_PROMPT
        })

        for user_msg, assistant_msg in history:
            messages.append({"role": "user", "content": user_msg})
            messages.append({"role": "assistant", "content": assistant_msg})

        messages.append({"role": "user", "content": message})

        response = llm.create_chat_completion(
            messages=messages,
            max_tokens=512,
            temperature=0.7,
            top_p=0.95,
        )

        return response["choices"][0]["message"]["content"]

    gr.ChatInterface(
        fn=generate_response,
        title="Qwen2.5 Local Chat",
        description="Offline chat with Qwen2.5-1.5B-Instruct (Q4_K_M) using llama.cpp."
    ).launch(inbrowser=True)

## Notes on Design Choices

- **Explicit system prompt**: Qwen instruction models behave more consistently when given a clear but minimal behavioral anchor.
- **No hard-coded stop tokens**: Relying on EOS avoids brittle, model-specific stop sequences that can truncate output.
- **Full history replay**: Chat history is reconstructed each turn to preserve conversational context.
- **CPU-first configuration**: Tuned for efficient local inference on small, quantized models without GPU offload.

## When to use this instead of a GUI frontend

This approach is appropriate when you want to study model behavior, integrate inference into custom scripts, automate local workflows, or maintain full control over prompts and parameters. For everyday conversational use, mature GUI frontends remain more convenient.

## License

Use, modify, and experiment freely.
```
