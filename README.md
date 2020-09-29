# OpenDevOps
###### This is ONLY for DevOps learning and practice. Please contact the software vendor to get the product license if you are a company.

> **Table of Contents**
> - Framework
> - Quick Start
>   - Resource
>   - Deployment
>   - Configuration
>     - OpenLDAP
>     - Self Service Password
>     - Jira Software
>     - Confluence
>     - GitLab
>     - SonarQube
>     - Jenkins
>     - Harbor
>     - Rancher
>     - JumpServer
>   - Manual
> - Tool Chain
> - odoctl
> - ODO Dockerfiles

## Framework

![Open DevOps Services](doc/images/odo-framework-01.png)
![ODO Framework](doc/images/odo-framework-02.png)

## Quick Start

#### Resource

Type | CPU | Memory 
----|----|----
Minimum | 4 core | 8 G
Recommended | 8 core | 16 G
Optimum | 16 core | 32 G

#### Deployment

1. Clone project <br>`git clone https://github.com/QualitySphere/OpenDevOps.git`
2. Change dir to ODO home <br>`cd OpenDevOps`
3. Enable and update `odo-portal` environment part in `docker-compose.yaml` <br>Change localhost to your server IP or domain <br>![ODO Portal YAML](doc/images/odo-portal-01.png)
4. Start ODO services <br>`./odoctl start all`
5. Access ODO-Portal `http://ODO-HOST` <br>![ODO Portal](doc/images/odo-portal-02.png)

#### Configuration

- **OpenLDAP**
  - Auto-init
- **Self** **Service** **Password**
  - Access Self Service Password `http://ODO-HOST:18080`
  - Try to update default account `odo`'s password to validate SSP
  - Try to update `odo`'s password via E-mail. <br>if you find there is no hostname in the reset password link, you can update `$reset_url` in `odo-ldap/ssp/config.inc.php`
- **Jira** **Software**
  - Auto-init
- **Confluence**
  - Auto-init
- **GitLab**
  - Auto-init
- **SonarQube**
  - Auto-init
- **Jenkins**
  - Access Jenkins `http://ODO-HOST:15080` to unlock it
  - You can get `initialAdminPassword` via otoctl tool `./odoctl license jenkins` in ODO-HOST <br>![](doc/images/odo-jenkins-01.png)
  - ![](doc/images/odo-jenkins-02.png) 
  - Add/Remove the plugins to config Jenkins <br>![](doc/images/odo-jenkins-03.png) 
    - check `GitLab` `Publish Over SSH` `SSH`
    - uncheck `Ant` `Gradle`
  - Waiting for installation complete <br>![](doc/images/odo-jenkins-04.png) 
  - Use default admin account to continue <br>![](doc/images/odo-jenkins-05.png) 
  - Try to config LDAP later <br>![](doc/images/odo-jenkins-06.png) 
- **Harbor**
  - To Be Written
- **Rancher**
  - To Be Written
- **JumpServer**
  - To Be Written

#### Manual

- [Jira Software](https://docs.atlassian.com/jira/jsw-docs-0811/)
- [Confluence](https://docs.atlassian.com/confluence/docs-75/)
- [GitLab](https://docs.gitlab.com/ee/README.html)
- [SonarQube](https://docs.sonarqube.org/latest/)
- [Jenkins](https://www.jenkins.io/zh/doc/book/blueocean/creating-pipelines/)
- [Harbor](https://goharbor.io/docs/2.0.0/working-with-projects/)
- [Rancher](https://rancher.com/docs/rancher/v2.x/en/)
- [JumpServer](https://docs.jumpserver.org/zh/master/admin-guide/quick_start/)

## Tool Chain

Service|Port|Container Port|Volume|Container Volume
----|----|----|----|----
OpenLDAP|18389|389|odo-ldap/db<br>odo-ldap/config|/var/lig/ldap<br>/etc/ldap
PHPLdapAdmin|18880|80|-|-
Self Service Password|18080|80|odo-ldap/ssp/config.inc.php|/var/www/html/conf/config.inc.php
PostgresQL|18432|5432|odo-pg|/var/lib/postgresql/data
Jira|8080|8080|odo-jira|/var/atlassian/application-data/jira
Confluence|8090<br>8091|8090<br>8091|odo-conf|/var/atlassian/application-data/confluence
GitLab|12080<br>12443<br>222|80<br>443<br>222|odo-gitlab/data<br>odo-gitlab/config|/var/opt/gitlab<br>/etc/gitlab
Jenkins|15080<br>50000|8080<br>50000|odo-jenkins/jenkins_home<br>/var/run/docker.sock|/var/jenkins_home<br>/var/run/docker.sock
SonarQube|9000|9000|odo-sonar/data<br>odo-sonar/logs<br>odo-sonar/extensions<br>odo-sonar/sonar.properties|/opt/sonarqube/data<br>/opt/sonarqube/logs<br>/opt/sonarqube/extensions<br>/opt/sonarqube/conf/sonar.properties
Harbor|16080|80|odo-harbor|
Rancher|17443|443|odo-rancher|/var/lib/rancher
JumpServer|17080<br>2222|80<br>2222|odo-jms/data<br>odo-jms/mysql|/opt/jumpserver/data<br>/var/lib/mysql
Portal|80<br>443|80<br>443||

## odoctl 

- commands
```bash
./odoctl <COMMAND>:
    start           - Up container(s) to start service(s) and init them
    start_no_init   - Up container(s) to start service(s)
    stop            - Stop container(s) to stop service(s)
    down            - Down all services
    restart         - Restart container(s) to restart service(s)
    list            - List container(s)
    license         - Generate JIRA/Confluence/Plugin license
    cleanup         - Cleanup all containers and dirs
```

- services
```bash
./odoctl start/stop/restart <SERVICE>:
    all       - All Services
    ldap      - OpenLDAP, PhpLDAPAdmin and Self Service Password
    pg        - PostgresQL
    jira      - Jira Software
    conf      - Confluence
    sonar     - SonarQube Community Edition
    jenkins   - Jenkins
    gitlab    - GitLab Community Edition
    rancher   - Rancher
    jms       - JumpServer
    portal    - DevOps Portal
```

- list containers
```bash
./odoctl list
```

- generate license for JIRA/Confluence
```bash
./odoctl license <PRODUCT>:
    jira          - Generate JIRA software license
    jira_plugin   - Generate JIRA plugin license
    conf          - Generate Confluence server license
    conf_plugin   - Generate Confluence plugin license
    jenkins       - Get Jenkins initialAdminPassword

./odoctl license jira_plugin/conf/conf_plugin <PRODUCT_ID>:
    PRODUCT_ID is REQUIRED
      +-------------+------------+------------------------------------+
      | PRODUCT     | PRODUCT_ID | WHERE                              |
      +-------------+------------+------------------------------------+
      | jira_plugin | plugin ID  | JIRA application detail page       |
      +-------------+------------+------------------------------------+
      | conf        | server ID  | Confluence installation page       |
      +-------------+------------+------------------------------------+
      | conf_plugin | plugin ID  | Confluence application detail page |
      +-------------+------------+------------------------------------+
```

- cleanup ODO services and dirs 

```bash
./odoctl cleanup
```

## ODO Dockerfiles

- [Self Service Password](https://github.com/seoktaehyeon/docker-self-service-password/blob/1.3/Dockerfile)
- [Jira Software](https://github.com/seoktaehyeon/docker-jira-software/blob/8.11/Dockerfile)
- [Confluence Server](https://github.com/seoktaehyeon/docker-confluence-server/blob/7.5/Dockerfile)
- [ODO Portal](odo-portal/dockerBuild/Dockerfile)
- [ODO Harbor Installer](odo-harbor/dockerBuild/Dockerfile)

