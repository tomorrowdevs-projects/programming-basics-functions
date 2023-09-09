function getPassword() {
    const password = [];
    password.length = Math.floor((Math.random() * 4) + 7);

    for (let i = 0; i < password.length; i++) {
        password[i] = String.fromCharCode(Math.floor((Math.random() * 94) + 33))
    }

    return password.join("");
}

console.log( getPassword() );