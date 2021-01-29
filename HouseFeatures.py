from pydantic import BaseModel
class HouseFeatures(BaseModel):
    total_sqft: float 
    bhk: int
    bath: int
    location: str 