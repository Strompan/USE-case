from pydantic import BaseModel 

class AviariesIn(BaseModel):
    enclosure_number:int
    enclosure_area:int

class AviariesOut(BaseModel):
    id:int
    enclosure_number:int
    enclosure_area:int


