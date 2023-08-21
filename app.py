import streamlit
import pandas as pd


# Create dummy data with three columns for testing. Two columns are categorical and others are real

def initialize_data():
    return pd.DataFrame({
        'categorical_1': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
        'categorical_2': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
        'real_1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'real_2': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    })


def main():
    df = initialize_data()
    streamlit.title('Streamlit App')
    streamlit.write(df)




if __name__ == '__main__':
    main()