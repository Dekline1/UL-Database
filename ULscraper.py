import pandas as pd
import ssl
import glob


def find_quality_control_order_file():
    pattern = "DYN*.xlsx"
    files = glob.glob(pattern)
    if files:
        return files[0]
    else:
        raise FileNotFoundError("File meeting criteria not found")


def scrap_maker(amount=999999):
    scraper = pd.read_html(ulSiteUrl)
    ul_scrap = scraper[0]
    if amount >= 999999:
        ul_scrap.iloc[:amount + 1, [0, 1]].to_excel("Full UL list.xlsx", index=False, header=False)
    else:
        ul_scrap.iloc[:amount + 1, [0, 1]].to_excel(f"First {amount} records of UL list.xlsx", index=False,
                                                    header=False)


ssl._create_default_https_context = ssl._create_unverified_context
ulSiteUrl = "https://iq.ul.com/pwb/Trade.aspx"
ourPcbCollection = "Our company PCB list.xlsx"

scrap_maker(15)

qualityControlOrderFilePath = find_quality_control_order_file()
qualityControlOrderFile = pd.read_excel(qualityControlOrderFilePath).iloc[100:110, :]
print(qualityControlOrderFile)
qualityControlOrderFile.to_excel(ourPcbCollection, index=False)