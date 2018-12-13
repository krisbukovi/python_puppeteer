# filename: puppet.py 
# author: krisbukovi
# purpose: to start a chrome browser up using puppeteer that cycles through all 13 million abstract pages and captures the html and stores it in a postgres db. 


%%cython
import time 
import asyncio
from pyppeteer import launch

async def main():

	urls = ['https://ui.adsabs.harvard.edu/#abs/2019MNRAS.482.1858Y/abstract', 'https://ui.adsabs.harvard.edu/#abs/2019Icar..319....1A/abstract', 'https://ui.adsabs.harvard.edu/#abs/2019MNRAS.482.1786L/abstract', 'https://ui.adsabs.harvard.edu/#abs/2019MNRAS.482.1733G/abstract', 'https://ui.adsabs.harvard.edu/#abs/2019MNRAS.482.5018E/abstract']	
	size = len(urls)
	start_time = time.time()

	
	for u in urls:

		browser = await launch()
		page = await browser.newPage()
		await page.goto(u)
	

		content = await page.evaluate('''() => {

			return {

				html: document.documentElement.outerHTML

			}	

		}''')

		#print(content)

	await browser.close()

	seconds = time.time() - start_time
	days = (13000000 * (seconds/86400.0))/size
	print("%s seconds to run program" % (seconds))
	print("%f days to grab code for all 13 million abstracts" % (days))


asyncio.get_event_loop().run_until_complete(main())
