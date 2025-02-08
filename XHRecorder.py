import asyncio
from playwright.async_api import async_playwright
import sys

async def capture_requests(url, output_file):

	async with async_playwright() as p:

		captured_requests = []
		browser = await p.chromium.launch(headless=True)
		custom_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
		context = await browser.new_context(user_agent=custom_user_agent)
		page = await context.new_page()

		async def handle_request(request):

			if 'fetch' in request.resource_type or 'xhr' in request.resource_type:

				request_info = {
					'url': request.url,
					'method': request.method,
					'resource_type': request.resource_type,
				}

				captured_requests.append(request_info)

				print(f" URL: {request_info['url']}")
				print(f" Method: {request_info['method']}")
				print(f" Resource Type: {request_info['resource_type']}")
				print(" ----------------------------------------------")

				#print(request_info)

		page.on('request', handle_request)

		await page.goto(url)
		await asyncio.sleep(5) # may need tweaking

		with open(output_file, 'w') as f:

			for req in captured_requests:

				f.write(str(req) + '\n')

		await context.close()
		await browser.close()

url = sys.argv[1]
output_file = 'captured_requests.txt'
print(" ----------------------------------------------")
asyncio.run(capture_requests(url, output_file))
