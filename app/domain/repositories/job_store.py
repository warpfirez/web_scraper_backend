from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.domain.entities.job import Job


class JobStore(ABC):
    @abstractmethod
    async def save_jobs(self, jobs: list[Job]) -> None:
        raise NotImplementedError
    
    @abstractmethod
    async def fetch_jobs(self) -> list[Job]:
        raise NotImplementedError