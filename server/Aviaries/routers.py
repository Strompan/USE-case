from fastapi import APIRouter
from Aviaries.resolvers import get_aviaries, create_Aviaries, update_aviaries, delete_aviaries
from Aviaries.models import AviariesIn, AviariesOut

router = APIRouter()
@router.get('/getaviaries/{id}')
def get_aviaries_router(id):
    result = get_aviaries(id)
    return result 

@router.post('/create')
def create_aviaries_router(aviariesin:AviariesIn):
    result = create_Aviaries(aviariesin)
    return result

@router.put('/update/{id}')
def update_aviaries_router(aviariesin:AviariesIn, id):
    result = update_aviaries(aviariesin, id)
    return result

@router.delete('/delete/{id}')
def delete_aviaries_router(id):
    result = delete_aviaries(id)
    return result
    


