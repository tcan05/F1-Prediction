import os
import pandas as pd


def read_dataset(filename: str):
    '''
    Read the dataset from a CSV file.
    
    :param filename: Name of the CSV file.
    :type filename: str
    '''

    script_dir = os.path.dirname(os.path.abspath(__file__))

    filename = filename
    filepath = os.path.join(script_dir, filename)

    dataset = pd.read_csv(filepath)
    print(f"Dataset '{filename}' loaded successfully.")
    
    return dataset


def clean_dataset_save(dataset: pd.DataFrame, new_filename: str, columns_to_drop: list):
    '''   
    Drop the selected column(s) and save the dataset to a new CSV file.

    :param dataset: Input as pandas DataFrame.
    :type dataset: pd.DataFrame
    :param new_filename: _cleaned.csv is appended to this parameter.
    :type new_filename: str
    :param columns_to_drop: List of column names to be dropped.
    :type columns_to_drop: list
    '''

    base_name = os.path.splitext(new_filename)[0]

    dataset = dataset.drop(columns = columns_to_drop, axis = 1)
    dataset.to_csv(f"{base_name}_cleaned.csv", index = False)


def join_datasets_save(on_column: str, new_filename: str, joined_how: str, dataset1: pd.DataFrame, dataset2: pd.DataFrame, dataset3: pd.DataFrame = None):
    '''
    Join two or three datasets on a specific column and save the new dataset to a CSV file.

    :param on_column: Which column to join the dataset on.
    :type on_column: str
    :param new_filename: _combined.csv is appended to this parameter.
    :type new_filename: str
    :param joined_how: How to join the datasets (e.g. 'inner', 'outer', 'left', 'right').
    :type joined_how: str
    :param dataset1: First input as pandas DataFrame.
    :type dataset1: pd.DataFrame
    :param dataset2: Second input as pandas DataFrame.
    :type dataset2: pd.DataFrame
    :param dataset3: Optional third input as pandas DataFrame.
    :type dataset3: pd.DataFrame
    '''

    base_name = os.path.splitext(new_filename)[0]

    if dataset3 is not None:

        combined_data = pd.merge(dataset1, dataset2, on = on_column, how = joined_how)
        combined_data = pd.merge(combined_data, dataset3, on = on_column, how = joined_how)

    else:
        combined_data = pd.merge(dataset1, dataset2, on = on_column, how = joined_how)

    combined_data.to_csv(f"{base_name}_combined.csv", index = False)


def rename_column_save(dataset: pd.DataFrame, new_filename: str, old_col_name: str, new_col_name: str):
    '''
    Rename a specific column in the dataset and save it to a new CSV file.

    :param dataset: Input as pandas DataFrame.
    :type dataset: pd.DataFrame
    :param new_filename: _renamed.csv is appended to this parameter.
    :type new_filename: str
    :param old_col_name: Column name to be renamed.
    :type old_col_name: str
    :param new_col_name: New column name.
    :type new_col_name: str
    '''

    base_name = os.path.splitext(new_filename)[0]

    dataset.rename(columns = {old_col_name: new_col_name}, inplace = True)
    dataset.to_csv(f"{base_name}_renamed.csv", index = False)


def freq_encode(dataset: pd.DataFrame, col: str):
    '''
    Frequency encode a specific column and insert it to the dataset.
    Deletes the original column after encoding.

    :param dataset: Input as pandas DataFrame.
    :type dataset: pd.DataFrame
    :param col: Column name to be frequency encoded.
    :type col: str
    '''

    freq = (dataset.groupby(col).size() / len(dataset)).round(4)

    dataset.loc[:, "{}_freq".format(col)] = dataset[col].map(freq)
    dataset.drop(columns = [col], axis = 1, inplace = True)

    return dataset["{}_freq".format(col)]


def time_to_seconds(t):
    '''
    Convert time in format "M:S.MS" to total seconds as float.
    
    :param t: Time in format "M:S.MS"
    '''
    
    if pd.isna(t) or t == "\\N" or t == "":
        return 0.0
    
    minutes, seconds = t.split(":")
    return round(int(minutes) * 60 + float(seconds), 3)


def fill_na_zero(dataset: pd.DataFrame, columns: list):
    '''    
    :param dataset: Input as pandas DataFrame.
    :type dataset: pd.DataFrame
    :param columns: List of column names to be filled with zero.
    :type columns: list
    '''

    dataset[columns] = dataset[columns].replace("\\N", 0)
    return dataset