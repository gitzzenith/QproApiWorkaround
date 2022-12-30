
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
    "session_id": "F4896F46-EE50-4005-A9F1-7734E4BD8861",
    "team_idx": 0
};
fetch('192.168.43.60:6721/join_session', {
    mode: 'no-cors',
    method: 'POST', // or 'PUT'
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
})