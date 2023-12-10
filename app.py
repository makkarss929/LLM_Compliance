from fastapi import Request
from src.helper import LLMCompliance
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import uvicorn
from typing import Optional, Union
from pydantic import BaseModel
import os


class LLMComplianceSchema(BaseModel):
    pages: dict
    compliance_rules: str


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

obj = LLMCompliance()

@app.get("/")
def hello():
    return "Welcome to LLM Compliance API"


@app.post("/non_compliance")
def handler(body: LLMComplianceSchema, request: Request):
    results = obj.pipeline(body.pages, body.compliance_rules)
    return results


if __name__ == '__main__':
    uvicorn.run(app, port=5001, host="0.0.0.0")