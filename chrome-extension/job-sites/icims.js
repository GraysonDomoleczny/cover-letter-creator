chrome.runtime.onMessage.addListener((message) => {
    if (message.type === "CREDENTIALS") {
        const credentials = message.credentials
        console.log(credentials)
        // document.getElementById("PersonProfileFields.Login").value = credentials.username
        // document.getElementById("PersonProfileFields.Password").value = credentials.password
        // document.getElementById("rcf2039").value = "yay"
    }
})