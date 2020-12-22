export const userService = {
    login,
    logout,
    checkAuth,
    updateUser
};

let baseUrl = 'http://127.0.0.1:8000/api'

function login(username, password) {
    const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
    };

    return fetch(baseUrl + '/auth/login/', requestOptions)
        .then(handleResponse)
        .then(token => {
            // login successful if there's a jwt token in the response
            console.log(token)
            if (token) {
                // store user details and jwt token in local storage to keep user logged in between page refreshes
                localStorage.setItem('access', JSON.stringify(token.access))
                localStorage.setItem('refresh', JSON.stringify(token.refresh))
            }
            return token;
        })
}

function logout() {
    // remove user from local storage to log user out
    localStorage.removeItem('access');
    localStorage.removeItem('refresh');
}


function checkAuth() {
    let access = localStorage.getItem('access')
    if (!access) {
        return false
    }
    return true
}

function updateUser(userdata) {
    let access = JSON.parse(localStorage.getItem('access'))
    let userid = JSON.parse(localStorage.getItem("user")).id
    console.log(userid)
    const requestOptions = {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + access
        },
        body: JSON.stringify(userdata)
    };

    return fetch(baseUrl + '/users/' + userid, requestOptions)
        .then(handleResponse)

}

function handleResponse(response) {
    return response.text().then(text => {
        const data = text && JSON.parse(text);
        if (!response.ok) {
            if (response.status === 401) {
                // auto logout if 401 response returned from api
                const error = (data && data.message) || response.statusText;
                return Promise.reject(error);
                // logout();
                // console.log("esto se ejecuta")
                // // location.reload(true);
            }
        }
        return data;
    });
}

