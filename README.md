# Multi-LLM RAG Framework

## 프로젝트 설명
이 프로젝트는 RAG프레임워크를 사용하여 여러 LLM 컨테이너와 통신하는 방법을 시연합니다.

## 구조
- **framework/**: LLM 컨테이너와 통신하는 Flask 애플리케이션.
- **llm/**: 간단한 상태 정보를 제공하는 Flask 애플리케이션.
- **docker-compose.yml**: 두 개의 컨테이너를 정의하고 설정하는 Docker Compose 파일.

## 실행 방법
1. `docker-compose build` 명령어를 사용하여 Docker 이미지를 빌드합니다.
2. `docker-compose up` 명령어를 사용하여 컨테이너를 시작합니다.
3. 브라우저에서 `http://localhost:5000/check_llm_status`에 접속하여 LLM 컨테이너의 상태를 확인합니다.
