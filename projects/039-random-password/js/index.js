function getPassword() {
    let password = "";
    const passwordLength = Math.floor((Math.random() * 4) + 7);

    for (let i = 0; i < passwordLength; i++) {
        password += String.fromCharCode(Math.floor((Math.random() * 94) + 33))
    }

    return password;
}

console.log( getPassword() );