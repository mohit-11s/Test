import psycopg2
import json
import os
try:
    print('inside try block')
    filePath=os.getcwd()
    print(filePath)


    try:
        with open(os.path.join(filePath,'config.json')) as f:
            config=json.load(f)
            print('hostname=',config['hostname'])
    except Exception as err:
        print(f' exception in opening config.json')

    try:
        Conn=psycopg2.connect(
            host=config['hostname'],
            password=config['password'],
            port=config['port'],
            user=config['username'],
            dbname=config['dbname']

        )
        print('connection is successfull')
        Conn.autocommit = True
    
        database=input('enter the name of the database: ').strip().capitalize()
        try:
            with Conn.cursor() as cur:
                print('cursor crated successfully')


                check_database_query=f''' select 1 from pg_database where datname=%s'''
                cur.execute(check_database_query,(database,))
                exist=cur.fetchone()
                if exist:
                    print(f'{database} already exist hence skipping db creation')
                else:
                    try:
                        create_database_query=f'''create database "{database}"'''
                        print('create databse successfull')
                        cur.execute(create_database_query)


                    except Exception as err:
                        print(f'error in creating database {err}')


        except Exception as err:
            print(f'error in creating cursor {err}')


    
    except Exception as err:
        print(f' exception in conneting to database {err}')


except Exception as err:
    print(f'Exception occured {err}')