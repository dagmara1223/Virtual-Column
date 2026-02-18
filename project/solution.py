import pandas as pd
import re

'''
This function should chceck wether the column name is valid. 
Column name is valid if :
- is not empty
- contains only letters and underscores
'''
def is_valid_column_name(column_name: str) -> bool:
    if not column_name:
        return False 
    pattern = r"^[A-Za-z_]+$"
    return re.fullmatch(pattern, column_name) is not None
        
'''
This function checks whether the rule is correct. 
It is, when:
- Role contains only : +, -, *, _
- Role may contain spaces and letters
'''
def is_valid_role(role: str)->bool:
    if not isinstance(role, str) or not role.strip():
        return False 
    pattern = r"^[A-Za-z_+\-* ]+$"
    return re.fullmatch(pattern, role) is not None 

'''
This function extracts column1, column2 and operator from role.
'''
def parse_role(role: str) -> tuple | None:
    role = role.replace(" ", "")
    operators = ["*", "-", "+"]
    is_operator = []
    
    for i in role:
        if i in operators:
            is_operator.append(i)
    # if more than one operator: 
    if len(is_operator) != 1:
        return None
    
    # split two columns by operator
    op = is_operator[0]
    columns = role.split(op)
    
    if len(columns)!=2:
        return None 
    left_column = columns[0]
    right_column = columns[1]
    if not left_column or not right_column:
        return None 
    
    return left_column, right_column, op

'''
Main execute
'''
def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    # Validation

    #Type 
    if not isinstance(df, pd.DataFrame):
        return pd.DataFrame()
    #New Column name 
    if not is_valid_column_name(new_column):
        return pd.DataFrame()
    #All columns
    for column in df.columns:
        if not is_valid_column_name(column):
            return pd.DataFrame()
    #Role
    if not is_valid_role(role):
        return pd.DataFrame()
    
    parsed_role = parse_role(role)
    if parsed_role == None:
        return pd.DataFrame()
    left_role, right_role, operator = parsed_role 
    
    if left_role not in df.columns or right_role not in df.columns:
        return pd.DataFrame()

    # Creating new column
    new_df = df.copy()
    if operator == "+":
        new_df[new_column] = new_df[left_role] + new_df[right_role]
    
    elif operator == '-':
        new_df[new_column] = new_df[left_role] - new_df[right_role]
    
    elif operator == "*":
        new_df[new_column] = new_df[left_role] * new_df[right_role]
    
    return new_df

# Testing by hand 
# if __name__ == "__main__":
#     result_col = is_valid_column_name("test")
    
#     result_pr = is_valid_role("test1 + tst2")
#     print(result_pr)


    
