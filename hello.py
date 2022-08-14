

def app(environ, start_response):
    
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    q_str = environ["QUERY_STRING"]
    args = q_str.split('&')
    
    body = ''
    
    for str in args:
        body + str + '\n'
       
    start_response(status, headers)
    return [ body ]