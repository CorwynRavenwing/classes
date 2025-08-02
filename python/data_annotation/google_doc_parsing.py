
import requests
from bs4 import BeautifulSoup

# link = "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub"
link = "https://docs.google.com/document/d/e/2PACX-1vRPzbNQcx5UriHSbZ-9vmsTow_R6RRe7eyAU60xIF9Dlz-vaHiHNO2TKgDi7jy4ZpTpNqM7EvEcfr_p/pub"

def parse_google_doc(link) -> None:
    with requests.get(link) as response_data:
        soup = BeautifulSoup(response_data.text, 'html.parser')

    tables = soup.find_all('table')
    # print(f'{len(tables)=}')
    assert(len(tables) == 1)
    for table in tables:
        trs = table.find_all('tr')
        data = []
        for tr in trs:
            row = [
                td.p.span.text
                for td in tr.find_all('td')
            ]
            data.append(row)
        clean_data = [
            (int(x), int(y), char)
            for (x, char, y) in data
            if x != 'x-coordinate'
        ]
        # print(f'{clean_data=}')
        X_vals = {row[0] for row in clean_data}
        Y_vals = {row[1] for row in clean_data}
        # print(f'{X_vals=} {Y_vals=}')
        X_size = max(X_vals) + 1
        Y_size = max(Y_vals) + 1
        # print(f'{X_size=} {Y_size=}')

        grid = [[' '] * X_size for _ in range(Y_size)]

        for (x, y, char) in clean_data:
            # print(f'{x=} {y=} {char=}')
            grid[y][x] = char
        # print(f'{grid=}')
        # NOTE: (0,0) is in lower-left of grid!
        for row in reversed(grid):
            print(''.join(row))

parse_google_doc(link)

