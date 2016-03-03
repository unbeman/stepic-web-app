def app(environ, start_response):
	line = environ["QUERY_STRING"]
	body = "\n".join(line.split("&"))
	status = "200 OK"
	headers = [
		("Content-Type", "text/plain"),
		("Content-Length", str(len(body)))
	]
	start_response(status, headers)
	return iter([body])
