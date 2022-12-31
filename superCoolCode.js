// Join Match
async function postData(sessionid, ipFrag) {
    const data = {
        "session_id": sessionid,
        "team-idx": 2
    };

    //fetchUrl = 'http://127.0.0.' + ipFrag + ':6721/join_session'; // desktop
    fetchUrl = '192.168.43.' + ipFrag + ':6721/join_session'; // quest

    fetch(fetchUrl, {
        mode: 'no-cors',
        method: 'POST', // or 'PUT'
        headers: {
        'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
        /*.then(function(response) {
            console.log(response.ok);
        })
        .catch(function(error) {
            document.getElementById('errOut').value = "Fetch error " + error;
        }*/
}

// Runs when join button is clicked
function handleSubmit(event) {
    event.preventDefault();
    var ipFrag = document.getElementById('ipFrag').value;
    
    try {
        postData("F10C1B4F-382E-49D9-857E-1CADC7DC675C", ipFrag);
    }
    catch(err)
    {
        console.log("error, " + err);
    }
    
    
    console.log(ipFrag);
    return false;
}