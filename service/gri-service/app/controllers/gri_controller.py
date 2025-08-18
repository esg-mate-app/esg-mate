from fastapi import APIRouter, HTTPException
from typing import List
from ..models.gri_models import (
    GRIStandard, GRIStandardCreate, GRIStandardUpdate,
    GRIReporting, GRIReportingCreate, GRIReportingUpdate,
    GRIReport, GRIReportCreate, GRIReportUpdate
)
from ..services.gri_service import GRIService

router = APIRouter()
gri_service = GRIService()

@router.get("/", response_model=dict)
async def root():
    """GRI Service 루트 엔드포인트"""
    return {
        "message": "GRI Service",
        "port": 8003,
        "endpoints": ["/standards", "/reporting", "/reports", "/health"]
    }

@router.get("/health")
async def health_check():
    """GRI Service 헬스체크"""
    return {
        "status": "healthy",
        "service": "gri",
        "port": 8003
    }

# GRI Standards 엔드포인트
@router.get("/standards", response_model=List[GRIStandard])
async def get_gri_standards():
    """모든 GRI 표준 조회"""
    try:
        standards = await gri_service.get_all_standards()
        return standards
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/standards/{standard_id}", response_model=GRIStandard)
async def get_gri_standard(standard_id: int):
    """특정 GRI 표준 조회"""
    try:
        standard = await gri_service.get_standard_by_id(standard_id)
        if not standard:
            raise HTTPException(status_code=404, detail="Standard not found")
        return standard
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/standards", response_model=GRIStandard)
async def create_gri_standard(standard_data: GRIStandardCreate):
    """새로운 GRI 표준 생성"""
    try:
        standard = await gri_service.create_standard(standard_data)
        return standard
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/standards/{standard_id}", response_model=GRIStandard)
async def update_gri_standard(standard_id: int, standard_data: GRIStandardUpdate):
    """GRI 표준 수정"""
    try:
        standard = await gri_service.update_standard(standard_id, standard_data)
        if not standard:
            raise HTTPException(status_code=404, detail="Standard not found")
        return standard
    except HTTPException:
        raise
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/standards/{standard_id}")
async def delete_gri_standard(standard_id: int):
    """GRI 표준 삭제"""
    try:
        success = await gri_service.delete_standard(standard_id)
        if not success:
            raise HTTPException(status_code=404, detail="Standard not found")
        return {"message": "Standard deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# GRI Reporting 엔드포인트
@router.get("/reporting", response_model=List[GRIReporting])
async def get_gri_reporting():
    """모든 GRI 리포팅 조회"""
    try:
        reporting = await gri_service.get_all_reporting()
        return reporting
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/reporting/{reporting_id}", response_model=GRIReporting)
async def get_gri_reporting_by_id(reporting_id: int):
    """특정 GRI 리포팅 조회"""
    try:
        reporting = await gri_service.get_reporting_by_id(reporting_id)
        if not reporting:
            raise HTTPException(status_code=404, detail="Reporting not found")
        return reporting
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/reporting", response_model=GRIReporting)
async def create_gri_reporting(reporting_data: GRIReportingCreate):
    """새로운 GRI 리포팅 생성"""
    try:
        reporting = await gri_service.create_reporting(reporting_data)
        return reporting
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/reporting/{reporting_id}", response_model=GRIReporting)
async def update_gri_reporting(reporting_id: int, reporting_data: GRIReportingUpdate):
    """GRI 리포팅 수정"""
    try:
        reporting = await gri_service.update_reporting(reporting_id, reporting_data)
        if not reporting:
            raise HTTPException(status_code=404, detail="Reporting not found")
        return reporting
    except HTTPException:
        raise
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/reporting/{reporting_id}")
async def delete_gri_reporting(reporting_id: int):
    """GRI 리포팅 삭제"""
    try:
        success = await gri_service.delete_reporting(reporting_id)
        if not success:
            raise HTTPException(status_code=404, detail="Reporting not found")
        return {"message": "Reporting deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# GRI Reports 엔드포인트
@router.get("/reports", response_model=List[GRIReport])
async def get_gri_reports():
    """모든 GRI 리포트 조회"""
    try:
        reports = await gri_service.get_all_reports()
        return reports
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/reports/{report_id}", response_model=GRIReport)
async def get_gri_report(report_id: int):
    """특정 GRI 리포트 조회"""
    try:
        report = await gri_service.get_report_by_id(report_id)
        if not report:
            raise HTTPException(status_code=404, detail="Report not found")
        return report
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/reports", response_model=GRIReport)
async def create_gri_report(report_data: GRIReportCreate):
    """새로운 GRI 리포트 생성"""
    try:
        report = await gri_service.create_report(report_data)
        return report
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/reports/{report_id}", response_model=GRIReport)
async def update_gri_report(report_id: int, report_data: GRIReportUpdate):
    """GRI 리포트 수정"""
    try:
        report = await gri_service.update_report(report_id, report_data)
        if not report:
            raise HTTPException(status_code=404, detail="Report not found")
        return report
    except HTTPException:
        raise
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/reports/{report_id}")
async def delete_gri_report(report_id: int):
    """GRI 리포트 삭제"""
    try:
        success = await gri_service.delete_report(report_id)
        if not success:
            raise HTTPException(status_code=404, detail="Report not found")
        return {"message": "Report deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 추가 엔드포인트
@router.get("/standards/category/{category}")
async def get_standards_by_category(category: str):
    """카테고리별 GRI 표준 조회"""
    try:
        standards = await gri_service.get_standards_by_category(category)
        return standards
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/reporting/period/{period}")
async def get_reporting_by_period(period: str):
    """기간별 GRI 리포팅 조회"""
    try:
        reporting = await gri_service.get_reporting_by_period(period)
        return reporting
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
