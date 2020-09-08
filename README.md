# OpenDevOps

#### Tool Chain

Service|Port|Container Port|Volume|Container Volume
----|----|----|----|----
OpenLDAP|18389|389||
PHPLdapAdmin|18880|80||
Self Service Password|18080|80||
MySQL|18306|3306|
Jira|8080|8080||
Confluence|8090<br>8091|8090<br>8091||
GitLab|12080<br>12443<br>222|80<br>443<br>222||
Jenkins|15080<br>50000|8080<br>50000||
SonarQube|9000|9000||
Harbor||||
Rancher|17443|443||
JumpServer|17080<br>2222|80<br>2222||
Portal|80<br>443|80<br>443||

#### ODO Dockerfiles

- [Self Service Password](https://github.com/seoktaehyeon/docker-self-service-password/blob/1.3/Dockerfile)
- [Jira Software](https://github.com/seoktaehyeon/docker-jira-software/blob/8.11/Dockerfile)
- [Confluence Server](https://github.com/seoktaehyeon/docker-confluence-server/blob/7.5/Dockerfile)
