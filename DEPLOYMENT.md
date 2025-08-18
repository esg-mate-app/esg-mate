# ESG Mate MSA 배포 가이드

## 🚀 배포 아키텍처

```
┌─────────────────┐    ┌─────────────────┐
│   Next.js       │    │   FastAPI       │
│   Frontend      │    │   Backend       │
│                 │    │                 │
│   Vercel        │    │   Railway       │
│   (포트: 3000)  │    │   (포트: 8080)  │
└─────────────────┘    └─────────────────┘
         │                       │
         └───────────────────────┘
                 API 통신
```

## 📋 사전 준비사항

### 1. Vercel 설정
- [Vercel](https://vercel.com) 계정 생성
- 새 프로젝트 생성 (GitHub 연동)
- 환경 변수 설정:
  - `NEXT_PUBLIC_API_URL`: Gateway 서비스 URL

### 2. Railway 설정
- [Railway](https://railway.app) 계정 생성
- 각 서비스별 프로젝트 생성:
  - `gateway-service` (포트 8080)
  - `auth-service` (포트 8008)
  - `materiality-service` (포트 8002)
  - `gri-service` (포트 8003)
  - `tcfd-service` (포트 8005)
  - `chatbot-service` (포트 8001)

### 3. GitHub Secrets 설정
Repository Settings > Secrets and variables > Actions에서 다음 설정:

#### Frontend (Vercel)
```
VERCEL_TOKEN=your_vercel_token
VERCEL_ORG_ID=your_org_id
VERCEL_PROJECT_ID=your_project_id
```

#### Backend (Railway)
```
RAILWAY_TOKEN=your_railway_token
```

## 🔧 배포 단계

### 1. Frontend 배포 (Vercel)
```bash
# 자동 배포 (GitHub Actions)
git push origin main

# 수동 배포
cd frontend
vercel --prod
```

### 2. Backend 배포 (Railway)
```bash
# 자동 배포 (GitHub Actions)
git push origin main

# 수동 배포
cd gateway
railway up

cd ../service/auth-service
railway up

# ... 기타 서비스들
```

## 🌐 환경 변수 설정

### Frontend (.env.production)
```bash
NEXT_PUBLIC_API_URL=https://your-gateway.railway.app
NEXT_PUBLIC_APP_NAME=ESG Mate
NEXT_PUBLIC_APP_VERSION=1.0.0
```

### Backend (Railway 환경 변수)
```bash
# Gateway Service
PORT=8080
DEBUG=False

# Auth Service
PORT=8008
JWT_SECRET_KEY=your-secret-key
DEBUG=False

# Materiality Service
PORT=8002
DEBUG=False

# GRI Service
PORT=8003
DEBUG=False

# TCFD Service
PORT=8005
DEBUG=False

# Chatbot Service
PORT=8001
OPENAI_API_KEY=your-openai-key
DEBUG=False
```

## 📊 서비스별 포트 및 URL

| 서비스 | 포트 | Railway URL | 상태 |
|--------|------|-------------|------|
| Gateway | 8080 | `https://gateway-service.railway.app` | 🚀 |
| Auth | 8008 | `https://auth-service.railway.app` | 🚀 |
| Materiality | 8002 | `https://materiality-service.railway.app` | 🚀 |
| GRI | 8003 | `https://gri-service.railway.app` | 🚀 |
| TCFD | 8005 | `https://tcfd-service.railway.app` | 🚀 |
| Chatbot | 8001 | `https://chatbot-service.railway.app` | 🚀 |

## 🔍 헬스체크 엔드포인트

각 서비스의 헬스체크:
```bash
# Gateway
curl https://gateway-service.railway.app/health

# Auth Service
curl https://auth-service.railway.app/health

# Materiality Service
curl https://materiality-service.railway.app/health

# GRI Service
curl https://gri-service.railway.app/health

# TCFD Service
curl https://tcfd-service.railway.app/health

# Chatbot Service
curl https://chatbot-service.railway.app/health
```

## 🚨 문제 해결

### 1. 배포 실패 시
- GitHub Actions 로그 확인
- Railway 로그 확인
- 환경 변수 설정 확인
- 포트 충돌 확인

### 2. 서비스 간 통신 문제
- CORS 설정 확인
- 서비스 URL 확인
- 네트워크 정책 확인

### 3. 성능 최적화
- Railway 인스턴스 크기 조정
- 캐싱 전략 적용
- 로드밸런싱 설정

## 📈 모니터링

### 1. Vercel Analytics
- 페이지 뷰
- 성능 메트릭
- 사용자 행동

### 2. Railway Metrics
- CPU 사용률
- 메모리 사용률
- 네트워크 트래픽
- 응답 시간

## 🔄 CI/CD 파이프라인

### Frontend 배포 흐름
1. `main` 브랜치에 푸시
2. GitHub Actions 트리거
3. 테스트 실행
4. 빌드 검증
5. Vercel 배포

### Backend 배포 흐름
1. `main` 브랜치에 푸시
2. GitHub Actions 트리거
3. 각 서비스별 테스트
4. Railway 배포
5. 헬스체크 검증

## 📝 배포 체크리스트

- [ ] GitHub Secrets 설정 완료
- [ ] Vercel 프로젝트 생성 및 설정
- [ ] Railway 프로젝트들 생성 및 설정
- [ ] 환경 변수 설정 완료
- [ ] 첫 번째 배포 테스트
- [ ] 서비스 간 통신 테스트
- [ ] 헬스체크 엔드포인트 확인
- [ ] 모니터링 설정 완료

## 🎯 다음 단계

1. **로컬 테스트**: 모든 서비스가 로컬에서 정상 작동하는지 확인
2. **첫 배포**: 각 서비스를 개별적으로 배포하여 테스트
3. **통합 테스트**: 전체 시스템이 정상 작동하는지 확인
4. **모니터링**: 성능 및 오류 모니터링 설정
5. **자동화**: 추가적인 CI/CD 파이프라인 구축
