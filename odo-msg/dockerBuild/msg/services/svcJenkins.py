#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import requests
from urllib.parse import urlparse
import os
import logging


def list_jobs():
    """
    List all Jenkins jobs
    job type: WorkflowJob, WorkflowMultiBranchProject, FreeStyleProject
    :return:
    """
    _auth = '%s:%s' % (os.environ.get('JENKINS_USER'), os.environ.get('JENKINS_TOKEN'))
    _jurl = os.environ.get('JENKINS_URL')
    _url = '/'.join([
        '%s://%s@%s' % (urlparse(_jurl).scheme, _auth, urlparse(_jurl).netloc),
        'api',
        'json'
    ])
    logging.info('List jobs from: %s' % _url)
    _session = requests.session()
    _rsp = _session.get(url=_url)
    _jobs = _rsp.json().get('jobs')
    _session.close()
    _job_list = list()
    for _job in _jobs:
        _job['type'] = _job['_class'].split('.')[-1]
        _job_list.append(_job['name'])
    logging.info('Jobs: %s' % _job_list)
    return _jobs


def generate_build_with_param_url(job_name: str):
    _auth = '%s:%s' % (os.environ.get('JENKINS_USER'), os.environ.get('JENKINS_TOKEN'))
    _jurl = os.environ.get('JENKINS_URL')
    _url_prefix = '%s://%s@%s/job' % (urlparse(_jurl).scheme, _auth, urlparse(_jurl).netloc)
    _url = ''
    logging.info('Search job [%s]' % job_name)
    for _job in list_jobs():
        if _job['name'].lower() == job_name.lower():
            logging.info('Job details: %s' % _job)
            if _job['type'] == 'WorkflowMultiBranchProject':
                _url = '/'.join([
                    _url_prefix,
                    _job['name'],
                    'job',
                    'master',
                    'buildWithParameters'
                ])
            else:
                _url = '/'.join([
                    _url_prefix,
                    job_name,
                    'buildWithParameters'
                ])
            break
    logging.info('Generate build URL: %s' % _url)
    return _url


if __name__ == '__main__':
    print('This is Jenkins functions scripts')
