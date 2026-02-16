from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.domain.entities.job import JobRepository

class JobRemoteRepository(JobRepository):
    
    async def fetch_jobs():
        raise NotImplementedError