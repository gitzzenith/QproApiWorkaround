
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

// Join Match
const data = {
    "session_id": "B75BB299-36B3-4EEC-B0F4-4E5827032118",
    "team_idx": 0
};
fetch('192.168.43.200:6721/join_session', {
    mode: 'no-cors',
    method: 'POST', // or 'PUT'
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
})
