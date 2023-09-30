# Task-1: Neural Network for Handwritten Digits Recognition
This code is designed to build and train a neural network for recognizing handwritten digits from the MNIST dataset. The network architecture includes convolutional layers, max pooling, dropout for regularization, and dense layers. It utilizes the Keras library with a TensorFlow backend.

## Installation and Usage
### Dependencies
- Python 3
- Libraries: `numpy`, `pandas`, `seaborn`, `tensorflow`, `keras`, `matplotlib`

### Installation
1. Ensure you have Python 3 installed on your system.
2. Install the required libraries using the following command:
   ```
   pip install numpy pandas seaborn tensorflow keras matplotlib
   ```
### Usage
1. Open a Python environment (Jupyter Notebook, IDE, or command line).
2. Copy and paste the provided code into your environment.
3. Execute the code.

The code performs the following steps:
1. Imports necessary libraries.
2. Loads and preprocesses the MNIST dataset.
3. Normalize the data.
4. Displays 10 random images from the training set.
5. Flattens the images and categorizes the labels.
6. Reshape the data to include a grayscale channel.
7. Builds the neural network with convolutional, max pooling, dropout, and dense layers.
8. Compile the model and fit it to the dataset for training.
9. Plots graphs showing training vs. validation loss and accuracy over epochs.
10. Evaluate the model on the test dataset and display the loss and accuracy.
11. Creates predictions on the test dataset.
12. Generates a confusion matrix to evaluate the performance.

## Code Organization
The code is organized as follows:
- Importing libraries: Necessary libraries are imported, including `numpy`, `pandas`, `seaborn`, `tensorflow`, `keras`, and `matplotlib`.
- Data loading and preprocessing: The MNIST dataset is loaded and preprocessed, including normalization, reshaping, and categorization of labels.
- Model building: A neural network architecture is defined using Keras with TensorFlow backend, including convolutional, max pooling, dropout, and dense layers.
- Model training and evaluation: The model is compiled, trained on the training set, and evaluated on the test set. Loss, accuracy, and confusion matrix are displayed.

## Conclusion
This code demonstrates an efficient approach to building and training a neural network for recognizing handwritten digits. It uses convolutional layers for feature extraction, max pooling for down-sampling, and dropout for regularization. The model achieves high accuracy on the MNIST dataset. The code is well-structured, making it easy to understand and modify for similar tasks.


Certainly! Here's the provided information formatted for a GitHub README.md file:


# Task 2: Working with databases
This project involves creating a simple NoSQL database using MongoDB and providing a Python script to interact with it. The script enables adding, retrieving, updating, and deleting passenger data within the database.

## Installation
### Dependencies
- Python 3
- MongoDB
- Required Python Libraries: `pymongo`

### Instructions
1. Ensure you have Python 3 and MongoDB installed on your system.
2. Install the necessary Python library using the following command:
   ```bash
   pip install pymongo
   ```

## Usage
### Connecting to MongoDB
- The Python script connects to the MongoDB server running on `localhost` at port `27017`.
- Create a database using MongoDB Compass with the database name "titanic" and collection name "data"
- Import the data that has been given to the Task-2 directory
- Run the Python script to interact with the database.


### Functions
- `add_passenger(data)`: Adds a passenger to the database.
- `get_all_passengers()`: Retrieves all passengers from the database.
- `update_passenger(passenger_id, new_data)`: Updates a passenger's information.
- `delete_passenger(passenger_id)`: Deletes a passenger from the database.

# Task-3: Integration with a Google API

This project involves creating a Python script to interact with a Google API to retrieve information. In this example, I have used the Google Sheets API to fetch data from a specific worksheet. The script is capable of sending requests to the API and processing the received data.
---

## Installation

### Dependencies

- Python 3
- Required Python Libraries: `gspread`

### Instructions
1. Ensure you have Python 3 installed on your system.
2. Install the necessary Python library using the following command:
   ```bash
   pip install gspread
   ```

---

## Usage

1. **API Access and Sheet Selection**:
   - Initialize the API access with `gspread.service_account()` and provide the path to your API key JSON file.
   - Open a specific Google Sheet named "s&p500_tickers_list" and select the first worksheet (`wks = sh.get_worksheet(0)`).

2. **Basic Information Retrieval**:
   - Retrieve basic information about the sheet, such as the total number of rows and columns.
   - Fetch the value of specific cells, like 'A9' and a cell in the third row and fourth column.

3. **Fetching All Records**:
   - Retrieve the entire dataset from the Google Sheet using `wks.get_all_records()` and store it in the variable `data`. This approach provides a dictionary for each row, with column names as keys and their corresponding values.

4. **Data Processing Approaches**:
   - **Filtering Data**:
     - Use a list comprehension to filter records where the 'Weight' column has a value greater than 2%. This approach is concise and efficient.
   - **Aggregate Calculation**:
     - Use the `sum()` function to calculate the total shares held for the filtered companies. This is a straightforward and effective way to aggregate data.
   - **Finding Maximum Value**:
     - Use the `max()` function to find the company with the highest number of shares held. This is done by comparing the 'Shares Held' values across all records.

5. **Overall Approach**:
   - The code is organized in a clear and sequential manner, making it easy to follow the flow of execution.
   - Data processing approaches are chosen based on their efficiency and effectiveness. List comprehensions, built-in functions (`sum`, `max`), and lambda functions are employed for specific tasks.

---

## Google Sheet Sample

| Name                               | Ticker | Identifier | SEDOL  | Weight   | Sector | Shares Held    | Local Currency |
|------------------------------------|--------|------------|--------|----------|--------|----------------|----------------|
| APPLE INC                          | AAPL   | 037833100  | 2046251| 7.509788 | -      | 169302916.000  | USD            |
| MICROSOFT CORP                     | MSFT   | 594918104  | 2588173| 6.710840 | -      | 85143918.000   | USD            |
| AMAZON.COM INC                     | AMZN   | 023135106  | 2000019| 3.125138 | -      | 102217629.000  | USD            |
| NVIDIA CORP                        | NVDA   | 67066G104  | 2379504| 2.906099 | -      | 28319819.000   | USD            |
| TESLA INC                          | TSLA   | 88160R101  | B616C79| 1.961302 | -      | 30850041.000   | USD            |
| ALPHABET INC CL A                  | GOOGL  | 02079K305  | BYVY8G0| 1.891169 | -      | 68030443.000   | USD            |
| META PLATFORMS INC CLASS A         | META   | 30303M102  | B7TL820| 1.831602 | -      | 25331408.000   | USD            |
| BERKSHIRE HATHAWAY INC CL B        | BRK.B  | 084670702  | 2073390| 1.648414 | -      | 20420721.000   | USD            |
| ALPHABET INC CL C                  | GOOG   | 02079K107  | BYY88Y7| 1.636199 | -      | 58518947.000   | USD            |

---

This documentation provides an overview of the code and its usage, along with explanations for the data processing approaches and a sample of the Google Sheet data. Users can now effectively interact with a Google API to retrieve and process information using the provided Python script.
