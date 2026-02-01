# 🕰️ The 1993 Time Capsule (User-Agent Challenge)

**Category:** Web Exploitation / HTTP Headers  
**Difficulty:** Medium  
**Tech Stack:** Python (Flask), Docker

## 📝 Description
**"Legacy Access Only."**

Our intelligence team has located a legacy LNM Security Portal running on an ancient server. The system is heavily restricted and rejects all modern connections. It appears to only accept connections from a very specific, historical workstation environment from the early 90s.

**Objective:** Bypass the "Protocol Mismatch" error and retrieve the internal flag.

## 🔍 The Vulnerability
The application relies on the `User-Agent` HTTP header to identify the client.
* **Intended Behavior:** The server expects the client to be an ancient browser ("NCSA Mosaic 2.0").
* **The Flaw:** `User-Agent` is a client-side header. Hackers can change this string to anything they want, tricking the server into thinking they are using the required software.

### Vulnerable Code Snippet (`useragent.py`)
```python
REQUIRED_UA = "NCSA_Mosaic/2.0 (Windows 3.1)"

@app.route('/', methods=['POST'])
def challenge():
    user_agent = request.headers.get('User-Agent', '')
    
    # The Vulnerability: Trusting the client input blindly
    if REQUIRED_UA in user_agent:
        msg = "Handshake Successful. Flag: " + FLAG
    else:
        msg = "ERROR: Protocol Mismatch." 
```

🔓 Solution
To solve this, we must spoof our User-Agent string to match the requirement found in the hints.

Method 1: Using Curl
```curl -A "NCSA_Mosaic/2.0 (Windows 3.1)" -X POST http://localhost:5080```

Method 2: Using Burp Suite

Intercept the request to http://localhost:5080.

Send it to Repeater.

Change User-Agent: Mozilla/5.0... to User-Agent: NCSA_Mosaic/2.0 (Windows 3.1).

Send the request.

Flag: LNMHACKS{u$er_4g3nt_i$_n0t_m6_F0rt3}
