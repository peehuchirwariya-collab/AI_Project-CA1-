# AI Ethics Q&A Bot

A small, offline Python FAQ bot for introductory questions about AI ethics. It uses a transparent keyword match against a curated set of answers and clearly says when it does not know.

## Run

From this folder:

```text
python main.py
```

Type `quit` or `exit` to stop the chat.

## Test

```text
python -m unittest -v
```

## Scope

This is an educational FAQ demo, not legal, compliance, medical, or policy advice. To extend it, add another `FAQ` entry in `main.py` with a concise answer and topic keywords. For a production assistant, add reviewed sources, retrieval, logging, privacy controls, and human escalation.
