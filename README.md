# 🚩 Company Asset Viewer (LFI Challenge)

**Category:** Web Exploitation / Local File Inclusion (LFI)
**Difficulty:** Beginner
**Tech Stack:** Python (Flask), Docker

## 📝 Description
Welcome to the "Company Asset Viewer." This internal tool allows employees to view approved company assets (like icons and logos) dynamically. However, the developer might have been a little too trusting with how file paths are handled.

**Objective:** Read the content of \`/flag.txt\` stored on the server's root directory.

## 🔍 The Vulnerability
The application uses a \`file\` parameter to load images.
* **Intended Usage:** \`?file=static/icon.png\`
* **The Flaw:** The code checks if the path *starts with* \`static/\`, but it does not sanitize directory traversal sequences.

## 🔓 Solution
To solve this, use **Directory Traversal** (\`../\`) to move up from the \`static\` folder.

**Exploit Payload:**
\`http://localhost:5001/?file=static/../../../../flag.txt\`

## The Developer's Mistake
Do you see the flaw? The developer used startswith('static/')

This prevents me from simply asking for /flag.txt or /etc/passwd. However, it does not prevent me from asking for static/../../flag.txt.

As long as my request starts with the correct word, the operating system will happily process the ../ (dot-dot-slash) characters to walk up the directory tree.

## Step 3: The Exploit
When you launch the container (docker-compose up), you are greeted with a "Company Asset Viewer" page.

Recon: You notice the image loads via ?file=static/icon.png.

**Test**: You try changing it to ?file=flag.txt.

**Result:** 404 Error (Because it must start with "static/").

**Attack:** You try a traversal attack. You need to go "up" several directories to reach the root.

**Payload:** ?file=static/../../../../flag.txt

Boom. The server reads the file and displays the flag right on the webpage!

## Conclusion
Building this challenge taught me that input validation is tricky. Simply checking the beginning of a string isn't enough. Secure code must validate the absolute path to ensure it never leaves the intended directory.
