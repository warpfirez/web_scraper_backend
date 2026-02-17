from app.domain.repositories.job_repository import JobRepository
from app.domain.repositories.job_store import JobStore


class RunScrape:
    def __init__(self, job_source: JobRepository, job_store: JobStore):
        self.job_source = job_source
        self.job_store = job_store
        
    async def __call__(self):
        await self.job_source.fetch_jobs()
        await self.job_store.save_jobs([])