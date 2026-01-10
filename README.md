# SLM
SLM Chat Interface in Python for Small Language Models

This repository contains minimal Python scripts that launch a local, offline chat interface for running small language models (SLMs) in GGUF format on Debian systems. Using llama.cpp via the llama-cpp-python bindings and Gradio for the frontend, each script loads a quantized model—such as Phi-3-mini or Qwen2.5—and provides a browser-based chat window. The implementation preserves conversation history for contextual continuity and is easily adaptable to other instruction-tuned GGUF models by updating the model path and, if necessary, the stop token. No internet connection or cloud services are required; all computation occurs locally on the CPU.
