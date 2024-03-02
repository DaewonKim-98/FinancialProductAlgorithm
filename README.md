# 팀원 정보
- 팀장 : 서울 3반 이재종
- 팀원 : 서울 3반 김대원

<br>

# 프로젝트 일정 및 역할 분배
![image-1](https://github.com/DaewonKim-98/FinancialProductAlgorithm/assets/139425563/5b14c6ad-b03b-44f3-b962-4d7b321be807)
- 프로젝트 기간에 맞게 단계별로 꾸준히 구현 및 테스트 보완하였습니다.   

<br>

# 설계 내용
## 개발 환경 및 아키텍처
#### 개발환경
![Alt text](images/image-4.png)

## 아키텍처
- Django REST Framework & Vue3

### 1. DB 설계 - ERD 작성
![Alt text](images/image.png)

### 2. 메인 컴포넌트 설계
![Alt text](images/image-2.png)

### 3. 프론트 설계 - UI/UX 대략적인 구조
![Alt text](images/image-3.png)

<br>

# 금융 상품 추천 알고리즘에 대한 기술적 설명
## 타겟 인사이트 도출
- 금융 지식이 부족한 현대인들과 이에 따라 가장 무난한 상품을 투자하는 경향이 두드러짐
![Alt text](images/image-5.png)
![Alt text](images/image-6.png)

- 이는 편승효과(밴드왜건 효과)를 빗대어 설명할 수 있는데, 다수의 소비자나 유행을 따라 상품을 구입하는 현상
- 특히 해당 분야의 지식이 부족할 때 편승 효과가 커지는 경향이 있음
![Alt text](images/image-7.png)
![Alt text](images/image-8.png)

## 추천 방법
- 목표가 주택마련이기 떄문에 본인과 유사한 거주지를 희망하고, 총 자산이 비슷한 사람들은 어떤 상품을 가입했는지 추천

## 기술적 설명
1. 현재 사용자와 같은 희망 거주지를 
선택한 유저 목록 추출
2. 나의 총자산의 + 25%, -25% 내에 포함되는
유저 목록 추출
3. 해당 유저들의 id를 통해 유저들의 가입 상품 리스트
를 한곳에 전달
4. 해당 리스트를 순회하며 빈도 체크 후
빈도순으로 10개 정렬하여 출력

<br>

# 서비스 대표 기능들에 대한 설명
1. 금융 상품 조회 및 정렬
2. 환율 계산기
3. 내 주변 은행 검색
4. 게시판

<br>

# 일자별 진행도 및 느낀점
## 231116
### 진행도
- Jira 툴을 활용한 우선순위 판단 및 일정 관리
- 팀원과의 브레인스토밍을 통한 금융 상품 추천 알고리즘 결정
- 결정한 금융 상품 추천 알고리즘에 필요한 ERD 작성 (drowio)
- figma 툴을 활용한 디자인 설계
- 금융감독원 오픈 API를 통한 데이터 요청 후 필요한 필드만 별도 가공하여 저장
- Vue with DRF를 활용한 회원가입 시스템 구현
### 느낀 점
- 금융 상품 추천 알고리즘에 필요한 유저의 추가 정보를 회원가입 할 때에 추가 필드로 가공하는 과정에서 추가 정보가 DB에 저장 되지 않는 에러 발생
- 오픈 API의 데이터 가공 시, NULL 값으로 인한 에러를 따로 가공하는 과정에서 코드 가독성이 떨어졌다. 

## 231117
### 진행도
- 회원관리 시스템 전체 구현 완료
- 예적금 금리 비교 : 전체조회 구현 및 상품기간별 금리 조회 구현
- 예적금 검색 폼 구현 완료
### 느낀점
- 예적금 데이터에서 테이블 단순 출력이 아닌 컬럼명을 한글로 변경하고, 정렬이 가능한 별도의 테이블로 재가공 하는 과정에서 시간을 많이 할애하였다.
- 테이블 가공을 위한 데이터 저장 타이밍을 결정하는데에 비동기 처리가 원할하게 되지 않았다. 

## 231120
### 진행도
- 환율 계산기 구현
- 예적금 금리 상세 조회 구현
- 예적금 금리 상세 조회 페이지에서 로컬 스토리지에 가입 상품 추가 가능
- 프로필 페이지에서 가입한 상품 확인 및 삭제 기능 구현
- 회원가입, 로그인 캘린더 선택 되지 않는 오류 해결
- 커뮤니티 페이지에서 게시물 생성, 상세 페이지 기능 구현
### 느낀점
- 캘린더에서 선택 되지 않는 부분을 구글링과 GPT를 통해 해결하려 했으나 시간이 너무 오래 걸렸다.
- 환율 API에서 양방향 v-model 과정에서 두가지 인풋을 동시에 변환하려다 무한 루프에 빠지는 경우가 있었다.
- 로컬 스토리지에 저장된 상품을 각각의 유저 DB와 연결해야하는 부분에서 user id를 가입 상품과 같이 저장하였으나, 다른 컴퓨터에서 접속 시 로컬 스토리지가 확인되지 않아 재구현이 필요하다고 느꼈다.
- 커뮤니티에서 작성자의 이름이 보이도록 만드는 것을 구현하는데 오래 걸렸다.
- 게시물 수정, 삭제, 댓글 생성, 삭제 등의 기능을 구현하려 했으나 실패했다.

## 231121
### 진행도
- 마이페이지에서 금융상품 추천을 위한 추가 정보 입력 폼 구현
- 추가 정보 입력 모델, 시리얼라이저, 저장 확인
- 커뮤니티 페이지 게시물 수정, 삭제, 댓글 생성, 삭제 기능 구현
- 은행 지도 생성, 검색 기능 구현
- 마이페이지에서 개인 정보 수정 기능 구현
### 느낀점
- vue에서는 현재 유저 정보를 로컬스토리지에 저장된 auth Token을 활용하여 다시 django로 보내줘야하는 과정을 미리 활용했어야하는데, 회원관리와 뒤늦게 활용하려하다보니 이전 코드들의 수정사항이 많아졌고, 사전 설계의 중요성을 느꼈다. 
- 은행 지도를 생성할 때 export default 부분이 잘 이해가 되지 않아 힘들었다.
- css와 병행하는 것이 쉽지 않았다.

## 231122
### 진행도
- 각 시/군/구 별 아파트 실 거래가를 DB 저장
- 상품 추천 받기 알고리즘을 구상하고 실현
- 유저 정보를 로컬 스토리지에 저장하지 않고 USER DB와 관계된 모델을 생성 후, 저장해서 다른 컴퓨터에서도 사용할 수 있게 구성
- 금융상품별 상세페이지로 들어갈 때 금융상품 선택을 다르게 했을 때 들어가지지 않는 버그를 수정
### 느낀점
- 알고리즘 테스트를 위해 더미데이터 무작위 생성을 시도하였으나 다양한 관계로 설정된 모델의 필드를 고려하는 부분과, 파일의 위치를 import하는 과정에서 포기하게 되었다. 
- 상품 추천 받기 알고리즘을 구상하는데 시간이 오래 걸렸고 단순하게 구현하는 것만으로도 힘들어서 어려움을 겪었다.

## 231123
### 진행도
- 프로젝트 최종 테스트 및 보완
- CSS 적용
- 가상의 유저 데이터 생성
### 느낀점
- 가상의 랜덤 유저 데이터 목록을 생성하는 과정에서 api가 필요한 각각의 필드를 구현하는 부분에서 api를 활용하여 요청과 반환 구조를 완벽하게 다루게 되었다.

## 마무리하며
- 이번 프로젝트를 시작할 때 이런 말을 보게 되었습니다. “아무리 유명한 화가라도 스케치 없이 그림을 완성할 수는 없다.” 처음 프로젝트를 시작할 때는 설계가 그렇게 중요할까? 하며 생각 없이 넘겼는데, 프로젝트를 진행하며 누구보다 설계의 중요성을 뼈저리게 느끼게 되었습니다. 프로젝트 초기에 ERD 및 컴포넌트의 설계가 미흡했다면 진행과정에서 현재 진행도와 필요한 작업의 우선순위를 판단하기 어려워 큰 어려움을 느낄 수 있었다고 생각했습니다.
