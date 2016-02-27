from cgi import parse_qs, escape

def wsgi_app(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type','text/plain')]
    line = (environ['QUERY_STRING'])
    list = line.split('&')
    for word in list:
        word+='\n'
    start_response(status, headers)
    return list
