# FastAPI Templates - 3-Tier Architecture

FastAPI 프로젝트를 빠르게 시작하기 위한 템플릿입니다. 현재 브랜치에서는 3-Tier 구조를 FastAPI로 구현하였습니다.

## 폴더 구조
```
src/
├── adapters/                        # 외부 시스템(데이터베이스, 메시지 브로커 등)과의 연동 책임
│   └── something_adapter.py         # [예시] 특정 외부 시스템과의 통신 로직 구현
├── core/                            # 프로젝트 전역에서 사용되는 핵심 설정, 유틸리티, 공통 기능
│   └── templates.py                 # Jinja2 템플릿 관련 공통 함수
├── routers/                         # FastAPI의 엔드포인트 라우터 집합 (URL 경로별 분리)
│   ├── api/                         # API 엔드포인트 관련 라우터
│   │   ├── ping/                    # 하위 API 기능별 라우터
│   │   │   └── ping_router.py       # ping API 엔드포인트 라우터
│   │   └── api_router.py            # API 라우터들을 하나로 통합하는 엔트리 포인트
│   └── page/                        # 페이지 렌더링(HTML 등) 관련 라우터
│       ├── main/                    # 메인 페이지 라우터
│       │   └── main_router.py       # 메인 페이지 라우터 정의
│       └── page_router.py           # 페이지 라우터들을 하나로 통합하는 엔트리 포인트
├── services/                        # 비즈니스 로직 및 서비스 계층
│   └── something_service.py         # 특정 비즈니스 로직(서비스) 구현
├── templates/                       # Jinja2 등 템플릿 파일 저장 디렉터리
│   └── main_template.jinja          # 메인 페이지용 Jinja2 템플릿 파일
├── views/                           # 뷰 계층, 서비스와 템플릿 연결 및 렌더링 책임
│   └── main_view.py                 # 메인 페이지 뷰 함수 정의
└── main.py                          # FastAPI 앱의 엔트리 포인트, 앱 생성 및 api, page 라우터 등록
```

## 앱 실행 명령어

**개발 환경**
```bash
$ fastapi dev src/main.py
```

**프로덕션 환경**
```bash
$ fastapi run src/main.py
```

* 루트 디렉토리에서 위 명령어 실행
* `--host 0.0.0.0` : 외부 접속 허용 가능
* `--port 포트` : 특정 포트로 앱 실행