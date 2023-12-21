from Aviaries.models import AviariesIn,AviariesOut
from database.database import get_db_manager
import sys
sys.path.append('C:/Users/Winner/Desktop/server/Use-case/server')


db_manager = get_db_manager()
def get_aviaries(id):
    query = '''SELECT * 
    FROM aviaries 
    WHERE id = ? '''
    result = db_manager.execute(query,(id,)) 
    print(result)
    return result

def create_Aviaries(aviaries_in:AviariesIn):
    query = '''INSERT INTO aviaries(enclosure_number,enclosure_area)
    VALUES (?,?)'''
    result = db_manager.execute(query,(aviaries_in.enclosure_number, aviaries_in.enclosure_area))
    return result

def update_aviaries(aviaries_in:AviariesIn,id):
    query = '''UPDATE aviaries
    SET enclosure_number = ?, enclosure_area = ?
    WHERE id = ?'''
    result = db_manager.execute(query,(aviaries_in.enclosure_number, aviaries_in.enclosure_area,id))
    return result

def delete_aviaries(id):
    query = '''DELETE FROM aviaries
    WHERE id = ?'''
    result = db_manager.execute(query,(id,))
    return result







