
/*/ Hide UI
const data = {
    "enabled": false
};
fetch('http://127.0.0.1:6721/ui_visibility', {
    mode: 'no-cors',
    method: 'POST', // or 'PUT'
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
})*/

// Get unique fragment of IP
ipFragment = parseInt(prompt("Enter unique part of ip"));
document.getElementById("errOut").innerHTML = ipFragment;

postData("B75BB299-36B3-4EEC-B0F4-4E5827032118", ipFragment);
// Join Match
async function postData(sessionid, ipFrag) {
    const data = {
        "session_id": sessionid,
        "team-idx": 2
    };

    //fetchUrl = 'http://127.0.0.' + ipFrag + ':6721/join_session'; // desktop
    fetchUrl = 'http://192.168.43.' + ipFrag + ':6721/join_session'; // quest

    fetch(fetchUrl, {
        mode: 'no-cors',
        method: 'POST', // or 'PUT'
        headers: {
        'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
}

