from extract import fetch_data
from transfor import tranform_data
from load import connect_to_db


def main():
    connection = connect_to_db()
    print(f"Code Run Successfully")




if __name__ == '__main__':
    main()