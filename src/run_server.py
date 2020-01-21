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
application.run(host='127.0.0.1', port=2000, debug=True)