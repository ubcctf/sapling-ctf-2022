/*!
* Start Bootstrap - Freelancer v7.0.5 (https://startbootstrap.com/theme/freelancer)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-freelancer/blob/master/LICENSE)
*/
//
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {
    document.getElementById('reviewform').addEventListener('submit', function(e) {
        e.preventDefault();
        
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/add_review');
        xhr.setRequestHeader('Content-Type', 'application/json');
        
        var name = document.getElementById('name').value;
        var message = document.getElementById('message').value;
        var stars = document.getElementById('stars').value;

        var data = `{
        "name": "${name}",
        "message": "${message}",
        "stars": "${stars}"
        }`;

        xhr.send(data);

        console.log(xhr.response);

        document.getElementById('submitSuccessMessage').style.display = "block";
        
    });
});
