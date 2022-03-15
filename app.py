import os

from url_shortener import app

if __name__ == "__main__":
    app.run(os.environ.get("PORT", 3000))
