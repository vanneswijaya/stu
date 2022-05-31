from fastapi import Request, Response, FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from master import Convert

app = FastAPI()

from_app_dummy_data = {"from_cur":"HKD",
                            "from_amt":1000,
                            "to_cur":"SGD",
                            "to_amt":0,}
                        

# @app.post("/convert") #bs tmbahin user_id klo mau 
# async def instant(transaction: Transaction):
#     convert_dict = transaction.dict()
#     return convert_dict

@app.post("/instant") #bs tmbahin user_id klo mau 
async def instant(request: Request):
    rjson = await request.json()
    instant = Convert(rjson['to_cur'], rjson['from_amt'], rjson['to_amt'])
    output_dict = instant.output_dict()
    return JSONResponse(status_code=200, content=output_dict)

@app.post("/cashback")
async def cashback(request: Request):
    rjson = await request.json()
    cashback = Convert(rjson['to_cur'], rjson['from_amt'], rjson['to_amt'])
    cashback_dict = cashback.cashback(rjson['input_tp'])
    return JSONResponse(status_code=200, content=cashback_dict)
    
@app.post("/graph-data")
async def cashback(request: Request):
    rjson = await request.json()
    data = Convert(rjson['to_cur'], 10, 0)
    data_dict = data.compare_real_price()
    return JSONResponse(status_code=200, content=data_dict)