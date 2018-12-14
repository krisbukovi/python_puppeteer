# filename: pupp://ui.adsabs.harvard.edu/#abs/2019ScTEn.650.1722P/abstract t.py 
# author: krisbukovi
# purpose: to start a chrome browser up using puppeteer that cycles through all 13 million abstract pages and captures the html and stores it in a postgres db. 


import time 
import asyncio
from pyppeteer import launch
from functools import partial

async def getHTML(pg, webpage):
	await pg.goto(webpage)

	content = await page.evaluate('''() => {

		return {
			html:document.documentElement.outerHTML
		}
	}''')

	return content

async def main():

	urls = ['https://ui.adsabs.harvard.edu/#abs/2019NewA...66...20P/abstract', 'https://ui.adsabs.harvard.edu/#abs/2019NewA...66...31M/abstract', 'https://ui.adsabs.harvard.edu/#abs/2019NewA...66...40N/abstract', 'https://ui.adsabs.harvard.edu/#abs/2019AcSpA.209..264M/abstract', 'https://ui.adsabs.harvard.edu/#abs/2019JMoSt1177..418K/abstract', 'https://ui.adsabs.harvard.edu/#abs/2019MNRAS.482.4364C/abstract', 'https://ui.adsabs.harvard.edu/#abs/2019MNRAS.482.4372C/abstract', 'https://ui.adsabs.harvard.edu/#abs/2019MNRAS.482.4422C/abstract', 'https://ui.adsabs.harvard.edu/#abs/2019MNRAS.482.4726N/abstract', 'https://ui.adsabs.harvard.edu/#abs/2019MNRAS.482.4985A/abstract', 'https://ui.adsabs.harvard.edu/#abs/2019MNRAS.482.5167S/abstract', 'https://ui.adsabs.harvard.edu/#abs/2019MNRAS.482.5349R/abstract', 'https://ui.adsabs.harvard.edu/#abs/2019MNRAS.482.5459M/abstract', 'https://ui.adsabs.harvard.edu/#abs/2019MNRAS.482.5553J/abstract', 'https://ui.adsabs.harvard.edu/#abs/2019MNRAS.482.5567M/abstract', 'https://ui.adsabs.harvard.edu/#abs/2019MNRAS.483..392D/abstract', 'https://ui.adsabs.harvard.edu/#abs/2019MNRAS.483..458B/abstract', 'https://ui.adsabs.harvard.edu/#abs/2019MNRAS.483..711A/abstract', 'https://ui.adsabs.harvard.edu/#abs/2019MNRAS.483..529C/abstract', 'https://ui.adsabs.harvard.edu/#abs/2019MNRAS.483..840B/abstract', 'https://ui.adsabs.harvard.edu/#abs/2019MNRAS.483L..47C/abstract', 'https://ui.adsabs.harvard.edu/#abs/2019MNRAS.483L..64D/abstract', 'https://ui.adsabs.harvard.edu/#abs/2019NewA...67....1N/abstract', 'https://ui.adsabs.harvard.edu/#abs/2019NewA...67...45V/abstract', 'https://ui.adsabs.harvard.edu/#abs/2019NewA...68...51M/abstract', 'https://ui.adsabs.harvard.edu/#abs/2019IJAEO..75...15B/abstract', 'https://ui.adsabs.harvard.edu/#abs/2019PhyE..107....5B/abstract', 'https://ui.adsabs.harvard.edu/#abs/2019SurSc.681...32E/abstract', 'https://ui.adsabs.harvard.edu/#abs/2019CNSNS..70...89J/abstract', 'https://ui.adsabs.harvard.edu/#abs/2019CNSNS..70..223O/abstract', 'https://ui.adsabs.harvard.edu/#abs/2015AIPC.1672m0003H/abstract', 'https://ui.adsabs.harvard.edu/#abs/2019MNRAS.482.1858Y/abstract', 'https://ui.adsabs.harvard.edu/#abs/2019Icar..319....1A/abstract', 'https://ui.adsabs.harvard.edu/#abs/2019MNRAS.482.1786L/abstract', 'https://ui.adsabs.harvard.edu/#abs/2019MNRAS.482.1733G/abstract', 'https://ui.adsabs.harvard.edu/#abs/2019MNRAS.482.5018E/abstract']	
	size = len(urls)
	start_time = time.time()

	browser = await launch(headless = True)
	page = await browser.newPage()
	
	content = map(partial(getHTML, page), urls) 

	#print(content)

	await browser.close()

	seconds = time.time() - start_time
	days = (13000000 * (seconds/86400.0))/size
	
	print("size is %d" % size)
	print("%s seconds to run program" % (seconds))
	print("%f days to grab code for all 13 million abstracts" % (days))


asyncio.get_event_loop().run_until_complete(main())
