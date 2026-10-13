chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
    const tabId = tabs[0].id

    chrome.scripting.executeScript({
        target: {tabId: tabId},
        func: () => {
            const title = document.querySelector('[href*="/jobs/view/"]')
            const info = document.querySelector('[id^="JobDetails_AboutTheJob_"] [data-testid="expandable-text-box"]')
            const location = document.querySelector("#workspace > div > div.gflllu.gflllr.gfllls.gflkaw.gflkh0.gflllj.gflllk.gfllll.gflllm.gfllln.gflk0l.gflk0j.gflgy6.gflanr.gflgqm.gflk0n.gflk0p.gfllgi > div > div.gflk01.gflk00.gflgas.gflarr.gflk02.gfllgi > div > div:nth-child(2) > div > div > div > div > div.gfllid.gflanj.gflg7u.gflh8y.gflgxu.gflha6.gflhbm.gfllgi > div > div.gflanb.gfllgi > div > div.gfllid.gflanj.gflg7u.gflh8y.gflgxu.gflha6.gflhci.gfllgi > p > span:nth-child(1)")

            return {
                info: info.innerText,
                location: location.innerText,
                title: title.innerText
            }
        }
    }, (results) => {
        const job = results[0]
        console.log(job)
    })
})

