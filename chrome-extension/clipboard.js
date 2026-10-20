document.getElementById("linkedinToClipboard").addEventListener("click", async () => { 
    await navigator.clipboard.writeText("https://www.linkedin.com/in/grayson-domoleczny-8a4456351")
})

document.getElementById("githubToClipboard").addEventListener("click", async () => { 
    await navigator.clipboard.writeText("https://github.com/GraysonDomoleczny")
})

document.getElementById("lewisDescToClipboard").addEventListener("click", async () => { 
    await navigator.clipboard.writeText("Bachelor of Science (BS) in Computer and Information Technology. Current 4.0 GPA with coursework focused on programming, databases, networking, cybersecurity, and information technology.")
})

document.getElementById("codDescToClipboard").addEventListener("click", async () => { 
    await navigator.clipboard.writeText("Associate of Applied Science (AAS) in Computer Information Technology, graduated Magna Cum Laude. Completed coursework and technical training in networking, cybersecurity, Linux, Windows administration, programming, and systems troubleshooting.")
})

document.getElementById("reyesAddressToClipboard").addEventListener("click", async () => { 
    await navigator.clipboard.writeText("6250 North River Road")
})