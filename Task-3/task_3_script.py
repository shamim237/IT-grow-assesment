import gspread


sa = gspread.service_account(r"C:/Users/jibon/.config/gspread/service_account.json") # path to the json file containing an api key
sh = sa.open("s&p500_tickers_list") # read the google sheet
wks = sh.get_worksheet(0) # load the worksheet, here lloading the 1st worksheet

print("Rows: ", wks.row_count) # get the total no. of rows in the sheet
print("Cols: ", wks.col_count) # get the total no. of columns in the sheet
print(wks.acell('A9').value)   # get the value of "A9" column
print(wks.cell(3,4).value)     # get the value of rxc value
print(wks.get('A7:E9'))        # get the value between column A7 to E9
print("="*100)

data = wks.get_all_records() # get the whole data from the google sheet


# Filter data for companies with a Weight greater than 2%
filtered_data = [row for row in data if float(row['Weight']) > 2]

# Calculate total shares held for companies with a Weight greater than 2%
total_shares_held = sum(float(row['Shares Held']) for row in filtered_data)

# Find the company with the highest number of shares held
max_shares_company = max(data, key=lambda row: float(row['Shares Held']))

# Print the results
print(f"Companies with Weight > 2%: {filtered_data}")
print("="*100)
print(f"Total shares held for filtered companies: {total_shares_held}")
print("="*100)
print(f"Company with the highest number of shares held: {max_shares_company}")
print("="*100)
   