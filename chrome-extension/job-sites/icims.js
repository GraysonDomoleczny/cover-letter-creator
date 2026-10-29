chrome.runtime.onMessage.addListener((message) => {
    if (message.type === "CREDENTIALS") {
        const credentials = message.credentials

        const iframe = window.top.document.getElementById("icims_content_iframe").contentDocument

        iframe.getElementById("PersonProfileFields.Login").value = credentials.username
        iframe.getElementById("PersonProfileFields.Password").value = credentials.password
        iframe.getElementById("PersonProfileFields.Password_Confirm").value = credentials.password

        iframe.getElementById("PersonProfileFields.FirstName").value = "Grayson"
        iframe.getElementById("PersonProfileFields.LastName").value = "Domoleczny"
        iframe.getElementById("rcf2039").value = "Grayson"
        iframe.getElementById("PersonProfileFields.Email").value = "gdomoleczny3@gmail.com"
        
        iframe.getElementById("1101415_PersonProfileFields.PhoneType").value = "mobile"
        iframe.getElementById("1101415_PersonProfileFields.PhoneNumber").value = "2242687918"

    }
})