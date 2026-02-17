from __future__ import annotations

from typing_extensions import Self

import logging
import schedule
import time

class ScrapeEngine:
    _instance = None
    
    def __new__(cls) -> Self:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if getattr(self, "_initialized", False):
            return
        self._initialized = True

        self._scheduler = schedule.Scheduler()
        self._scheduler.every(1).day.do(self._scrape)
    
    def runScrapeEngine(self):
        while True:
            self._scheduler.run_pending()
            time.sleep(1)
        
    def _scrape(self) -> None:
        try:
            pass
        except Exception:
            logging.exception("Scrape job failed")