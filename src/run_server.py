# -*- coding: utf-8 -*-
"""
    run_server
    ~~~~~~~~~~~~~~~~~~~~~~
    Run Flask server locally.

    :copyright: (c)2020 by rico0821
"""
from fridge import create_app


application = create_app()

print('Starting server...')
local = '127.0.0.1'
external = '172.30.1.11'
application.run(host=local, port=80, debug=True)