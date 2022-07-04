from typing import Dict, List, Optional
from pydantic import BaseModel


class HealthCheckDefinition(BaseModel):
    url: str
    interval: Optional[int] = 30

class ServersDefinition(BaseModel):
    url: str
    description: str    

class MicroserviceDefinition(BaseModel):
    name: str
    tags: List[str]
    host: str
    port: int
    metadata: Optional[Dict]
    healthcheck: Optional[HealthCheckDefinition]
    servers: Optional[ServersDefinition]
