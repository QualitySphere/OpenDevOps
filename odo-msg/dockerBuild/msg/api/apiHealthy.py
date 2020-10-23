#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def healthy():
    """
    GET /api/healthy
    :return:
    """
    try:
        return {
            'status': 'Healthy'
        }, 200
    except Exception as e:
        raise Exception(e)


if __name__ == '__main__':
    print('This is Healthy API scripts')
