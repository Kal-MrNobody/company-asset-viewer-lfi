from flask import Flask, request, make_response
import os

app = Flask(__name__)

@app.route('/')
def index():
    filename = request.args.get('file')

    # === The Vulnerable File Loader ===
    if filename and filename.startswith('static/'):
        try:
            if os.path.exists(filename):
                # We use 'rb' (read binary) so images load correctly
                with open(filename, 'rb') as f:
                    content = f.read()
                    response = make_response(content)
                    return response
        except Exception as e:
            return str(e), 500

    # === The Front End HTML Page ===
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Secure Asset Viewer</title>
        <style>
            body { font-family: sans-serif; background: #f4f4f9; display: flex; justify-content: center; align-items: center; height: 100vh; }
            .card { background: white; padding: 40px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); text-align: center; }
            img { max-width: 300px; border-radius: 8px; margin: 20px 0; border: 1px solid #ddd; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Company Asset Viewer</h1>
            <p>Loading secure resource...</p>
            <img src="/?file=static/icon.png" alt="Secure Icon">
            <p style="color: #888; font-size: 0.8em;">Debug: Loaded via LFI</p>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
