import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

from get_pins import server_request

PORT = 8765


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):

        parsed_url = urlparse(self.path)

        if parsed_url.path != "/pins":
            self.send_error(404)
            return

        params = parse_qs(parsed_url.query)

        city = params.get("city", ["Stuttgart"])[0]

        try:
            pins = server_request(city)

            body = json.dumps(
                pins,
                ensure_ascii=False
            ).encode("utf-8")

            status = 200

        except Exception as e:
            print("Error while collecting pins:", e)

            body = json.dumps({
                "error": str(e)
            }).encode("utf-8")

            status = 500

        self.send_response(status)
        self.send_header(
            "Content-Type",
            "application/json; charset=utf-8"
        )
        self.send_header(
            "Access-Control-Allow-Origin",
            "*"
        )
        self.end_headers()

        self.wfile.write(body)


if __name__ == "__main__":
    print(f"Server runs on http://127.0.0.1:{PORT}/pins")
    HTTPServer(("127.0.0.1", PORT), Handler).serve_forever()