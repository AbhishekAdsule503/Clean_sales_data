📘 The "Sales Data" Cleaner
1. Project Title & Goal

This project reads a messy sales CSV file, cleans the data, removes duplicates, converts prices from USD to INR, and saves the final clean data into a JSON file.

2. Setup Instructions
Prerequisites

Python 3 installed on your system

Steps to Run

Keep all files in the same folder:

sales.csv

sales_cleaner.py

Open terminal / command prompt in that folder.

Run the script using this command:

python sales_cleaner.py


After successful execution, a new file named clean_sales.json will be created in the same folder.

3. The Logic (How I Thought)
Why did I choose this approach?

I used Python because it has built-in modules like csv and json which are simple and efficient for data processing tasks.
To remove duplicates, I used a set because it helps quickly check whether a product with the same price already exists.
I kept the logic straightforward so that the data cleaning steps are easy to understand and debug.

What was the hardest bug I faced, and how did I fix it?

The hardest issue I faced was that the output file (clean_sales.json) was not visible at first.
I realized that Python was creating the file in the current working directory, not the folder I was checking.
To fix this, I ensured that I ran the script from the same folder where the CSV file was present and verified the working directory.

4. Output Screenshots

 the screenshot of the final output file opened in a text editor:

5. Future Improvements

If I had 2 more days, I would:

Add proper error handling for incorrect or missing CSV data

Make the currency conversion dynamic instead of hardcoded

Add logging to track data cleaning steps

Create unit tests to verify the output automatically
