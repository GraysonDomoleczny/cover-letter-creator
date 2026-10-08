chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
    const tabId = tabs[0].id

    chrome.scripting.executeScript({
        target: {tabId: tabId},
        func: () => {
            return document.querySelector('script[type="application/ld+json"]').textContent
        }
    }, (results) => {
        job = JSON.parse(results[0].result)
        console.log(job.description)
    })
})

