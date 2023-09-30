# **Find the Google Sheet here:** _[sheet_link]_(https://docs.google.com/spreadsheets/d/103GblZTjzJ45q7LHkKwLNf5Zi0M6Z1lGmkL2b-aqbKw/edit?usp=sharing)


# Code Organization:

**API Access and Sheet Selection:**

- You start by initializing the API access with `gspread.service_account()` and provide the path to your API key JSON file.
- Next, you open a specific Google Sheet named "s&p500_tickers_list" and select the first worksheet (`wks = sh.get_worksheet(0)`).

**Basic Information Retrieval:**

- You retrieve basic information about the sheet such as the total number of rows and columns.
- Additionally, you fetch the value of specific cells, like 'A9' and a cell in the third row and fourth column.

**Fetching All Records:**

- The entire dataset from the Google Sheet is retrieved using `wks.get_all_records()` and stored in the variable `data`.
- This approach provides a dictionary for each row, with column names as keys and their corresponding values.

**Data Processing Approaches:**

**Filtering Data:**

- A list comprehension is used to filter records where the 'Weight' column has a value greater than 2%. This approach is concise and efficient.

**Aggregate Calculation:**

- The `sum()` function is used to calculate the total shares held for the filtered companies. This is a straightforward and effective way to aggregate data.

**Finding Maximum Value:**

- The `max()` function is used to find the company with the highest number of shares held. This is done by comparing the 'Shares Held' values across all records.

**Overall Approach:**

- The code is organized in a clear and sequential manner, making it easy to follow the flow of execution.
- Data processing approaches are chosen based on their efficiency and effectiveness. List comprehensions, built-in functions (`sum`, `max`), and lambda functions are employed for specific tasks.
- This code demonstrates a structured and efficient approach to interacting with a Google Sheet, processing the data, and extracting meaningful information.
