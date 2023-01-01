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
    document.getElementById("feedback").innerHTML = "joining... if you are not redirected in a few seconds, please restart Echo VR and try again";
    sessionid = "{sessionID}";
    ip = "{apiIP}";
    teamid = document.getElementById("teamid").selectedIndex;
    console.log(teamid)
    
    const data = {{
        "session_id": sessionid,
        "team_idx": teamid
    }};
    console.log(data)
    for(let i = 0; i < 256; i++) {{
        fetchUrl = 'http://' + ip + i + ':6721/join_session';
        console.log(fetchUrl);
        postData(data);
    }}
    return false;
}}'''

ipStatic = "192.168.43." # this should be the same for everyone

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
