/*!
* Start Bootstrap - Freelancer v7.0.5 (https://startbootstrap.com/theme/freelancer)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-freelancer/blob/master/LICENSE)
*/
//
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {
    document.getElementById('reportform').addEventListener('submit', function(e) {
        e.preventDefault();
        
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/report');
        xhr.setRequestHeader('Content-Type', 'application/json');
        
        var site = document.getElementById('site').value;

        var data = `{
        "site": "${site}"
        }`;

        xhr.send(data);
        document.getElementById('submitSuccess').style.display = "block";
    });
});
