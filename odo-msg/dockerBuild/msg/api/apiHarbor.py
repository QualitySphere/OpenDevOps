#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from services import svcHarbor
import connexion


def invoke(body):
    """
    POST /harbor/invoke
    :param body:
    :return:
    """
    try:
        svcHarbor.invoke(body)
        return {
            'title': 'Invoke Succeed'
        }, 200
    except Exception as e:
        raise Exception(e)


if __name__ == '__main__':
    print('This is Harbor API scripts')
