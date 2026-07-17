from pathlib import Path
from unittest import TestCase
from unittest.mock import patch

from eplc_assistant.config import Settings
from eplc_assistant.runtime import build_services


class FakeEmbedder:
    def __init__(self, model_name: str) -> None:
        self.model_name = model_name


class FakeIndex:
    def __init__(self, spec: object) -> None:
        self.spec = spec

    def search(self, embedding: list[float], limit: int) -> list[object]:
        return []


class FakeGenerator:
    def __init__(self, *, api_key: str, model: str) -> None:
        self.api_key = api_key
        self.model = model


class RuntimeTests(TestCase):
    @patch("eplc_assistant.runtime.OpenAITextGenerator", FakeGenerator)
    @patch("eplc_assistant.runtime.ChromaIndex", FakeIndex)
    @patch("eplc_assistant.runtime.BgeEmbeddingProvider", FakeEmbedder)
    def test_services_share_one_embedding_configuration(self) -> None:
        settings = Settings(
            openai_api_key="test-key",
            embedding_model="BAAI/bge-large-en-v1.5",
            chroma_root=Path("/indexes"),
        )

        services = build_services(settings)

        self.assertEqual(
            ("design", "development", "implementation", "requirement"),
            services.drafting.supported_phases,
        )
        self.assertEqual(6, services.qna._top_k)

