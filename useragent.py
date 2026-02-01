from flask import Flask, request, render_template_string

app = Flask(__name__)

# Configuration
# This is the old-school User-Agent from 1993
REQUIRED_UA = "NCSA_Mosaic/2.0 (Windows 3.1)"
FLAG = "LNMHACKS{u$er_4g3nt_i$_n0t_m6_F0rt3}"

# Minimalist/Luxury Dark UI Template
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LNM Heritage Portal</title>
    <style>
        body { 
            background: #0a0a0a; 
            color: #d4d4d4; 
            font-family: 'Inter', 'Segoe UI', sans-serif; 
            display: flex; 
            justify-content: center; 
            align-items: center; 
            height: 100vh; 
            margin: 0; 
        }
        .container { 
            border: 1px solid #333; 
            padding: 3rem; 
            background: #111;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            text-align: center; 
            max-width: 450px;
            border-radius: 4px;
        }
        h2 { 
            letter-spacing: 4px; 
            font-weight: 300; 
            color: #fff;
            margin-bottom: 20px;
        }
        p { font-size: 0.9em; color: #888; line-height: 1.6; }
        .ua-hint { color: #555; font-style: italic; margin-top: 10px; }
        button { 
            background: transparent; 
            border: 1px solid #fff; 
            color: #fff; 
            padding: 12px 30px; 
            cursor: pointer; 
            margin-top: 30px; 
            transition: all 0.4s ease;
            text-transform: uppercase;
            font-size: 0.8em;
            letter-spacing: 2px;
        }
        button:hover { 
            background: #fff; 
            color: #000; 
        }
        .error { color: #ff5555; margin-top: 20px; font-family: monospace; }
        .success { 
            color: #00ff41; 
            font-weight: bold; 
            border: 1px solid #00ff41; 
            padding: 15px; 
            margin-top: 20px;
            background: rgba(0, 255, 65, 0.05);
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>LEGACY ACCESS</h2>
        <p>System detected. This terminal only accepts requests from the <strong>NCSA Mosaic 2.0</strong> workstation.</p>
        
        {% if msg %}
            <div class="{{ 'success' if 'LNMHACKS' in msg else 'error' }}">
                {{ msg }}
            </div>
        {% endif %}

        <form method="POST">
            <button type="submit">Initialize Handshake</button>
        </form>
        <div class="ua-hint">Verification Protocol: 1993.01</div>
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def challenge():
    msg = None
    if request.method == 'POST':
        user_agent = request.headers.get('User-Agent', '')
        # Checking for the exact old-school string
        if REQUIRED_UA in user_agent:
            msg = "Handshake Successful. Flag: {}".format(FLAG)
        else:
            msg = "ERROR: Protocol Mismatch. Client identified as: {}".format(user_agent[:40])
            
    return render_template_string(HTML_TEMPLATE, msg=msg)

if __name__ == '__main__':
    # Running on port 5080 for your Kali setup
    app.run(host='0.0.0.0', port=5080)
