# run with:    gunicorn 0_myhello:app

def app(environ, start_response):
    data = b"Hello, World!"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", f"{len(data)}"),
    ])
    return [data]
