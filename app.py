import os

from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def home():
    return """
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Cloud Assignments</title>
        <style>
          :root { color-scheme: dark; font-family: system-ui, sans-serif; }
          body {
            min-height: 100vh;
            margin: 0;
            display: grid;
            place-items: center;
            background: linear-gradient(145deg, #10243a, #172554 60%, #164e63);
            color: #e2e8f0;
          }
          main {
            width: min(90%, 38rem);
            padding: 2.5rem;
            border: 1px solid #ffffff30;
            border-radius: 1.25rem;
            background: #0f172acc;
            box-shadow: 0 1.5rem 4rem #02061780;
          }
          h1 { margin-top: 0; color: #67e8f9; }
          p { line-height: 1.7; }
          .status {
            display: inline-block;
            margin-top: 1rem;
            padding: .5rem .85rem;
            border-radius: 99rem;
            background: #064e3b;
            color: #a7f3d0;
          }
        </style>
      </head>
      <body>
        <main>
          <h1>Cloud Assignments</h1>
          <p>A Python web application packaged with Docker and ready to run on Kubernetes.</p>
          <span class="status">Application is running</span>
        </main>
      </body>
    </html>
    """


@app.get("/health")
def health():
    return jsonify(status="healthy", application="cloud-assignments")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
