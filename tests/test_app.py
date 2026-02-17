import http.server
import socketserver
import threading
import time
import unittest
from pathlib import Path
from urllib.request import urlopen


class TestMultiStreamView(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        repo_root = Path(__file__).resolve().parents[1]
        handler = http.server.SimpleHTTPRequestHandler

        cls._old_cwd = Path.cwd()
        import os

        os.chdir(repo_root)

        cls.httpd = socketserver.TCPServer(("127.0.0.1", 0), handler)
        cls.port = cls.httpd.server_address[1]

        cls.server_thread = threading.Thread(target=cls.httpd.serve_forever, daemon=True)
        cls.server_thread.start()
        time.sleep(0.2)

    @classmethod
    def tearDownClass(cls):
        cls.httpd.shutdown()
        cls.httpd.server_close()
        import os

        os.chdir(cls._old_cwd)

    def test_index_page_contains_main_elements(self):
        with urlopen(f"http://127.0.0.1:{self.port}/index.html") as response:
            self.assertEqual(response.status, 200)
            content = response.read().decode("utf-8")

        self.assertIn("<h1>🎥 Multi Stream View</h1>", content)
        self.assertIn('id="form-live"', content)
        self.assertIn('id="grid"', content)
        self.assertIn('src="script.js"', content)

    def test_required_project_files_exist(self):
        repo_root = Path(__file__).resolve().parents[1]
        self.assertTrue((repo_root / "index.html").exists())
        self.assertTrue((repo_root / "styles.css").exists())
        self.assertTrue((repo_root / "script.js").exists())


if __name__ == "__main__":
    unittest.main()
