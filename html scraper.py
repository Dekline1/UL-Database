import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
url = "https://iq.ul.com/pwb/Trade.aspx"
scraper = pd.read_html(url)
ULscrapSample = scraper[0]
ULscrapFull = scraper[0]
ULscrapSample.iloc[:20, [0, 1]].to_excel("ULlistSample.xlsx", index=False, header=False)
ULscrapFull.iloc[:, [0, 1]].to_excel("ULlistFull.xlsx", index=False, header=False)
# generuje csv bez rozdzielenia na nazwe producenta i jego UL
