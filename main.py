from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Existing routes...

@app.get("/", response_class=HTMLResponse)
async def serve_html(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



class model_input(BaseModel):
    Gender: int
    Married: int
    Dependents: int
    Education: int
    Self_Employed: int
    ApplicantIncome: int
    CoapplicantIncome: int
    LoanAmount: int
    Loan_Amount_Term: int
    Credit_History: int
    Property_Area: int    

# loading the saved model
loan_model = pickle.load(open('loan_ml_model.sav', 'rb'))

@app.get("/sample")
def get_sample():
    return {"message": "This is a sample response from FastAPI!"}

@app.post('/loan_prediction')
def loan_predd(input_parameters: model_input) -> str:
    input_dict = input_parameters.dict()

    Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area = [
        input_dict[key] for key in input_dict.keys()
    ]

    input_list = [Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area]

    prediction = loan_model.predict([input_list])

    if prediction[0] == 0:
        return 'The person is not Applicable for loan'
    else:
        return 'The person is Applicable for loan'
