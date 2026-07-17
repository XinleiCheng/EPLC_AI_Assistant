"""Small language-model boundary that can be replaced in tests."""

from __future__ import annotations

from typing import Protocol


class TextGenerator(Protocol):
    def generate(
        self,
        *,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.0,
    ) -> str: ...


class OpenAITextGenerator:
    """OpenAI implementation kept behind a narrow application interface."""

    def __init__(self, *, api_key: str, model: str) -> None:
        if not api_key:
            raise ValueError("An OpenAI API key is required.")

        from openai import OpenAI

        self._client = OpenAI(api_key=api_key)
        self._model = model

    def generate(
        self,
        *,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.0,
    ) -> str:
        response = self._client.chat.completions.create(
            model=self._model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=temperature,
        )
        return (response.choices[0].message.content or "").strip()

