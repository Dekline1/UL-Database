import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

scraper = pd.read_html("https://iq.ul.com/pwb/Trade.aspx")

i = [0, 1,2,3]
for df in scraper:
    #print(df[i].to_string(header=False))
    for line in df[i]:
        line.to_csv('id.txt', header=False, index=False)


