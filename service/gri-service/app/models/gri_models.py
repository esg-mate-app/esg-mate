from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from enum import Enum

class GRIStandardCategory(str, Enum):
    FOUNDATION = "Foundation"
    ECONOMIC = "Economic"
    ENVIRONMENTAL = "Environmental"
    SOCIAL = "Social"

class ReportingStatus(str, Enum):
    NOT_STARTED = "Not Started"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    VERIFIED = "Verified"

class GRIStandard(BaseModel):
    id: int
    code: str = Field(..., min_length=1, max_length=20)
    title: str = Field(..., min_length=1, max_length=200)
    description: str = Field(..., min_length=1, max_length=1000)
    category: GRIStandardCategory
    disclosure_level: str = Field(..., min_length=1, max_length=50)
    version: str = Field(..., min_length=1, max_length=20)
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class GRIStandardCreate(BaseModel):
    code: str = Field(..., min_length=1, max_length=20)
    title: str = Field(..., min_length=1, max_length=200)
    description: str = Field(..., min_length=1, max_length=1000)
    category: GRIStandardCategory
    disclosure_level: str = Field(..., min_length=1, max_length=50)
    version: str = Field(..., min_length=1, max_length=20)

class GRIStandardUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = Field(None, min_length=1, max_length=1000)
    category: Optional[GRIStandardCategory] = None
    disclosure_level: Optional[str] = Field(None, min_length=1, max_length=50)
    version: Optional[str] = Field(None, min_length=1, max_length=20)

class GRIReporting(BaseModel):
    id: int
    standard_id: int
    reporting_period: str = Field(..., min_length=4, max_length=10)
    status: ReportingStatus
    implementation_level: str = Field(..., min_length=1, max_length=50)
    notes: Optional[str] = Field(None, max_length=1000)
    reporter: str = Field(..., min_length=1, max_length=100)
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class GRIReportingCreate(BaseModel):
    standard_id: int
    reporting_period: str = Field(..., min_length=4, max_length=10)
    status: ReportingStatus
    implementation_level: str = Field(..., min_length=1, max_length=50)
    notes: Optional[str] = Field(None, max_length=1000)
    reporter: str = Field(..., min_length=1, max_length=100)

class GRIReportingUpdate(BaseModel):
    reporting_period: Optional[str] = Field(None, min_length=4, max_length=10)
    status: Optional[ReportingStatus] = None
    implementation_level: Optional[str] = Field(None, min_length=1, max_length=50)
    notes: Optional[str] = Field(None, max_length=1000)
    reporter: Optional[str] = Field(None, min_length=1, max_length=100)

class GRIReport(BaseModel):
    id: int
    title: str = Field(..., min_length=1, max_length=200)
    reporting_period: str = Field(..., min_length=4, max_length=10)
    version: str = Field(..., min_length=1, max_length=20)
    status: ReportingStatus
    standards_covered: List[int]
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class GRIReportCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    reporting_period: str = Field(..., min_length=4, max_length=10)
    version: str = Field(..., min_length=1, max_length=20)
    status: ReportingStatus
    standards_covered: List[int]

class GRIReportUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    reporting_period: Optional[str] = Field(None, min_length=4, max_length=10)
    version: Optional[str] = Field(None, min_length=1, max_length=20)
    status: Optional[ReportingStatus] = None
    standards_covered: Optional[List[int]] = None
