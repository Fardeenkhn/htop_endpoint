from flask import Flask
import os
import subprocess
from datetime import datetime

app = Flask(__name__)

@app.route("/htop")
def htop():
    name = "FARDEEN KHAN"
    username = os.getenv("USER") or os.getenv("USERNAME")
    ist_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S') + ' IST'

    # Get top command output
    top_output = subprocess.getoutput("top -n 1 -b")

    return f"""<pre>
Name: {name}
Username: {username}
Server Time (IST): {ist_time}
TOP output:
{top_output}
</pre>"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)