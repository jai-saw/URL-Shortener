import os

from url_shortener import app

if __name__ == "__main__":
    port = os.environ.get("PORT", 3000)
    host = os.environ.get("HOST", "0.0.0.0")
    app.run(port, host)
