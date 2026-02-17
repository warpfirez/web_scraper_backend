from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.domain.entities.job import Job

class JobRepository(ABC):
    
    @abstractmethod
    async def scrape_jobs(self):
        pass