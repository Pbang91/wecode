git init - git을 초기화하는 명렁어. 현재 directory에 git을 관리하겠다는 신호이다.

git branch -M manin - git의 master(main) 브랜치의 이름을 main으로 리네임하겠다는 명령어이다.

git remote origin 'remote repository 주소' - local repository와 remote repository를 연동하겠다는 명렁어이다.

git status - 현재 directory에서 수정,삭제,생성된 파일(혹은 폴더)들의 상태를 알려준다. git commit을 진행하기 전 상태로 알려준다.

git add . - git이 설정된 directory의 모든 파일(폴더 포함) 중 변경사항이 있는 모든 것들을 Staging Area 로 넘겨주는 명령어이다.

git commit -m "message" - 실제 버전이 저장되는 repository로 특정 메세지를 지니고 보내주는 명렁어이다. 이때부터 버전관리가 가능해진다.

git push origin 'remote branch name' - 연동한 원격 저장소로 깃 커민된 내용을 전달하겠다는 명령어이다. 
