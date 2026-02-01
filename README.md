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
