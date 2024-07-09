import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
url = "https://iq.ul.com/pwb/Trade.aspx"
scraper = pd.read_html(url)
print(scraper)
scraper[0].to_csv("ULlist.csv", index=False)

# generuje csv bez rozdzielenia na nazwe producenta i jego UL
