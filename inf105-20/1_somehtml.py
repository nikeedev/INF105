# run with: gunicorn 1_somehtml:app


from zoneinfo import ZoneInfo
from datetime import datetime as dt


MAIN_TEMPL = """\
<html>
<head>
  <meta charset="utf-8">
  <title>WSGI test</title>
</head>
<body>
  <h1>The time is</h1>
  {times}
  <h1>I can count in Python, look!</h1>
  {content}
  <h1>Other stuff</h1>
  {other}
</body>
</html>
"""


def count():
    lines = []
    for i in range(1,11):
        lines.append(f"<p>Number {i}</p>")
    return '\n'.join(lines)


TZs = [
  'Pacific/Honolulu',
  'America/Los_Angeles',
  'America/New_York', 
  'Europe/London', 
  'Europe/Oslo', 
  'Asia/Tehran', 
  'Asia/Shanghai', 
  'Australia/Sydney',
]


def get_time():
    now = dt.now(ZoneInfo("UTC"))
    lines = []
    for zone in TZs:
        city = zone.split('/')[1]
        tz = ZoneInfo(zone)
        localtime = now.astimezone(tz).strftime("%Y-%m-%d %H:%M:%S")
        lines.append(f"<p>{localtime} in {city}</p>")
    return '\n'.join(lines)


def parse_environ(env):
    return f"""\
    <pre>
    {env["QUERY_STRING"] = }
    {env["PATH_INFO"] = }
    </pre>
    """
        


def app(environ, start_response):
    other = parse_environ(environ)
    data = MAIN_TEMPL.format(content=count(), times=get_time(), other=other).encode('utf-8')
    start_response("200 OK", [
        ("Content-Type", "text/html"),
        ("Content-Length", f"{len(data)}"),
    ])
    return [data]
