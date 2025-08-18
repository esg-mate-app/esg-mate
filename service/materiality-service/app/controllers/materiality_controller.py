from fastapi import APIRouter, HTTPException, Depends
from typing import List
from ..models.materiality_models import (
    MaterialityTopic, MaterialityTopicCreate, MaterialityTopicUpdate,
    MaterialityAssessment, MaterialityAssessmentCreate, MaterialityAssessmentUpdate,
    MaterialityMatrix
)
from ..services.materiality_service import MaterialityService

router = APIRouter()
materiality_service = MaterialityService()

@router.get("/", response_model=dict)
async def root():
    """Materiality Service 루트 엔드포인트"""
    return {
        "message": "Materiality Service",
        "port": 8002,
        "endpoints": ["/topics", "/assessments", "/matrix", "/health"]
    }

@router.get("/health")
async def health_check():
    """Materiality Service 헬스체크"""
    return {
        "status": "healthy",
        "service": "materiality",
        "port": 8002
    }

@router.get("/topics", response_model=List[MaterialityTopic])
async def get_materiality_topics():
    """모든 중요도 주제 조회"""
    try:
        topics = await materiality_service.get_all_topics()
        return topics
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/topics/{topic_id}", response_model=MaterialityTopic)
async def get_materiality_topic(topic_id: int):
    """특정 중요도 주제 조회"""
    try:
        topic = await materiality_service.get_topic_by_id(topic_id)
        if not topic:
            raise HTTPException(status_code=404, detail="Topic not found")
        return topic
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/topics", response_model=MaterialityTopic)
async def create_materiality_topic(topic_data: MaterialityTopicCreate):
    """새로운 중요도 주제 생성"""
    try:
        topic = await materiality_service.create_topic(topic_data)
        return topic
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/topics/{topic_id}", response_model=MaterialityTopic)
async def update_materiality_topic(topic_id: int, topic_data: MaterialityTopicUpdate):
    """중요도 주제 수정"""
    try:
        topic = await materiality_service.update_topic(topic_id, topic_data)
        if not topic:
            raise HTTPException(status_code=404, detail="Topic not found")
        return topic
    except HTTPException:
        raise
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/topics/{topic_id}")
async def delete_materiality_topic(topic_id: int):
    """중요도 주제 삭제"""
    try:
        success = await materiality_service.delete_topic(topic_id)
        if not success:
            raise HTTPException(status_code=404, detail="Topic not found")
        return {"message": "Topic deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/assessments", response_model=List[MaterialityAssessment])
async def get_assessments():
    """모든 중요도 평가 조회"""
    try:
        assessments = await materiality_service.get_all_assessments()
        return assessments
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/assessments/{assessment_id}", response_model=MaterialityAssessment)
async def get_assessment(assessment_id: int):
    """특정 중요도 평가 조회"""
    try:
        assessment = await materiality_service.get_assessment_by_id(assessment_id)
        if not assessment:
            raise HTTPException(status_code=404, detail="Assessment not found")
        return assessment
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/assessments", response_model=MaterialityAssessment)
async def create_assessment(assessment_data: MaterialityAssessmentCreate):
    """새로운 중요도 평가 생성"""
    try:
        assessment = await materiality_service.create_assessment(assessment_data)
        return assessment
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/assessments/{assessment_id}", response_model=MaterialityAssessment)
async def update_assessment(assessment_id: int, assessment_data: MaterialityAssessmentUpdate):
    """중요도 평가 수정"""
    try:
        assessment = await materiality_service.update_assessment(assessment_id, assessment_data)
        if not assessment:
            raise HTTPException(status_code=404, detail="Assessment not found")
        return assessment
    except HTTPException:
        raise
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/assessments/{assessment_id}")
async def delete_assessment(assessment_id: int):
    """중요도 평가 삭제"""
    try:
        success = await materiality_service.delete_assessment(assessment_id)
        if not success:
            raise HTTPException(status_code=404, detail="Assessment not found")
        return {"message": "Assessment deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/matrix", response_model=MaterialityMatrix)
async def get_materiality_matrix():
    """중요도 매트릭스 조회"""
    try:
        matrix = await materiality_service.get_materiality_matrix()
        return matrix
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
