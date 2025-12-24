from utils.getAGConnection import getAGConnection



def executeQuery(query):
   
    
    connection= getAGConnection()

    cursor = connection.cursor()
   
   
    cursor.execute(query)

    connection.commit()

    
    cursor.close()

    connection.close()