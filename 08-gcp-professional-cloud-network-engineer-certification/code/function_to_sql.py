
import pymysql

db_user = 'root' #os.environ.get('CLOUD_SQL_USERNAME')
db_password = 'demo123' #os.environ.get('CLOUD_SQL_PASSWORD')
db_name = 'demodb' #os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = 'single-odyssey-349606:us-east1:sql-private' #os.environ.get('CLOUD_SQL_CONNECTION_NAME')
host = '10.44.0.3' #os.environ.get('SQL_HOST')

def serverless_vpc(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json()

    cnx = pymysql.connect(user=db_user, password=db_password,host=host, db=db_name)

    with cnx.cursor() as cursor:
        cursor.execute('Select * from Persons;')
        result = cursor.fetchall()
        last_name = result[0][1]
        fisrt_name = result[0][2]
    cnx.close()

    return str(fisrt_name + " " +last_name)
