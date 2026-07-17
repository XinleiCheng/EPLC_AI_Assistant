"""Composition root for production service implementations."""

from __future__ import annotations

from dataclasses import dataclass

from eplc_assistant.config import Settings
from eplc_assistant.llm import OpenAITextGenerator
from eplc_assistant.rag import BgeEmbeddingProvider, ChromaIndex, MultiIndexRetriever
from eplc_assistant.services import DraftingService, QnaService


@dataclass(frozen=True)
class ApplicationServices:
    qna: QnaService
    drafting: DraftingService


def build_services(settings: Settings) -> ApplicationServices:
    """Build shared adapters once and inject them into application services."""

    settings.require_api_key()
    embedder = BgeEmbeddingProvider(settings.embedding_model)
    generator = OpenAITextGenerator(
        api_key=settings.openai_api_key,
        model=settings.chat_model,
    )

    policy_retriever = MultiIndexRetriever(
        embedder=embedder,
        indexes=[ChromaIndex(spec) for spec in settings.policy_indexes],
        distance_threshold=settings.semantic_distance_threshold,
    )
    phase_retrievers = {
        phase: MultiIndexRetriever(
            embedder=embedder,
            indexes=[ChromaIndex(spec)],
            distance_threshold=settings.semantic_distance_threshold,
        )
        for phase, spec in settings.phase_indexes.items()
    }

    return ApplicationServices(
        qna=QnaService(
            retriever=policy_retriever,
            generator=generator,
            top_k=settings.top_k,
        ),
        drafting=DraftingService(
            phase_retrievers=phase_retrievers,
            generator=generator,
            top_k=settings.top_k,
        ),
    )

