# XHRecorder
Playwright-based script that captures all network requests a website makes when first visited. Things like XHR fetches, API calls, or what third-party scripts are being loaded to figure out what a site is loading and from where. Useful for identifying third-party trackers, ad networks, unexpected data leaks, API endpoints, etc.

Usage:
```
python XHRecorder.py https://target.site
```

Output:
```
----------------------------------------------
 URL: https://copilot.microsoft.com/locales/en-US/translation.json
 Method: GET
 Resource Type: fetch
 ----------------------------------------------
 URL: https://copilot.microsoft.com/fd/ls/lsp.aspx?
 Method: POST
 Resource Type: xhr
 ----------------------------------------------
 URL: https://copilot.microsoft.com/
 Method: GET
 Resource Type: fetch
 ----------------------------------------------
 URL: https://copilot.microsoft.com/c/api/start
 Method: POST
 Resource Type: fetch
 ----------------------------------------------
 URL: https://copilot.microsoft.com/c/api/conversations
 Method: POST
 Resource Type: fetch
 ----------------------------------------------
 URL: https://copilot.microsoft.com/c/api/conversations/ADfouRpbYZKRXqZEqTk3n/history
 Method: GET
 Resource Type: fetch
 ----------------------------------------------
 URL: https://copilot.microsoft.com/c/api/conversations
 Method: GET
 Resource Type: fetch
 ----------------------------------------------
 URL: https://copilot.microsoft.com/c/api/config
 Method: GET
 Resource Type: fetch
 ----------------------------------------------
 URL: https://copilot.microsoft.com/c/api/user
 Method: GET
 Resource Type: fetch
 ----------------------------------------------
 URL: https://copilot.microsoft.com/c/api/user/settings
 Method: GET
 Resource Type: fetch
 ----------------------------------------------
 URL: https://copilot.microsoft.com/c/api/conversations
 Method: GET
 Resource Type: fetch
 ----------------------------------------------
 URL: https://browser.events.data.microsoft.com/OneCollector/1.0/?cors=true&content-type=application/x-json-stream&w=0
 Method: POST
 Resource Type: xhr
```
