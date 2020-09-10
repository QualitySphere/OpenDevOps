# OpenDevOps
###### This is ONLY for DevOps learning and practice. Please contact the software vendor to get the product license if you are a company.

#### Quick Start

```bash
# 1. Git Clone
git clone https://github.com/QualitySphere/OpenDevOps.git
# 2. Change dir to ODO home
cd OpenDevOps
# 3. Start ODO services
./odoctl start ldap
./odoctl start pg
./odoctl start jira
./odoctl start conf
...
```

#### Tool Chain

Service|Port|Container Port|Volume|Container Volume
----|----|----|----|----
OpenLDAP|18389|389|odo-ldap/db<br>odo-ldap/config|/var/lig/ldap<br>/etc/ldap
PHPLdapAdmin|18880|80|-|-
Self Service Password|18080|80|odo-ldap/ssp/config.inc.php|/var/www/html/conf/config.inc.php
MySQL|18306|3306|odo-mysql/mysql<br>odo-mysql/docker.cnf|/var/lib/mysql<br>/etc/mysql/conf.d/docker.cnf
Jira|8080|8080|odo-jira|/var/atlassian/application-data/jira
Confluence|8090<br>8091|8090<br>8091|odo-conf|/var/atlassian/application-data/confluence
GitLab|12080<br>12443<br>222|80<br>443<br>222|odo-gitlab/data<br>odo-gitlab/config|/var/opt/gitlab<br>/etc/gitlab
Jenkins|15080<br>50000|8080<br>50000|odo-jenkins/jenkins_home<br>/var/run/docker.sock|/var/jenkins_home<br>/var/run/docker.sock
SonarQube|9000|9000|odo-sonar/data<br>odo-sonar/logs<br>odo-sonar/extensions<br>odo-sonar/sonar.properties|/opt/sonarqube/data<br>/opt/sonarqube/logs<br>/opt/sonarqube/extensions<br>/opt/sonarqube/conf/sonar.properties
Harbor||||
Rancher|17443|443|odo-rancher|/var/lib/rancher
JumpServer|17080<br>2222|80<br>2222|odo-jms/data<br>odo-jms/mysql|/opt/jumpserver/data<br>/var/lib/mysql
Portal|80<br>443|80<br>443||

#### odoctl tool

- commands
```bash
./odoctl <COMMAND>:
    start     - Up container(s) to start service(s)
    stop      - Stop container(s) to stop service(s)
    down      - Down all services
    restart   - Restart container(s) to restart service(s)
    list      - List container(s)
    license   - Generate JIRA/Confluence/Plugin license
    cleanup   - Cleanup all containers and dirs
```

- service
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
```

- list containers
```bash
./odoctl list
```

- generate license
```bash
./odoctl license <PRODUCT>:
    jira          - Generate JIRA software license
    jira_plugin   - Generate JIRA plugin license
    conf          - Generate Confluence server license
    conf_plugin   - Generate Confluence plugin license

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


#### ODO Dockerfiles

- [Self Service Password](https://github.com/seoktaehyeon/docker-self-service-password/blob/1.3/Dockerfile)
- [Jira Software](https://github.com/seoktaehyeon/docker-jira-software/blob/8.11/Dockerfile)
- [Confluence Server](https://github.com/seoktaehyeon/docker-confluence-server/blob/7.5/Dockerfile)

