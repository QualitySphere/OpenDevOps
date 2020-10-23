#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from services import svcGitlab
import connexion


def invoke(body):
    """
    POST /gitlab/invoke
    :param body:
    :return:
    """
    try:
        svcGitlab.invoke(body)
        return {
            'title': 'Invoke Succeed'
        }, 200
    except Exception as e:
        raise Exception(e)


if __name__ == '__main__':
    print('This is Gitlab API scripts')
