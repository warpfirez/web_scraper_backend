from __future__ import annotations

from typing import TYPE_CHECKING

from app.domain.repositories.job_repository import JobRepository

if TYPE_CHECKING:
  from app.domain.entities.job import Job


class ScrapeJobs:
  def __init__(self, job_repository: JobRepository):
    self._job_repository = job_repository

  async def __call__(self) -> list[Job]:
    return await self._job_repository.scrape_jobs()