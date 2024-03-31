import psycopg2
conn = psycopg2.connect(database="python-test1",
                        host='python-test1-host',
                        user='python-test1-user',
                        password='python-test1-password',
                        port='python-test1-port')

cursor = conn.cursor()

cursor.execute('SELECT * FROM python-test1')