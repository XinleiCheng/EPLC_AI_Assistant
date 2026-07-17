"""Central runtime configuration and vector-index locations."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CHROMA_ROOT = REPOSITORY_ROOT / "Data" / "Vector DataBase"


@dataclass(frozen=True)
class IndexSpec:
    """A named Chroma index used by a retrieval workflow."""

    name: str
    path: Path


@dataclass(frozen=True)
class Settings:
    """Application settings loaded once at the composition boundary."""

    openai_api_key: str
    chat_model: str = "gpt-4o-mini"
    embedding_model: str = "BAAI/bge-large-en-v1.5"
    top_k: int = 6
    semantic_distance_threshold: float = 0.75
    chroma_root: Path = DEFAULT_CHROMA_ROOT

    @classmethod
    def from_env(cls) -> "Settings":
        """Load `.env` when available, then construct validated settings."""

        try:
            from dotenv import load_dotenv
        except ImportError:
            load_dotenv = None

        if load_dotenv is not None:
            load_dotenv(REPOSITORY_ROOT / ".env")

        chroma_value = os.getenv("CHROMA_ROOT", "").strip()
        chroma_root = Path(chroma_value).expanduser() if chroma_value else DEFAULT_CHROMA_ROOT
        if not chroma_root.is_absolute():
            chroma_root = REPOSITORY_ROOT / chroma_root

        return cls(
            openai_api_key=os.getenv("OPENAI_API_KEY", "").strip(),
            chat_model=os.getenv("CHAT_MODEL", "gpt-4o-mini").strip(),
            embedding_model=os.getenv(
                "EMBEDDING_MODEL", "BAAI/bge-large-en-v1.5"
            ).strip(),
            top_k=int(os.getenv("TOP_K", "6")),
            semantic_distance_threshold=float(
                os.getenv("SEM_THRESHOLD", "0.75")
            ),
            chroma_root=chroma_root.resolve(),
        )

    def require_api_key(self) -> None:
        if not self.openai_api_key:
            raise ValueError(
                "OPENAI_API_KEY is missing. Copy .env.example to .env and add a key."
            )

    @property
    def policy_indexes(self) -> tuple[IndexSpec, ...]:
        return (
            IndexSpec(
                "eplc-framework",
                self.chroma_root / "chroma_db_EPLC final Phase",
            ),
            IndexSpec(
                "hhs-policy",
                self.chroma_root / "chroma_eplc_policy",
            ),
        )

    @property
    def phase_indexes(self) -> dict[str, IndexSpec]:
        return {
            "requirement": IndexSpec(
                "requirement-templates",
                self.chroma_root / "chroma_db_Requirement Phase",
            ),
            "design": IndexSpec(
                "design-templates",
                self.chroma_root / "chroma_db_Design Phase",
            ),
            "development": IndexSpec(
                "development-templates",
                self.chroma_root / "chroma_db_development_phase",
            ),
            "implementation": IndexSpec(
                "implementation-templates",
                self.chroma_root / "chroma_db_Implementation_Phase",
            ),
        }

