"""Minimal Architectural Sensemaking runtime."""

from dataclasses import dataclass
from typing import Any, Callable


@dataclass
class Skill:
    name: str
    run: Callable[[Any], Any]


class SensemakingAgent:
    """Thin orchestrator: compose reusable skills over a reality input."""

    def __init__(self) -> None:
        self.skills: dict[str, Skill] = {}

    def register(self, skill: Skill) -> None:
        self.skills[skill.name] = skill

    def run(self, reality: Any, pipeline: list[str]) -> Any:
        current = reality
        for name in pipeline:
            current = self.skills[name].run(current)
        return current
