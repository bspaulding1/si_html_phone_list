#!/usr/bin/env python

import jinja2
import pandas as pd

# TODO: git repo
# TODO: configuration file
# output dir, 
# TODO: argparse + validation
# TODO: accept argument to name output file
# TODO: drive items population off csv (or google sheet)
# TODO: import nan as empty - or handle gracefully
# TODO: feed in other variables to template
# file_name?
# TODO: button color, style
# TODO: i could have a column key name mapping take place since the end columns will be consistent


output_file = '/Users/spauldo/Library/Mobile Documents/com~apple~CloudDocs/Downloads/auction2023.html'

items = []
items.append(dict(name="Joe", phone="123"))
items.append(dict(name="Bill", phone="456"))

df = pd.read_csv('/Users/spauldo/Downloads/Spaulding Underwriting Mailings - SMS.csv')

df['Cell Phone'] = '1' + df['Cell Phone'].str.replace('\(|\)|-| ', '')
df['Home Phone'] = '1' + df['Home Phone'].str.replace('\(|\)|-| ', '')

df = df.fillna('')

items = df.to_dict('records')

def main():
    templateLoader = jinja2.FileSystemLoader(searchpath="./")
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = "phone_list.html.j2"
    template = templateEnv.get_template(TEMPLATE_FILE)
    outputText = template.render(items=items)  # this is where to put args to the template renderer

    # print(outputText)
    with open(output_file, "w") as text_file:
        text_file.write(outputText)
    
    
if __name__ == '__main__':
    main()
