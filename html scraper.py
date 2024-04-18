import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

scraper = pd.read_html("https://en.wikipedia.org/wiki/Printed_circuit_board")

for idx, table in enumerate(scraper):
    print("*"*120)
    print(idx)
    print(table)
    print("*" * 120)

print("*" * 120)
print("*" * 120)
print("*" * 120)
print(scraper[3])