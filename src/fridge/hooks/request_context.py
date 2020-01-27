"""
    fridge.hooks.request_context
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Module for defining request context actions.

    :copyright: (c)2020 by rico0821

"""
def after_request(response):
    try:
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame_Options"] = "deny"
        response.headers.add(
            "Cache-Control",
            "no-store, no-cache, must-revalidate, post-check=0, pre-check=0"
        )
    finally:
        return response
