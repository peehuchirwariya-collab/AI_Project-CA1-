"""Offline FAQ bot for introductory AI ethics questions."""

from dataclasses import dataclass
import re
from typing import Iterable


@dataclass(frozen=True)
class FAQ:
    question: str
    answer: str
    keywords: frozenset[str]


FAQS = (
    FAQ(
        "What is AI ethics?",
        "AI ethics is the practice of designing, deploying, and governing AI in ways that respect human rights, reduce harm, and support accountability.",
        frozenset({"artificial", "ethics", "ethical", "responsible", "meaning"}),
    ),
    FAQ(
        "How can AI be biased?",
        "AI can reproduce or amplify unfair patterns in its data, labels, objectives, or deployment context. Test outcomes across groups and keep people involved in review.",
        frozenset({"bias", "biased", "fair", "fairness", "discrimination", "data"}),
    ),
    FAQ(
        "How should AI protect privacy?",
        "Collect only what is needed, explain the purpose, secure the data, limit retention, and give people meaningful control over access and deletion.",
        frozenset({"privacy", "private", "personal", "data", "consent", "surveillance"}),
    ),
    FAQ(
        "Who is accountable for an AI system?",
        "Accountability belongs to the people and organizations that design, procure, deploy, and oversee the system. A model should never be treated as the responsible decision-maker.",
        frozenset({"accountability", "accountable", "responsibility", "responsible", "owner", "human"}),
    ),
    FAQ(
        "When should humans review an AI decision?",
        "Use human review for high-impact decisions, uncertain outputs, appeals, and cases involving vulnerable people. Reviewers need authority, context, and time to disagree with the system.",
        frozenset({"human", "review", "oversight", "decision", "high", "impact", "appeal"}),
    ),
    FAQ(
        "Why is transparency important in AI?",
        "Transparency helps people understand a system's purpose, limits, data use, and decision process. It supports informed consent, auditing, contestability, and public trust.",
        frozenset({"transparency", "transparent", "explain", "explainability", "trust", "audit"}),
    ),
)

FALLBACK = (
    "I do not have a confident answer for that yet. Try asking about bias, privacy, "
    "accountability, human review, transparency, or the meaning of AI ethics."
)


def _tokens(text: str) -> set[str]:
    return set(re.findall(r"[a-z]+", text.lower()))


def answer_question(question: str, faqs: Iterable[FAQ] = FAQS) -> str:
    """Return the best FAQ answer, or a transparent fallback when confidence is low."""
    query_tokens = _tokens(question)
    if not query_tokens:
        return FALLBACK

    best_faq = None
    best_score = 0
    for faq in faqs:
        score = len(query_tokens & faq.keywords)
        if score > best_score:
            best_faq = faq
            best_score = score

    return best_faq.answer if best_faq and best_score >= 1 else FALLBACK


def run_chat() -> None:
    print("AI Ethics Q&A Bot")
    print("Ask about bias, privacy, accountability, human review, or transparency.")
    print("Type 'quit' to exit.\n")

    while True:
        try:
            question = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBot: Goodbye.")
            break

        if question.lower() in {"quit", "exit"}:
            print("Bot: Goodbye.")
            break

        print(f"Bot: {answer_question(question)}\n")


if __name__ == "__main__":
    run_chat()
