# socar-inc/airflow
쏘카 데이터비즈니스본부에서 airflow image 를 빌드하기 위해 사용하는 레포지토리입니다.

레포 관리자 : @socar-grab, @socar-dini

## 1. 레포지토리의 목적
* apache/airflow repository 를 fork 하여 쏘카 데이터비즈니스본부의 환경에 맞게 수정합니다.
* CI/CD 파이프라인을 통해 도커 이미지를 자동으로 빌드하고 GCR에 푸시합니다.
* 해당 이미지를 쏘카 데이터비즈니스본부의 airflow helm chart 에 이용합니다.


## 2. CI/CD pipeline
이 레포지토리는 CI/CD 툴로 `buddy`를 이용하고 있습니다.
### `develop 브랜치에 push` 하면
  * 해당 브랜치의 Dockerfile 을 바탕으로 도커 이미지를 build 하고,
  * socar-data-dev:airflow GCR 에 해당 도커 이미지를 push 합니다.

### `tag를 붙여서 push` 하면
  * 해당 브랜치의 Dockefile 을 바탕으로 도커 이미지를 build 하고,
  * socar-data:airflow GCR 에 해당 도커 이미지를 push 합니다.
    * tag 이름은 `airflow/<version_number>`형식이어야 합니다. (ex. `airflow/2.2.4`)
    * 되도록 `main branch` 에서 tag push 하도록 합니다.


## 3. 업데이트 시 프로세스
### 원본 레포지토리 (`apache/airflow`) 의 main branch 업데이트 사항을 가져올 때
* origin main branch 에 upstream main branch 변경 사항을 가져옵니다.
  ```shell
  git remote add upstream git@github.com:apache/airflow.git
  git fetch upstream
  git merge upstream/main
  git push origin main
  ```

* origin develop branch 에 origin main branch 변경 사항을 가져옵니다.
  ```shell
  git fetch && git rebase origin/main
  ```

### 우리 팀에서 사용하는 버전을 업데이트 할 때
* image 의 release number 를 변경합니다. (ex `airflow:2.2.4.0` -> `airflow:2.2.4.1`)
