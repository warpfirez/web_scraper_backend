from __future__ import annotations

from typing import TYPE_CHECKING, List

from app.domain.repositories.job_store import JobStore

if TYPE_CHECKING:
    from app.domain.entities.job import Job
    
    
class JobLocalRepository(JobStore):
    
    def __init__(self):
        pass
    
    async def save_jobs(self, jobs: list[Job]) -> None:
        pass
    
    async def fetch_jobs(self) -> List[Job]:
        return []