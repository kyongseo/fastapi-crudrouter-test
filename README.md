# FastAPI Authentication & CRUD with PostgreSQL

## 소개
이 프로젝트는 FastAPI를 사용하여 사용자 인증, JWT 기반 토큰 관리 및 기본 CRUD 기능을 제공하는 애플리케이션입니다. 데이터베이스는 PostgreSQL을 사용하며 Docker를 통해 실행됩니다.

---

## 주요 기능
1. 사용자 등록 및 로그인 (JWT 인증)
2. 리프레시 토큰 지원
3. `Post` CRUD API (FastAPI-CRUDRouter 활용)

---

## 설치 및 실행
### 요구 사항
- Docker
- Docker Compose
- Python 3.11.4
- venv
- pip
- make

### 설정 및 실행
1. 프로젝트를 클론합니다.
   ```bash
   git clone <your-repository-url>
   cd <project-folder>
   ```

2. 필요한 환경 변수를 설정합니다. `.env` 파일을 생성합니다.
   ```env
   POSTGRES_USER=boilerplate_user
   POSTGRES_PASSWORD=boilerplate
   POSTGRES_HOST=db
   POSTGRES_PORT=5432
   POSTGRES_DB=boilerplate-dev-db
   SECRET_KEY=your_secret_key
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   REFRESH_TOKEN_EXPIRE_MINUTES=1440
   ```

3. Docker Compose를 사용하여 애플리케이션을 실행합니다.
   ```bash
   docker-compose up --build
   ```

4. 애플리케이션은 기본적으로 [http://localhost:8000](http://localhost:8000)에서 실행됩니다.

---

## API 문서
FastAPI의 내장 문서를 통해 API를 테스트할 수 있습니다.
- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## Docker Compose 파일
아래는 `docker-compose.yml` 파일입니다.
```yaml
version: "3.9"

services:
  app:
    build:
      context: .
    ports:
      - "8000:8000"
    env_file:
      - .env
    depends_on:
      - db

  db:
    image: postgres:15
    restart: always
    environment:
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB}
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

---

## Dockerfile
아래는 `Dockerfile`의 내용입니다.
```dockerfile
FROM python:3.11.4-slim

# 작업 디렉토리 생성
WORKDIR /app

# 필수 패키지 설치
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Python 패키지 종속성 추가
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY ./app ./app

# FastAPI 서버 실행
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## 디렉토리 구조
```
project-folder/
├── app/
│   ├── main.py          # FastAPI 애플리케이션
│   ├── models.py        # SQLAlchemy 모델 정의
│   ├── schemas.py       # Pydantic 스키마 정의
│   ├── auth.py          # 인증 로직
│   └── database.py      # 데이터베이스 설정
├── Dockerfile            # Docker 파일
├── docker-compose.yml    # Docker Compose 파일
├── requirements.txt      # Python 종속성 목록
└── README.md             # 프로젝트 설명
```

---

## `requirements.txt`
아래는 애플리케이션에 필요한 Python 패키지 목록입니다.
```
fastapi
uvicorn
sqlalchemy
pydantic
passlib
python-jose
fastapi-crudrouter
psycopg2-binary
python-dotenv
```

### Python 패키지 설치
```bash
pip install -r requirements.txt
```

---

### 주요 명령어
1. `make service-build`
   - Docker Compose를 사용하여 모든 서비스를 빌드합니다.

2. `make service-up`
   - Docker Compose를 사용하여 모든 서비스를 백그라운드에서 실행합니다.

3. `make service-down`
   - Docker Compose를 사용하여 실행 중인 모든 서비스를 중지합니다.

4. `make service-clean`
   - Docker Compose를 사용하여 실행 중인 서비스를 중지하고, 모든 볼륨 데이터를 삭제합니다.

5. `make api-up`
   - FastAPI 애플리케이션 컨테이너(`app`)를 시작합니다.

6. `make api-down`
   - FastAPI 애플리케이션 컨테이너(`app`)를 중지합니다.

7. `make api-restart`
   - FastAPI 애플리케이션 컨테이너(`app`)를 재시작합니다.

8. `make api-log`
   - FastAPI 애플리케이션(`app`)의 로그를 실시간으로 확인합니다.

---

## 실행 후 확인
1. PostgreSQL 컨테이너가 실행 중인지 확인합니다.
   ```bash
   docker ps
   ```

2. Swagger UI를 열어 API를 테스트합니다.
   [http://localhost:8000/docs](http://localhost:8000/docs)

3. 데이터베이스 상태를 확인하려면 PostgreSQL 컨테이너 내부로 접근합니다.
   ```bash
   docker exec -it <container_id> psql -U boilerplate_user -d boilerplate-dev-db
   ```
