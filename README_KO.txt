신유빈 사인 레이더 - 크레딧 없는 시작용 프로젝트

구성
- index.html: 태블릿용 웹앱
- scripts/daily_search.py: 공개 Google News RSS 검색 결과 가져오기
- .github/workflows/daily-search.yml: 매일 12:00 한국시간 자동 실행 + 수동 실행
- results.json: 앱이 읽는 자동 검색 결과

중요한 제한
1. 이 자동 검색은 Google News RSS 공개 색인만 검색합니다. 번개장터/중고나라 등 모든 매물과 모든 게시물을 검색하지 않습니다.
2. 거래 사이트가 공개 RSS/API를 제공하고 자동 접근을 허용하는 경우에만 별도 연동을 추가해야 합니다. 로그인, CAPTCHA, 차단, 이용약관을 우회하지 않습니다.
3. 검색 결과는 친필 인증이 아닙니다. 판매 중 여부와 진위는 원문/증거를 확인해야 합니다.
4. 태블릿 푸시 알림은 아직 연결되지 않았습니다. 실제 푸시에는 HTTPS 호스팅, 서비스워커, 푸시 서버/VAPID 키 구성이 필요합니다.
5. 사용자가 저장한 매물은 현재 태블릿 브라우저의 localStorage에 저장됩니다. 브라우저 데이터 삭제 전에 백업하세요.

GitHub에서 무료로 매일 실행하는 방법
1. GitHub에 로그인하고 새 Public 저장소를 만듭니다.
2. 이 ZIP의 파일을 저장소 루트에 업로드합니다.
3. Actions 탭에서 워크플로가 활성화되어 있는지 확인합니다.
4. Actions > Daily autograph search > Run workflow로 첫 실행을 시험합니다.
5. Settings > Pages에서 Deploy from a branch, main, /(root)를 선택해 저장합니다.
6. 잠시 후 제공되는 GitHub Pages 주소를 삼성 인터넷에서 열어 홈 화면에 추가할 수 있습니다.

참고
- GitHub Actions 예약 실행은 지연될 수 있으며, 비활성 저장소/사용량/정책에 따라 제한될 수 있습니다.
- 공개 저장소에는 개인 정보나 비밀키를 올리지 마세요.
