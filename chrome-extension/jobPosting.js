chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
    const tabId = tabs[0].id
    const url = new URL(tabs[0].url)
    const domain = url.hostname

    chrome.scripting.executeScript({
        target: {tabId: tabId},
        args: [domain],
        func: (domain) => {
            if (domain == "www.linkedin.com") {
                const address = document.querySelector('asdasdasdasdasd')?.innerText ?? "Not Found"
                const description = document.querySelector('[id^="JobDetails_AboutTheJob_"] [data-testid="expandable-text-box"]')?.innerText ?? "Not Found"
                const locationInfo = document.querySelector('[data-sdui-screen]')?.innerText ?? "Not Found"
                const location =  locationInfo.split("\n").find(line => /·\s*.*ago\s*·\s*\d+\s+people clicked apply/i.test(line))?.split("·")[0].trim() ?? "Not Found";
                const organization = document.querySelector('[aria-label^="Company, "]')?.innerText ?? "Not Found"
                const title = document.querySelector('[href*="/jobs/view/"]')?.innerText ?? "Not Found"

                return {
                    address: address,
                    description: description,
                    location: location,
                    organization: organization,
                    title: title
                }
            }      
        }
    }, (results) => {
        const job = results[0].result
        console.log(job)

        async function sendData(data) {
            const response = await fetch("http://127.0.0.1:8000/", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify(data)
            })
            await response.json()
        }

        document.getElementById("generateLetter").addEventListener("click", () => { 
            job["action"] = "generateLetter"
            sendData(job)
        })
        
        document.getElementById("logToSpreadsheet").addEventListener("click", () => {
            job["action"] = "logToSpreadsheet"
            sendData(job)
        })
    })
})