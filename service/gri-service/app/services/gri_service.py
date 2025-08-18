from typing import List, Optional, Dict, Any
from ..models.gri_models import (
    GRIStandard, GRIStandardCreate, GRIStandardUpdate,
    GRIReporting, GRIReportingCreate, GRIReportingUpdate,
    GRIReport, GRIReportCreate, GRIReportUpdate
)
from ..repositories.gri_repository import GRIRepository

class GRIService:
    """GRI 표준 및 리포팅 관리 서비스"""
    
    def __init__(self):
        self.gri_repository = GRIRepository()
    
    # GRI Standards 관련 메서드
    async def get_all_standards(self) -> List[GRIStandard]:
        """모든 GRI 표준 조회"""
        return await self.gri_repository.get_all_standards()
    
    async def get_standard_by_id(self, standard_id: int) -> Optional[GRIStandard]:
        """ID로 GRI 표준 조회"""
        return await self.gri_repository.get_standard_by_id(standard_id)
    
    async def create_standard(self, standard_data: GRIStandardCreate) -> GRIStandard:
        """새로운 GRI 표준 생성"""
        # 코드 중복 확인
        existing_standard = await self.gri_repository.get_standard_by_code(standard_data.code)
        if existing_standard:
            raise ValueError("Standard code already exists")
        
        return await self.gri_repository.create_standard(standard_data)
    
    async def update_standard(self, standard_id: int, standard_data: GRIStandardUpdate) -> Optional[GRIStandard]:
        """GRI 표준 수정"""
        # 표준 존재 확인
        existing_standard = await self.gri_repository.get_standard_by_id(standard_id)
        if not existing_standard:
            return None
        
        # 코드 변경 시 중복 확인
        if standard_data.code and standard_data.code != existing_standard.code:
            duplicate_standard = await self.gri_repository.get_standard_by_code(standard_data.code)
            if duplicate_standard:
                raise ValueError("Standard code already exists")
        
        return await self.gri_repository.update_standard(standard_id, standard_data)
    
    async def delete_standard(self, standard_id: int) -> bool:
        """GRI 표준 삭제"""
        # 관련 리포팅이 있는지 확인
        related_reporting = await self.gri_repository.get_reporting_by_standard_id(standard_id)
        if related_reporting:
            raise ValueError("Cannot delete standard with existing reporting")
        
        return await self.gri_repository.delete_standard(standard_id)
    
    async def get_standards_by_category(self, category: str) -> List[GRIStandard]:
        """카테고리별 GRI 표준 조회"""
        return await self.gri_repository.get_standards_by_category(category)
    
    # GRI Reporting 관련 메서드
    async def get_all_reporting(self) -> List[GRIReporting]:
        """모든 GRI 리포팅 조회"""
        return await self.gri_repository.get_all_reporting()
    
    async def get_reporting_by_id(self, reporting_id: int) -> Optional[GRIReporting]:
        """ID로 GRI 리포팅 조회"""
        return await self.gri_repository.get_reporting_by_id(reporting_id)
    
    async def create_reporting(self, reporting_data: GRIReportingCreate) -> GRIReporting:
        """새로운 GRI 리포팅 생성"""
        # 표준 존재 확인
        standard = await self.gri_repository.get_standard_by_id(reporting_data.standard_id)
        if not standard:
            raise ValueError("GRI Standard not found")
        
        return await self.gri_repository.create_reporting(reporting_data)
    
    async def update_reporting(self, reporting_id: int, reporting_data: GRIReportingUpdate) -> Optional[GRIReporting]:
        """GRI 리포팅 수정"""
        # 리포팅 존재 확인
        existing_reporting = await self.gri_repository.get_reporting_by_id(reporting_id)
        if not existing_reporting:
            return None
        
        # 표준 변경 시 존재 확인
        if reporting_data.standard_id and reporting_data.standard_id != existing_reporting.standard_id:
            standard = await self.gri_repository.get_standard_by_id(reporting_data.standard_id)
            if not standard:
                raise ValueError("GRI Standard not found")
        
        return await self.gri_repository.update_reporting(reporting_id, reporting_data)
    
    async def delete_reporting(self, reporting_id: int) -> bool:
        """GRI 리포팅 삭제"""
        return await self.gri_repository.delete_reporting(reporting_id)
    
    async def get_reporting_by_period(self, period: str) -> List[GRIReporting]:
        """기간별 GRI 리포팅 조회"""
        return await self.gri_repository.get_reporting_by_period(period)
    
    # GRI Reports 관련 메서드
    async def get_all_reports(self) -> List[GRIReport]:
        """모든 GRI 리포트 조회"""
        return await self.gri_repository.get_all_reports()
    
    async def get_report_by_id(self, report_id: int) -> Optional[GRIReport]:
        """ID로 GRI 리포트 조회"""
        return await self.gri_repository.get_report_by_id(report_id)
    
    async def create_report(self, report_data: GRIReportCreate) -> GRIReport:
        """새로운 GRI 리포트 생성"""
        # 포함된 표준들이 존재하는지 확인
        for standard_id in report_data.standards_covered:
            standard = await self.gri_repository.get_standard_by_id(standard_id)
            if not standard:
                raise ValueError(f"GRI Standard {standard_id} not found")
        
        return await self.gri_repository.create_report(report_data)
    
    async def update_report(self, report_id: int, report_data: GRIReportUpdate) -> Optional[GRIReport]:
        """GRI 리포트 수정"""
        # 리포트 존재 확인
        existing_report = await self.gri_repository.get_report_by_id(report_id)
        if not existing_report:
            return None
        
        # 포함된 표준들이 존재하는지 확인
        if report_data.standards_covered:
            for standard_id in report_data.standards_covered:
                standard = await self.gri_repository.get_standard_by_id(standard_id)
                if not standard:
                    raise ValueError(f"GRI Standard {standard_id} not found")
        
        return await self.gri_repository.update_report(report_id, report_data)
    
    async def delete_report(self, report_id: int) -> bool:
        """GRI 리포트 삭제"""
        return await self.gri_repository.delete_report(report_id)
    
    # 통계 및 분석 메서드
    async def get_reporting_statistics(self) -> Dict[str, Any]:
        """리포팅 통계 조회"""
        total_standards = len(await self.get_all_standards())
        total_reporting = len(await self.get_all_reporting())
        total_reports = len(await self.get_all_reports())
        
        return {
            "total_standards": total_standards,
            "total_reporting": total_reporting,
            "total_reports": total_reports,
            "completion_rate": (total_reporting / total_standards * 100) if total_standards > 0 else 0
        }
    
    async def get_standards_compliance_matrix(self) -> Dict[str, Any]:
        """표준 준수 매트릭스 조회"""
        standards = await self.get_all_standards()
        reporting = await self.get_all_reporting()
        
        compliance_matrix = {}
        for standard in standards:
            standard_reporting = [r for r in reporting if r.standard_id == standard.id]
            compliance_matrix[standard.code] = {
                "title": standard.title,
                "category": standard.category,
                "status": "Completed" if standard_reporting else "Not Started",
                "reporting_count": len(standard_reporting)
            }
        
        return compliance_matrix
