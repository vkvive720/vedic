from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

class FulfillmentRequest(BaseModel):
    session: str
    queryResult: dict
    originalDetectIntentRequest: dict




# fil=

# # class FulfillmentRequest(BaseModel):
# #     session: str
# #     queryResult: dict
# #     originalDetectIntentRequest: dict

@app.post("/")
async def webhook(request: Request):
    data = await request.json()
    fulfillment_request = FulfillmentRequest(**data)
    
    context= fulfillment_request.queryResult["outputContexts"][2]['parameters']
    
    
    # result_of_query=data["queryResult"]
    # =data
    
    # options=[context["op1"], context["options2"], context["option3"], context["option4"],context["option5"]]
    
    options=[context["op1"],context["op2"],context["op3"],context["op4"],context["op5"],context["op6"],context["op7"],context["op8"],context["op9"],context["op10"]]
    
    a=0
    b=0
    c=0
    
    for i in range(10):
        
        if(options[i]=="A"):
            a+=1
        if(options[i]=="B"):
            b+=1
        if(options[i]=="C"):
            c+=1
            
    ap=a*100/(a+b+c)
    bp=b*100/(a+b+c)
    cp=c*100/(a+b+c)
    
    
    
            
            
    text_response=f"you have vata {ap} % \npitta {bp} %  \n and kapha {cp} % "
    # text_response=str(fulfillment_request)
    
    # text_response=str(context)
    
        
    
    
    
    
    
    text_res="connected to server"
    
    return JSONResponse(content={
  "fulfillmentText": text_response,
  "source": "my-webhook-service",
  "payload": {
    "google": {
      "expectUserResponse": False
    }
  }
}
)
        
    
