from __future__ import annotations

from typing import TYPE_CHECKING

from app.data.repositories.job_local_repository import JobLocalRepository


if TYPE_CHECKING:
  from app.domain.entities.job import Job


class FetchJobs:
  def __init__(self, job_local_repository: JobLocalRepository):
    self.job_local_repository = job_local_repository

  async def __call__(self) -> list[Job]:
    return await self.job_local_repository.fetch_jobs()