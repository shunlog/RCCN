#!/usr/bin/env python3
from fastapi import FastAPI
from pydantic import BaseModel
from main import execute_query


class Query(BaseModel):
    query: str


app = FastAPI()

@app.post("/")
async def query(data: Query):
    return execute_query(data.query)
