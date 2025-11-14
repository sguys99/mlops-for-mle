# MLOps for MLE - Project Context

## 프로젝트 개요

이 프로젝트는 MLOps(Machine Learning Operations) 교육용 자료입니다. 실무에서 필요한 ML 시스템 구축의 전체 파이프라인을 단계별로 학습할 수 있도록 구성되어 있습니다.

**공식 튜토리얼**: https://mlops-for-mle.github.io/tutorial/

## 프로젝트 구조

```
mlops-for-mle/
├── archive/          # 기존 교육 자료 (레거시 코드)
│   ├── part1/       # 데이터 파이프라인
│   ├── part2/       # 모델 학습
│   ├── part3/       # 모델 레지스트리
│   ├── part5/       # API 개발
│   └── part6/       # 모델 배포
├── src/             # 개선된 새로운 코드 (작업 중)
│   └── part1/       # 데이터 파이프라인 개선 버전
├── pyproject.toml   # 프로젝트 의존성 관리 (uv)
└── README.md
```

## 기술 스택

### Core Dependencies
- **Python**: >=3.12
- **FastAPI**: >=0.121.1 - REST API 프레임워크
- **pandas**: >=2.3.3 - 데이터 처리
- **psycopg2-binary**: >=2.9.11 - PostgreSQL 연결
- **scikit-learn**: >=1.7.2 - 머신러닝 모델
- **sqlalchemy**: >=2.0.44 - ORM 및 데이터베이스 추상화

### Infrastructure
- **Docker & Docker Compose** - 컨테이너화
- **PostgreSQL** - 데이터 저장소 및 MLFlow 백엔드
- **MinIO** - S3 호환 객체 스토리지 (모델 아티팩트)
- **MLFlow** - 실험 추적 및 모델 레지스트리

## 커리큘럼 구조

### Part 1: Data Pipeline & Infrastructure
**위치**: [archive/part1](archive/part1/)

**학습 목표**:
- Docker/Docker Compose를 활용한 인프라 구축
- PostgreSQL 데이터베이스 설정 및 관리
- 지속적인 데이터 스트리밍 파이프라인 구축
- ETL 기초 (sklearn.datasets → PostgreSQL)

**주요 파일**:
- `data_generator.py` - Iris 데이터셋 생성 및 DB 삽입
- `table_creator.py` - PostgreSQL 테이블 스키마 생성
- `docker-compose.yaml` - PostgreSQL 오케스트레이션

**현재 상태**: src/part1에서 개선 작업 진행 중

---

### Part 2: Model Training & Experimentation
**위치**: [archive/part2](archive/part2/)

**학습 목표**:
- scikit-learn 파이프라인 구축 (StandardScaler + SVC)
- 다양한 데이터 소스에서 학습 (CSV, Database)
- 모델 검증 및 직렬화 (joblib)
- Train/Test 분리 및 평가 지표

**주요 파일**:
- `pipeline_train.py` - 기본 ML 파이프라인 학습
- `db_train.py` - PostgreSQL 기반 학습
- `pipeline_validate_save_model.py` - 모델 검증 및 저장

---

### Part 3: Model Registry & Artifact Management
**위치**: [archive/part3](archive/part3/)

**학습 목표**:
- MLFlow 실험 추적 및 모델 레지스트리
- MinIO를 활용한 S3 호환 아티팩트 저장
- 모델 버저닝 및 메타데이터 관리
- ML 라이프사이클 전체 관리

**주요 파일**:
- `save_model_to_registry.py` - MLFlow 모델 등록
- `load_model_from_registry.py` - 등록된 모델 로드
- `docker-compose.yaml` - MLFlow + PostgreSQL + MinIO 인프라

---

### Part 5: API Development & Model Serving
**위치**: [archive/part5](archive/part5/)

**학습 목표**:
- FastAPI를 활용한 REST API 구축
- Pydantic 모델을 통한 요청/응답 검증
- CRUD 연산 구현 (Create, Read, Update, Delete)
- HTTP 엔드포인트 및 에러 핸들링

**주요 파일**:
- `crud_pydantic.py` - FastAPI CRUD 구현
- `Dockerfile` - FastAPI 서비스 컨테이너화

---

### Part 6: Model Deployment & Artifact Download
**위치**: [archive/part6](archive/part6/)

**학습 목표**:
- MLFlow 레지스트리에서 모델 아티팩트 다운로드
- 모델 배포 및 추론 준비
- 버전 관리된 아티팩트 활용
- 커맨드라인 모델 관리 도구

**주요 파일**:
- `download_model.py` - MLFlow 모델 다운로드

---

## 학습 경로

이 커리큘럼은 **점진적인 MLOps 워크플로우**를 따릅니다:

1. **Part 1** → 데이터 기반 구축 (Database + Streaming Pipeline)
2. **Part 2** → 모델 학습 및 실험 (Algorithm + Preprocessing Iteration)
3. **Part 3** → 모델 관리 (MLFlow Registry + Artifact Storage)
4. **Part 5** → API 기능 노출 (FastAPI Fundamentals)
5. **Part 6** → 모델 배포 (Registered Model Serving)

**Note**: Part 4는 아카이브에 없음 (테스팅, 검증, 프로덕션 배포 전략 등이 포함되었을 가능성)

## 개발 방향 (archive → src)

### 개선 목표
`archive/`의 레거시 코드를 `src/`에서 다음과 같이 개선:

1. **코드 품질 향상**
   - 타입 힌팅 추가 (Type Hints)
   - 에러 핸들링 강화
   - 로깅 및 모니터링 추가
   - 보안 강화 (SQL Injection 방어 등)

2. **아키텍처 개선**
   - 모듈화 및 재사용성 향상
   - 설정 관리 분리 (Config Management)
   - 의존성 주입 패턴 적용
   - 테스트 가능한 구조 설계

3. **MLOps Best Practices**
   - CI/CD 파이프라인 통합
   - 모델 모니터링 및 드리프트 감지
   - 데이터 검증 및 품질 체크
   - 재현 가능성 (Reproducibility) 보장

4. **프로덕션 준비**
   - 환경 변수 기반 설정
   - Health check 엔드포인트
   - Graceful shutdown 처리
   - 성능 최적화

### 현재 진행 상황
- **Part 1**: [src/part1/data_generator.py](src/part1/data_generator.py) 작업 시작
- **Part 2-6**: 아직 미작업 상태

## 개발 환경 설정

### 패키지 관리
이 프로젝트는 **uv**를 사용하여 의존성을 관리합니다.

```bash
# 의존성 설치
uv sync

# 가상환경 활성화
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

### 데이터베이스 설정
PostgreSQL은 Docker Compose를 통해 실행됩니다:

```bash
# archive의 해당 part 디렉토리에서 실행
cd archive/part1
docker-compose up -d
```

**기본 연결 정보**:
- Host: localhost
- Port: 5432
- User: myuser
- Password: mypassword
- Database: mydatabase

## 작업 시 주의사항

### archive 코드 다룰 때
- archive는 **교육용 레퍼런스**이며, 실제 프로덕션 수준은 아님
- 보안 이슈가 있을 수 있음 (예: SQL Injection 취약점)
- 하드코딩된 credentials 존재

### src 코드 작성 시
- archive의 기능을 유지하되, 코드 품질을 향상시킬 것
- 교육 자료의 간결성과 실무 품질 사이의 균형 유지
- 학습 목표를 해치지 않는 범위에서 개선
- 각 Part의 독립성 유지 (순차적 학습 가능하도록)

## 참고 자료

- **공식 튜토리얼**: https://mlops-for-mle.github.io/tutorial/
- **FastAPI 문서**: https://fastapi.tiangolo.com/
- **MLFlow 문서**: https://mlflow.org/docs/latest/index.html
- **scikit-learn 문서**: https://scikit-learn.org/stable/

## Git 정보

- **현재 브랜치**: main
- **최근 커밋**:
  - 486b2ff - Relocate files
  - fa4731c - Add the dependency(sqlalchemy)
  - 57417c0 - Add dependencies(pandas, psycopg2-binary, scikit-learn)
  - 9925b9f - Add the dependency(fastapi)
  - 9aa6e57 - Update project files to migrate to uv

## 개발 워크플로우

### archive 코드 개선하기
1. archive/partN의 코드 분석 및 이해
2. 학습 목표 및 핵심 개념 파악
3. src/partN에 개선된 버전 작성
4. 기능 동등성 확인 (원래 동작 유지)
5. 추가 개선사항 적용 (타입 힌팅, 에러 핸들링 등)
6. 문서화 및 주석 추가

### 코드 리뷰 포인트
- 교육 자료로서의 가독성 유지
- 실무 적용 가능한 패턴 사용
- 보안 취약점 제거
- 테스트 가능한 구조
- 설정의 외부화 (하드코딩 제거)
