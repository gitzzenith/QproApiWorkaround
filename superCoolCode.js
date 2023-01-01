/// Join Match
async function postData(data) {
    fetch(fetchUrl, {
        mode: 'no-cors',
        method: 'POST',
        headers: {
        'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
}
function handleJoin(event) {
    document.getElementById("feedback").innerHTML = "joining... this may take a few seconds";
    sessionid = "3D94B739-F91F-4113-A131-12EDBF603A6F";
    ip = "192.168.43.";
    teamid = document.getElementById("teamid").selectedIndex;
    console.log(teamid)
    
    const data = {
        "session_id": sessionid,
        "team_idx": teamid
    };
    console.log(data)
    for(let i = 0; i < 256; i++) {
        fetchUrl = 'http://' + ip + i + ':6721/join_session';
        console.log(fetchUrl);
        postData(data);
    }
    return false;
}