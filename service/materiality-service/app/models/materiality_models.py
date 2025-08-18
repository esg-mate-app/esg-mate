from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from enum import Enum

class ImpactLevel(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"

class StakeholderImportance(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"

class MaterialityTopic(BaseModel):
    id: int
    topic: str = Field(..., min_length=1, max_length=200)
    description: str = Field(..., min_length=1, max_length=1000)
    impact_level: ImpactLevel
    stakeholder_importance: StakeholderImportance
    category: str = Field(..., min_length=1, max_length=100)
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class MaterialityTopicCreate(BaseModel):
    topic: str = Field(..., min_length=1, max_length=200)
    description: str = Field(..., min_length=1, max_length=1000)
    impact_level: ImpactLevel
    stakeholder_importance: StakeholderImportance
    category: str = Field(..., min_length=1, max_length=100)

class MaterialityTopicUpdate(BaseModel):
    topic: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = Field(None, min_length=1, max_length=1000)
    impact_level: Optional[ImpactLevel] = None
    stakeholder_importance: Optional[StakeholderImportance] = None
    category: Optional[str] = Field(None, min_length=1, max_length=100)

class MaterialityAssessment(BaseModel):
    id: int
    topic_id: int
    assessment_date: datetime
    score: float = Field(..., ge=0, le=10)
    notes: Optional[str] = Field(None, max_length=1000)
    assessor: str = Field(..., min_length=1, max_length=100)
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class MaterialityAssessmentCreate(BaseModel):
    topic_id: int
    assessment_date: datetime
    score: float = Field(..., ge=0, le=10)
    notes: Optional[str] = Field(None, max_length=1000)
    assessor: str = Field(..., min_length=1, max_length=100)

class MaterialityAssessmentUpdate(BaseModel):
    assessment_date: Optional[datetime] = None
    score: Optional[float] = Field(None, ge=0, le=10)
    notes: Optional[str] = Field(None, max_length=1000)
    assessor: Optional[str] = Field(None, min_length=1, max_length=100)

class MaterialityMatrix(BaseModel):
    topics: List[MaterialityTopic]
    assessments: List[MaterialityAssessment]
    matrix_data: List[dict]  # 매트릭스 시각화용 데이터
