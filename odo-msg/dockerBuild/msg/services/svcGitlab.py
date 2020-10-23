#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import logging
from services import svcJenkins


def invoke(body):
    """

    :param body:
    :return:
    """
    _url = svcJenkins.generate_build_with_param_url(job_name=body['project']['name'])
    _query = {
        'GIT_HTTP_URL': body['project']['git_http_url'],
        'GIT_SSH_URL': body['project']['git_ssh_url'],
        'GIT_BRANCH_NAME': body['ref'].split('/')[-1],
        'GIT_USER_NAME': body['user_username'],
    }
    logging.info('Query info: %s' % _query)
    _session = requests.session()
    _rsp = _session.post(url=_url, params=_query, json=body)
    _status_code = _rsp.status_code
    _session.close()
    return _status_code


if __name__ == '__main__':
    print('This is Gitlab service scripts')
