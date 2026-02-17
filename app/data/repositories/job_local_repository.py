from __future__ import annotations

from typing import TYPE_CHECKING
from xmlrpc.client import Boolean

from app.domain.repositories.job_store import JobStore

if TYPE_CHECKING:
    from app.domain.entities.job import Job
    
    
class JobLocalRepository(JobStore):
    
    def __init__(self):
        pass
    
    async def save_jobs(self) -> Boolean:
        return True
    
    async def fetch_jobs(self) -> list[Job]:
        return []