# 8조 냉장고
## spartamarket Project

### 프로젝트 소개
- 온라인상의 중고마켓(결제 기능 X)

### 팀 소개
- Django 에서 따온 8조 냉Django
- 팀장: 서영환
- 서기: 이새예
- 팀원: 김나희, 김나현(A)

### 프로젝트 주요기능

- 회원 기능
  - 회원가입
  - 로그인
  - 로그아웃

- 유저 기능
  - 프로필 확인
    - 유저이름, 가입일, 내가 등록한 물품 확인
    - 내가 찜한 물품 목록 확인
    - 팔로우 와 팔로워 수 확인
  - 프로필 수정
    - 사진 수정
    - 비밀번호 변경
    
- 게시 기능
  - 물품 등록
    - 해시 태그
    - 물품 이름
    - 물품 사진
    - 물품 설명
  - 물품 수정
    - 해시 태그
    - 물품 이름
    - 물품 사진
    - 물품 설명
  - 물품 삭제
  - 물품 조회
    - 전체 목록
      - 인기도순 정렬
      - 찜수 / 조회수 노출
    - 물품 이름 검색
    - 물품 설명 검색
    - 회원 유저네임 검색
    - 해시태크 검색
  - 상세 페이지
    - 찜 하기

### 개발 기간
-24.08.19~24.08.27

### 프로젝트 개발 환경
- Python    3.12.4
- Django    4.2
- pillow    10.4.0
- windows   10
- Visual Studio Code

### ERD
![spartamarket_8_ERD](https://github.com/user-attachments/assets/54af2678-598c-4cb4-8ea4-b2f31f117850)



### 와이프레임
![와이어프레임](/냉Django_wireframe.jpg)

### 역할 분담
- 서영환
  -게시 기능
    - 물품 등록
      - 해시태그
    - 물품 수정
      -해시태그
    - 물품 조회
      - 전체 목록
        - 인기도순 정렬
        - 찜수 / 조회수 노출
      - 검색
- 이새예
  - 회원 기능
    - 회원가입
    - 로그인
    - 로그아웃
  - 유저 기능
    - 비밀번호 변경
  - 게시 기능
    - 댓글 기능
- 김나희
  - 유저기능
    - 프로필 확인
    - 프로필 수정
  - 게시 기능
    - 상세 페이지
      - 찜하기
- 김나현
  - 게시 기능
    - 물품 등록
    - 물품 수정
    - 물품 삭제
    - 물품 조회
      - 전체 목록
### API

|Index|Method|URI|Description|
|---|----|------------|------------|
|1|GET|/index/| 전체 상품 조회|
|2|GET|/index/?serch_text={text}| text에 대한 상품의 제목, 내용, 작성자, 해시태그를 조회|
|3|GET|/index/?orders={order}| order은 'date','popularity' 두개의 값만 가능하며 'date'는 날짜별, 'popularity'는 찜수로 내림차순 정렬된 값을 조회|
|4|GET|/products/read/{productidx}/|상품의 상세 페이지 이동|
|5|GET|/products/create/|상품 등록 페이지 이동|
|6|POST|/products/create/|상품을 등록|
|7|GET|/products/update/{productidx}/|상품 수정 페이지 이동|
|8|POST|/products/create/{productidx}/|상품을 수정|
|9|POST|/products/delete/{productidx}/|상품을 삭제|
|10|POST|/products/{productidx}/like/|상품을 찜하기|
|11|POST|/products/{productidx}/comments/|상품에 댓글 등록|
|12|POST|/products/{commentidx}/comments/delete/|상품에 등록된 댓글 삭제|
|13|GET|/users/profile/{username}/|회원 프로필페이지 이동|
|14|POST|/users/{useridx}/follow/|회원 팔로워 등록&취소|
|15|POST|/users/update_profile/|회원 프로필 사진 변경|
|16|POST|/users/update_profile/|회원 프로필 사진 변경|
|17|GET|/accounts/login/|로그인 페이지 이동|
|18|POST|/accounts/login/|로그인 수행|
|19|POST|/accounts/logout/|로그아웃 수행|
|20|GET|/accounts/signup/|회원가입 페이지 이동|
|21|POST|/accounts/signup/|회원등록|
|22|POST|/accounts/delete/{userid}/|회원탈퇴|
|23|GET|/accounts/update/{userid}/|회원 정보 수정 페이지 이동|
|24|POST|/accounts/update/{userid}/|회원 정보 수정|
|25|GET|/accounts/change_password/|패스워드 변경 페이지 이동|
|26|POST|/accounts/change_password/|패스워드 변경|

