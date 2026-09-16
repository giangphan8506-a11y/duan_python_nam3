import pyodbc
class Database:

    def __init__(self):
        self.conn = pyodbc.connect(
            "DRIVER={SQL Server};"
            "SERVER=LAPTOP-M23D3TF7\\SQLEXPRESS;"
            "DATABASE=QuanLyXeLaiXe;"
            "UID=admin;"
            "PWD=Admin@123;"
        )

    def get_connection(self):
        return self.conn