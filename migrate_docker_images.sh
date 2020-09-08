#!/bin/bash
#set -ex
registry="registry.cn-hangzhou.aliyuncs.com/bxwill/"
repo="bxwill"

source_img="dinkel/openldap:latest"
target_img="${registry}/${repo}/openldap:latest"
docker pull ${source_img} && docker tag ${source_img} ${target_img} && docker push ${target_img}

source_img="dinkel/phpldapadmin:latest"
target_img="${registry}/${repo}/phpldapadmin:latest"
docker pull ${source_img} && docker tag ${source_img} ${target_img} && docker push ${target_img}

#docker push ${registry}${repo}/ssp:1.3

source_img="mysql:5.7"
target_img="${registry}/${repo}/mysql:5.7"
docker pull ${source_img} && docker tag ${source_img} ${target_img} && docker push ${target_img}

#docker push ${registry}${repo}/jira-software:8.11
#docker push ${registry}${repo}/confluence-server:7.5

source_img="gitlab/gitlab-ce:13.3.5-ce.0"
target_img="${registry}/${repo}/gitlab-ce:13.3.5"
docker pull ${source_img} && docker tag ${source_img} ${target_img} && docker push ${target_img}

source_img="jenkinsci/blueocean"
target_img="${registry}/${repo}/jenkins:blueocean"
docker pull ${source_img} && docker tag ${source_img} ${target_img} && docker push ${target_img}

source_img="sonarqube:7.9-community"
target_img="${registry}/${repo}/sonar:7.9"
docker pull ${source_img} && docker tag ${source_img} ${target_img} && docker push ${target_img}

source_img="rancher:v2.4.8"
target_img="${registry}/${repo}/rancher:2.4.8"
docker pull ${source_img} && docker tag ${source_img} ${target_img} && docker push ${target_img}

source_img="jumpserver/jms_all:2.1.2"
target_img="${registry}/${repo}/jms_all:2.1.2"
docker pull ${source_img} && docker tag ${source_img} ${target_img} && docker push ${target_img}
