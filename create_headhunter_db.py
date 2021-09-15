import sqlite3

connection = sqlite3.connect("headhunter.db")
create_table_query = '''CREATE TABLE vacancies_short (
                                added_at TEXT,
                                query_string TEXT,
                                type TEXT,
                                level TEXT,
                                direction TEXT,
                                vacancy_id TEXT,
                                premium TEXT,
                                has_test,response_url TEXT,
                                address_city TEXT,
                                address_street TEXT,
                                address_building TEXT,
                                address_description TEXT,
                                address_lat TEXT,
                                address_lng TEXT,
                                address_raw TEXT,
                                address_metro_stations TEXT,
                                alternate_url TEXT,
                                apply_alternate_url TEXT,
                                department_id TEXT,
                                department_name TEXT,
                                salary_from TEXT,
                                salary_to TEXT,
                                salary_currency TEXT,
                                salary_gross TEXT,
                                name TEXT,
                                insider_interview_id TEXT,
                                insider_interview_url TEXT,
                                area_url TEXT,
                                area_id TEXT,
                                area_name,url TEXT,
                                published_at TEXT,
                                employer_url TEXT,
                                employer_alternate_url TEXT,
                                employer_logo_urls_90 TEXT,
                                employer_logo_urls_240 TEXT,
                                employer_logo_urls_original TEXT,
                                employer_name TEXT,
                                employer_id TEXT,
                                response_letter_required TEXT,
                                type_id TEXT,
                                type_name TEXT,
                                archived TEXT,
                                schedule_id TEXT
                                );'''
cursor = connection.cursor()
print("База данных подключена к SQLite")
cursor.execute(create_table_query)
connection.commit()
print("Таблица SQLite создана")