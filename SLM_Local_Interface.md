# SLM Local Chat Interface (GGUF, llama.cpp, Gradio)

This repository contains variations of a simple but well-structured Python application that provides a clean, browser-based chat interface for running local small language models (SLMs) in GGUF format using llama.cpp. It is intended for users who want an offline, lightweight, and understandable alternative to large frameworks or cloud-based services.

The design goal is clarity and reliability rather than feature bloat. The code is short, readable, and easy to modify, making it suitable both for daily use and as a reference implementation.

---

## What This Project Does

This program loads a GGUF-format language model locally using llama-cpp-python and exposes it through a Gradio-powered chat interface. Conversation history is preserved and sent back to the model in structured chat form. Once installed, everything runs fully offline and performs well on CPU-only systems, including modest or older hardware.

The example configuration targets SLMs such as Phi-3 Mini 4K Instruct quantized as Q4_K_M, but any GGUF chat-capable model supported by llama.cpp can be used.

---

## Who This Is For

This project is intended for Linux users running local SLMs, privacy-focused or offline users, and developers who want a minimal, readable reference implementation. It is also suitable for experimentation and learning, as there is no hidden framework logic or abstraction layer.

No prior experience with Gradio is required.

---

## Requirements

### System

- Linux (tested on Debian-based systems)
- Python 3.10 or newer
- Enough RAM to load the selected model
- GPU is optional and not required for this configuration

### Python Dependencies

Install the required packages using pip:

    pip install llama-cpp-python gradio

If you want GPU acceleration or CPU-specific optimizations, refer to the llama-cpp-python documentation for build options.

---

## Model Setup

Download or place a GGUF model file somewhere on your system. Update the MODEL_PATH variable in the script to point to that file.

Example model path used in the script:

    /home/ben/llm_local/models/phi-3-mini-4k-instruct-q4_k_m.gguf

Only GGUF models compatible with llama.cpp will work.

---

## How the Program Works

When the script starts, the model is loaded once using the Llama class. Gradio then launches a local web interface in your browser. Each user message, along with the full conversation history, is converted into OpenAI-style chat messages and sent to the model using create_chat_completion. The assistant response is returned and displayed in the chat UI.

Key runtime parameters include a 4096 token context window, CPU-only inference, and a moderate temperature for balanced responses. All of these settings can be adjusted in the code.

---

## Running the Application

From the project directory, run:

    python chat.py

Gradio will open your default browser automatically. If it does not, the terminal output will show a local URL that you can open manually.

The interface provides a standard chat layout with scrolling history and persistent context for the duration of the session.

---

## Customization

You may want to adjust the following parameters:

- n_threads to match your CPU core count
- max_tokens to control response length
- temperature to tune creativity versus determinism
- n_gpu_layers if GPU acceleration is available
- stop tokens for different model families
- system prompts or role instructions

The code is intentionally flat and easy to edit.

---

## Compatibility Notes

Not all GGUF models are instruction- or chat-tuned. Some models may ignore chat roles or require different stop tokens. If a model behaves oddly, adding a system prompt or switching to an instruct-tuned model usually resolves the issue.

Phi-3 Mini serves as a general example because it works well with this setup without modification.

---

## Limitations

This is a deliberately minimal implementation. It does not include streaming output, multi-user support, authentication, long-term memory, or persistence across restarts. These omissions keep the program predictable and easy to understand.

---

## License and Usage

This repository contains example code intended for personal, educational, or experimental use. If you redistribute or build upon it, review the licenses of llama.cpp, llama-cpp-python, Gradio, and the specific model you are using.

---

## Summary

This project provides a clean and minimal local chat interface for GGUF models using llama.cpp and Gradio. It avoids unnecessary complexity while remaining flexible and easy to extend, making it a solid foundation for local LLM experimentation or daily offline use.

---

## Author

Ben Santora - January 2026
