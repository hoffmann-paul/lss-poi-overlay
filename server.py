import json
from http.server import BaseHTTPRequestHandler, HTTPServer

from get_pins import server_request   # <- Dateiname und Funktionsname anpassen

PORT = 8765


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/pins":
            self.send_error(404)
            return
        try:
            pins = server_request()
            body = json.dumps(pins, ensure_ascii=False).encode("utf-8")
            status = 200
        except Exception as e:
            print("Error while collecting pins:", e)
            body = json.dumps({"error": str(e)}).encode("utf-8")
            status = 500

        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    print(f"Server runs on http://127.0.0.1:{PORT}/pins")
    HTTPServer(("127.0.0.1", PORT), Handler).serve_forever()