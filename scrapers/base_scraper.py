import aiohttp
import asyncio
from abc import ABC, abstractmethod
from typing import Dict, List
import json
import logging

class BaseScraper(ABC):
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        
    @abstractmethod
    async def scrape(self) -> List[Dict]:
        """Scrape festival data from source"""
        pass
        
    async def fetch(self, url: str) -> str:
        """Fetch webpage content"""
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.text()