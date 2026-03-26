import subprocess
import sys
import time
import urllib.request


def wait_for_server(url, timeout=10):
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        try:
            urllib.request.urlopen(url)
            return True
        except Exception:
            time.sleep(0.2)
    return False


def check(description, url):
    print(f"  {description}...", end=" ", flush=True)
    with urllib.request.urlopen(url) as resp:
        data = resp.read()
        assert resp.status == 200
    print(f"OK ({len(data)} bytes)")
    return data.decode(errors="replace")


def test_e2e():
    print("Starting server...", flush=True)
    proc = subprocess.Popen(
        [sys.executable, "example.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    try:
        base = "http://127.0.0.1:5000"
        assert wait_for_server(f"{base}/api/docs/"), "Server did not start"
        print("Server is up\n")

        print("Checking index page:")
        body = check("GET /api/docs/", f"{base}/api/docs/")
        assert "swagger-ui" in body, "Missing swagger-ui in index"
        assert "Test application" in body, "Missing app name in index"
        print()

        print("Checking static assets:")
        check("GET /api/docs/swagger-ui-bundle.js", f"{base}/api/docs/swagger-ui-bundle.js")
        check("GET /api/docs/swagger-ui.css", f"{base}/api/docs/swagger-ui.css")
        check("GET /api/docs/favicon-32x32.png", f"{base}/api/docs/favicon-32x32.png")
        print()

    finally:
        print("Stopping server...")
        proc.terminate()
        proc.wait(timeout=5)


if __name__ == "__main__":
    test_e2e()
    print("OK")
