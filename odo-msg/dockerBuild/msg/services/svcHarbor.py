#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import logging
from services import svcJenkins


def invoke(body):
    _url = svcJenkins.generate_build_with_param_url(job_name=body['event_data']['repository']['namespace'])
    _query = {
        'DOCKER_IMG_NS': body['event_data']['repository']['namespace'],
        'DOCKER_IMG_NAME': body['event_data']['repository']['name'],
        'DOCKER_IMG_TAG': body['event_data']['resources'][0]['tag'],
    }
    logging.info('Query info: %s' % _query)
    _session = requests.session()
    _rsp = _session.post(url=_url, params=_query, json=body)
    _status_code = _rsp.status_code
    _session.close()
    return _status_code


if __name__ == '__main__':
    print('This is Harbor service scripts')
