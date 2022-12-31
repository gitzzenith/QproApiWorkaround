htmlContent = '''<!DOCTYPE html>
<html lang="en">
    <body>
        <h1>Welcome to ghetto Spark</h1>
        <form onsubmit="return handleJoin(event)">
            <select name="teamid" id="teamid">
                <option value=0>Orange</option>
                <option value=1>Blue</option>
                <option value=2>Spec</option>
            </select>
            <input type="submit" value="Join">
        </form>
        <h2 id="feedback"></h2>
        <script src="superCoolCode.js"></script>
    </body>
</html>'''

jsContent = '''/// Join Match
async function postData(data) {{
    fetch(fetchUrl, {{
        mode: 'no-cors',
        method: 'POST',
        headers: {{
        'Content-Type': 'application/json',
        }},
        body: JSON.stringify(data),
    }})
}}
function handleJoin(event) {{
    document.getElementById("feedback").innerHTML = "joining... this may take a few seconds";
    sessionid = "{sessionID}";
    ip = "{apiIP}";
    teamid = document.getElementById("teamid").selectedIndex;
    console.log(teamid)
    
    const data = {{
        "session_id": sessionid,
        "team-idx": teamid
    }};
    for(let i = 0; i < 256; i++) {{
        fetchUrl = 'http://' + ip + i + ':6721/join_session';
        console.log(fetchUrl);
        postData(data);
    }}
    return false;
}}'''

try:
    ipFile = open('staticIP.txt', 'r')
except FileNotFoundError:
    print("Run FIRST_TIME_SETUP.bat first")
    input("press enter to exit")
    exit()
ipStatic = ipFile.read()
ipFile.close()

# Ask for sessionID
sessionID = input("Paste sessionID or Spark Link here:")

sessionID = sessionID.strip().replace(">","").split("/")[-1] # extract sessionid from spark link

# Create dynamic webpage
import http.server
import socket
import socketserver

PORT = 6722
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
SERVERIP = local_ip
fullAddress = "{}:{}".format(SERVERIP, PORT)

outhtml = open('index.html', 'w')
outhtml.write(htmlContent.format(serverIP = fullAddress))
outhtml.close()

outjs = open('superCoolCode.js', 'w')
outjs.write(jsContent.format(sessionID = sessionID, apiIP = ipStatic))
outjs.close()

# Start web server
handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("Joining session:", sessionID)
    print("Server started at localhost:{}".format(PORT))
    print("\n\nVisit {} on your quest's browser while in game to join".format(fullAddress))
    print("Feel free to close this window when you've joined the match")
    httpd.serve_forever()
