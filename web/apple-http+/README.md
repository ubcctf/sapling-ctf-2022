# Apple HTTP+

Write a crappy single-threaded HTTP server in Swift that can handle multiple connections via event loop/async/await conccurency. Idea is to have a race condition during processing of the HTTP authorization header that allows user to authenticate as admin without correct creds.

## 1st part
Competitor reads the user/pass from the employees.txt file and sends an HTTP request with custom APPLE-USERNAME / APPLE-PASSWORD headers set to the user/pass of an employee. This gives them access to some secret employee-only page with the flag.

## 2nd part
The hardest part could be this race condition thing (send request with auth as normal employee hitting one of the /secret?? endpoints, send another request at the same time (slightly later) attempting to log in as "admin" (with incorrect creds), 2nd request should change username to "admin" right before the first request hits the username=="admin" and session.is_authenticated check guarding the /secret?? path). Gives competitor access to an "executive" only page that has some apple-meme on it + flag

```python

employees = [
    (user??, passw??),
    (user??, passw??),
    (user??, passw??),
    (user??, passw??),
    (user??, passw??),
]

def new_connection(socket ??):

    method = await get_method()??
    
    path = await get_path()??

    cookie = await get_cookie()??

    ?? if not cookie create new session ?? 

    session_token = ??extract from cookie?

    session = sessions[session_token]??


    session.username = await ??
    session.password = await ??
    session.is_authenticated = await authenticate(username, password)

    ???

    if path == "/":

        ??

    elif path == "/??":

        if session.username == "t1m_c00k" and session.is_authenticated:
            return flag response ?? "flag??{HTTP_IS_EZ_WITH_APPLE_HTTP+}"
        else:
            return negative response ??

    elif path == "/??secret??":

        if session.username == "steve_jobs" and session.is_authenticated:
            return flag response ?? "flag{RACE_CONDITIONS_ARE_EZ_WITH_APPLE_HTTP+}"
        else:
            return negative response ??

    else:

        ??

def authenticate(username, password):
    return authenticate_employee(username, password) or authenticate_executive(username, password)
    
    if (username, password) in employees:
        return True

    if username == "t1m_c00k" and password == (await load_tims_password()):
        ??

    ??

    return False

    if username == "t1m_c00k" and password == "mustbsecure8987fefb99196e3a0":
        return True
    elif username == "":
        ??
    else:
        ???

def authenticate_employee(username, password):

    ?? read from employee file
    return ?? user/pass in file


def authenticate_executive(username, password):
    # executive's usernames/password redacted for "security" purposes
    ?? read from exec file
    return ?? user/pass in file


```
