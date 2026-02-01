FROM python:3.9-slim

WORKDIR /app

# 1. Install dependencies
RUN pip install flask

# 2. Setup the "ctf" user (High ID to avoid conflicts)
RUN useradd -u 1000 -m ctf

# 3. Create the flag (Owned by root, Readable by everyone, Writable by NO ONE)
RUN echo "LNMHACKS{Y0U _Kn0w_C0mman6_Inj3cti0n_Y0u_6r3_5mart}" > /flag.txt && \
    chown root:root /flag.txt && \
    chmod 444 /flag.txt

# 4. Copy Application Files
COPY server.py .
COPY static ./static

# 5. LOCK DOWN PERMISSIONS
# Root owns the directory and files.
# 'ctf' user gets Read/Execute access only.
RUN chown -R root:root /app && \
    chmod -R 555 /app

# 6. Drop to low-privilege user
USER ctf

# 7. Run
CMD ["python", "server.py"]
