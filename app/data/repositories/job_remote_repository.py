from __future__ import annotations

from typing import TYPE_CHECKING
from xmlrpc.client import Boolean

from app.data.datasources.just_join_it_scraper import JustJoinScraper
from app.data.datasources.no_fluff_scraper import NoFluffScraper
from app.domain.repositories.job_repository import JobRepository

if TYPE_CHECKING:
    from app.domain.entities.job import Job

class JobRemoteRepository(JobRepository):
    
    def __init__(self, noFluffScraper: NoFluffScraper, justJoinScraper: JustJoinScraper):
        self.noFluffScraper = noFluffScraper
        self.justJoinScraper = justJoinScraper
    
    # change Exception to handled Error
    async def scrape_jobs(self) -> Exception | None:
        return None
    
    async def fetch_jobs(self) -> list[Job]:
        return []