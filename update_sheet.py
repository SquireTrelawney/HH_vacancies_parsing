import schedule
from clickhouse_driver import Client
import sqlite3
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
# client = Client('', 'default', '', '9000', '')
connection = sqlite3.connect("headhunter.db")
cursor = connection.cursor()
vacancies = cursor.execute('SELECT * FROM vacancies_short')
# creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
# gc = gspread.authorize(creds)

def update_sheet():
    print('Updating cell at', datetime.now())
    columns = []
    # print(vacancies)
    for item in cursor.description:
        columns.append(item[0])
        print(item)
    for item in vacancies:
        print(item)
    # df_vacancies = pd.DataFrame(vacancies, columns=columns)
    # df_vacancies.to_csv('vacancies_short.csv', index=False)

    # content = open('vacancies_short.csv', 'r').read()
    print("Записано в таблицу")
    # print(content)
    # gc.import_csv('1ZWS2kqraPa4i72hzp0noU02SrYVo0teD7KZ0c3hl-UI', content.encode('utf-8'))

update_sheet()
schedule.every().day.at("11:11").do(update_sheet)
while True:
    schedule.run_pending()
