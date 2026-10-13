chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
    const tabId = tabs[0].id

    chrome.scripting.executeScript({
        target: {tabId: tabId},
        func: () => {
            return document.querySelector('script[type="application/ld+json"]').textContent
        }
    }, (results) => {
        job = JSON.parse(results[0].result)
        console.log(job)
        const posting = {
            city: job.jobLocation.address.addressLocality,
            description: job.description,
            organization: job.hiringOrganization.name,
            state: job.jobLocation.address.addressRegion,
            streetAddress: job.jobLocation.address.streetAddress,
            title: job.title
        }
        console.log(posting)
    })
})

