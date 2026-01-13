# gemma-3 Local Chat (llama.cpp + Gradio)

This repository contains a minimal, educational Python chat interface for running **Gemma 3 instruction-tuned GGUF models** locally using `llama_cpp` and Gradio.  
The goal is not to compete with full-featured frontends like Jan.ai or LM Studio, but to provide a clear, close-to-the-metal reference implementation that exposes how local inference actually works.

## Why this exists

Modern local AI frontends abstract away many important details: prompt construction, chat history handling, system instructions, and sampling behavior. This script keeps those elements explicit and readable, making it useful for:

- Learning how instruction-tuned models behave
- Experimenting with sampling and context management
- Embedding local LLM inference directly into Python workflows
- Building lightweight, reproducible local tools

## Features

- Direct use of `llama_cpp` (no server, no REST API)
- Proper chat history reconstruction
- Explicit system prompt for Gemma instruction stability
- Minimal, readable code suitable for experimentation
- Fully offline operation

## Requirements

- Python 3.10+
- A local GGUF model (tested with `gemma-3-1b-it-q4_k_m.gguf`)
- Sufficient RAM for your chosen context size

Python dependencies:

    pip install llama-cpp-python gradio

Make sure `llama-cpp-python` is built with CPU support appropriate for your system.

## Script Overview

The script performs the following steps:

1. Loads the GGUF model via `llama_cpp.Llama`
2. Defines a short system prompt to anchor behavior
3. Reconstructs chat history on every turn (user/assistant pairs)
4. Appends the current user message
5. Calls `create_chat_completion`
6. Returns the model’s response to Gradio

All prompt structure and parameters are visible and easy to modify.

## Example Script

    from llama_cpp import Llama
    import gradio as gr

    MODEL_PATH = "/home/ben/llm_local/models/gemma-3-1b-it-q4_k_m.gguf"

    llm = Llama(
        model_path=MODEL_PATH,
        n_ctx=4096,
        n_threads=6,
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
        title="gemma-3 Local Chat",
        description="Offline chat with gemma-3-1b-it-q4_k_m using llama.cpp bindings."
    ).launch(inbrowser=True)

## Notes on Design Choices

- **No stop tokens**: Gemma GGUF models already terminate correctly using EOS. Adding unknown stop strings can cause truncation.
- **Explicit history handling**: Gradio passes history for a reason; ignoring it results in stateless responses.
- **Minimal system prompt**: Gemma instruction models respond more consistently when given a light behavioral anchor.
- **CPU-first configuration**: Designed for efficient local CPU inference on small models.

## When to use this instead of a GUI frontend

Use this approach when you want to understand model behavior, build custom tooling, automate inference, or maintain tight control over prompts and parameters. For general daily chat usage, mature GUI frontends remain more convenient.

## License

Use, modify, and experiment freely.
