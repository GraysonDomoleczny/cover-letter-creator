chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
    const tabId = tabs[0].id
    const url = new URL(tabs[0].url)
    const domain = url.hostname

    chrome.scripting.executeScript({
        target: {tabId: tabId},
        args: [domain],
        func: (domain) => {
            if (domain == "www.linkedin.com") {
                const description = document.querySelector('[id^="JobDetails_AboutTheJob_"] [data-testid="expandable-text-box"]')?.innerText ?? "Not Found"
                const locationInfo = document.querySelector('[data-sdui-screen]')?.innerText ?? "Not Found"
                const location = locationInfo.split("\n\n")[2].split(/[·]/)[0].trim()
                const organization = document.querySelector('[aria-label^="Company, "]')?.innerText ?? "Not Found"
                const title = document.querySelector('[href*="/jobs/view/"]')?.innerText ?? "Not Found"

                return {
                    description: description,
                    location: location,
                    organization: organization,
                    title: title
                }
            }

            if (domain == "www.indeed.com") {

            }

            // if standard framework
            const query = JSON.parse(document.querySelector('script[type="application/ld+json"]').innerText)

            const description = query.description
            const organization = query.hiringOrganization.name
            const city = query.jobLocation.address.addressLocality
            const state = query.jobLocation.address.addressRegion
            const streetAddress = query.jobLocation.address.streetAddress
            const title = query.title

            return {     
                description: description,
                location: `${city}, ${state}`,
                organization: organization,
                address: streetAddress,
                title: title
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


// connect to sql