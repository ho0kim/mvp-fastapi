# mvp-fastapi
Fast api 로 rest api 구축 틀만 만들어보기로 하자.  
토이 프로젝트로 구현 후 쓸만하면 팀 내 매니지먼트 센터 페이지 구현 백엔드로 사용할 예정이다.  
  
## Fast api 활용 사유
- 팀 내 주력 언어가 python과 sql 밖에 없다.. C/C++을 쓰긴하지만 주류는 아닌..(나는 자반데..)  
- 팀 내 인원들이 기본적인 Rest api 구조 및 서버 사이드 통신 구현을 할 줄 모른다..  
  (최대한 러닝커브가 낮아야한다)  
- 내부 인원들이 딴 일 하느라 시간이 별로 없다.  
  (생산성을 맥시멈으로 쥐어 짤 수 있는... )  
- Flask 대비 빠른 속도, 러닝커브 낮은 쉬운 프레임웍  
  (최근 관심도를 보면.. fast api가 압도적은 아니지만 그냥 쓰고싶었음..)  
- Django 대비 가벼움  
  (무거운건 필요없다.. 어차피 데이터를 외부에 전달할 수 있는 인터페이스 용도 그 이상도 이하도 아님)  
- DI 위주의 설계로 DB등의 의존성 관리가 편리, 버그 위험이 적음.  
- 비동기 처리가 가능하다 성능이 좋다
- Pydantic 기반, Validation이 잘 동작한다고 한다(테스트 해볼 예정)
- Swagger기반 자동화 문서가 효율적
  (모르는 사람이 보기엔 좋아보이지만 swagger 그냥 만들면 되는것..읍)
- 공식 문서가 잘되어있다. (이건 맞다.)

## 하지만 불안한 점 (여기저기서 들은 카더라 정리)
- major 1.0 버전 deploy가 아직 안되어있다.  (현재 0.79.0)
- 전반적인 아키텍처 스탠다드가 없는 느낌, boilerplate 코드들이 제시해주는 dir 구성이라던지 예시들은 있지만 표준화된 지침이 없다.
  (micro framework를 지향하는데서 나오는 부분인지는 모르겠으나 아쉽.)
- 비동기 처리는 쉬우나 비동기 DB 세션처리가 필요하다한다. (구현해봐야아겠음)
- ORM 을 sqlarchemy로 붙인다. 간단한 쿼리로 데이터 던지기는 좋지만, 쿼리가 복잡해질수록 투입 리소스가 많아 질 수 있음.
- 상황에 따라 동적 lazy_loading, fetch로딩을 걸어주려면 직접 구현해야함 (sqlachemy의 단점이라함)

-------------

## 구현 필요 사항
- 전체 디렉토리 구조 잡기
- 기본적인 Rest api 구조 구현
- auth. key를 통한 접근 구현
- jwt 토큰 활용
- rdb 연동을 위한 모듈 구현
- 혹시 모르니 trino jdbc 연결 모듈 구현
- 미들웨어 단에서 로깅 구조 구현
- dockerfile 추가
- gitlab cicd yaml 구현
- config 활용
