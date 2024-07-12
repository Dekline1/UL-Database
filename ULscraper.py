import pandas as pd
import ssl
import glob
import time

ssl._create_default_https_context = ssl._create_unverified_context
ulSiteUrl = "https://iq.ul.com/pwb/Trade.aspx"
ourPcbCollection = "Our company PCB list.xlsx"
quality_control_order_pattern = "DYN*.xlsx"


def ul_site_scrap_maker(amount="full"):
    scraper = pd.read_html(ulSiteUrl)
    ul_scrap = scraper[0]
    if amount == "full":
        ul_scrap.iloc[:, [0, 1]].to_excel("Full UL list.xlsx", index=False, header=False)
    else:
        ul_scrap.iloc[:15, [0, 1]].to_excel("First 15 records of UL list.xlsx", index=False,
                                            header=False)


def quality_control_order_file_founder():
    files = glob.glob(quality_control_order_pattern)
    if files:
        return files[0]
    else:
        print("Please add DYN file first and restart script")
        time.sleep(3)
        exit()


def our_pcb_collection_maker():
    qualityControlOrderFilePath = quality_control_order_file_founder()
    qualityControlOrderFile = pd.read_excel(qualityControlOrderFilePath).iloc[:, [2, 4, 6, 7, 10, 11, 12, 13]]
    qualityControlOrderFileFiltered = qualityControlOrderFile[qualityControlOrderFile["Grupa testowa"].isin(["RAP.DOST.", "PCB", "PCB_AS"])]
    qualityControlOrderFileFiltered.to_excel(ourPcbCollection, index=False)
    print(f"DYN file successfully converted to {ourPcbCollection}")
    time.sleep(3)
    exit()


# ul_site_scrap_maker()
our_pcb_collection_maker()
