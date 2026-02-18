# Virtual-Column
Small project that implements a safe and validated function for dynamically adding a virtual column to a Pandas DataFrame based on a simple arithmetic rule. <br>

The function: <br>
- Validates input DataFrame and Column Names
- Validates math expression
- Supports basic operations like '*', '-', '+'
- If validation fails - returns and empty DataFrame

## 🎨 Features 
- Fully tested with pytests
- Expression validation using regex
- Strict colum name validation
- Protection against invalid input

## Running Tests 
Install dependencies: <br>
```
pip install pandas pytest
```
Run tests using terminal: <br>
```
pytest
```

## 🤖 Example Usage 
➡️Input: Two columns <br>
**label_one** with values : 1, 4, 10 <br>
**label_two** with values: 2, 5, 12 <br>

⬅️ Expected output: <br>
**label_three = label_one + label_two** with values: 3, 9, 22 <br>

Input code: 
```
import pandas as pd
from solution import add_virtual_column

df = pd.DataFrame(
    [[1,2], [4,5], [10,12]],
    columns=["label_one", "label_two"]
)

result = add_virtual_column(df, "label_one + label_two", "label_three")

print(result)
```
<br>
Results ✅ : <br>
<img width="327" height="75" alt="image" src="https://github.com/user-attachments/assets/ca6dfce4-e570-43ac-a0cd-3ac991dcb5a8" /> <br>





