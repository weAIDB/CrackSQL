# -*- coding: utf-8 -*-
# @Project: xxxx
# @Module: llm_service
# @Author: xxxx
# @Time: 2024/9/24 14:26

import time
import uuid
import argparse

import torch
import transformers

import uvicorn
import tiktoken
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

app = FastAPI()


class CompletionRequest(BaseModel):
    model: str
    messages: list
    max_tokens: int = 4096
    do_sample: bool = False
    temperature: float = 0.01


class CompletionResponse(BaseModel):
    id: str
    object: str = "chat.completion"
    created: int
    model: str
    choices: list
    usage: dict


def init_model(model_id):
    pipeline = transformers.pipeline(
        "text-generation",
        model=model_id,
        model_kwargs={"torch_dtype": torch.bfloat16},
        device_map="auto"
    )

    return pipeline


def invoke_model(messages, max_new_tokens, do_sample, temperature):
    global pipeline

    outputs = pipeline(
        messages,
        max_new_tokens=max_new_tokens,
        do_sample=do_sample,
        temperature=temperature
    )

    return outputs[0]["generated_text"][-1]


def calculate_usage(prompt: str, completion: str, model: str = "gpt-4o"):
    encoding = tiktoken.encoding_for_model(model)
    prompt_tokens = len(encoding.encode(prompt))
    completion_tokens = len(encoding.encode(completion))
    total_tokens = prompt_tokens + completion_tokens
    return {
        "prompt_tokens": prompt_tokens,
        "completion_tokens": completion_tokens,
        "total_tokens": total_tokens,
        "prompt_tokens_details": None
    }


@app.post("/v1/chat/completions", response_model=CompletionResponse)
async def chat_completions_create(request: CompletionRequest):
    try:
        output_message = invoke_model(request.messages, request.max_tokens,
                                      request.do_sample, request.temperature)

        input_text = " ".join([msg["content"] for msg in request.messages if msg["content"]])
        output_text = output_message["content"]

        response_data = {
            "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, input_text + output_text)),
            "created": int(time.time()),
            "model": request.model,
            "choices": [
                {
                    "finish_reason": "stop",
                    "index": 0,
                    "message": output_message
                }
            ],
            "usage": calculate_usage(input_text, output_text)
        }

        return CompletionResponse(**response_data)

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='Startup LLM service.')

    parser.add_argument('--model_path', type=str,
                        help='Local model weight path')
    parser.add_argument('--host', type=str,
                        default='localhost', help='IP address of LLM service')
    parser.add_argument('--port', type=int,
                        help='Port of LLM service')

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    pipeline = init_model(args.model_path)

    uvicorn.run(app, host=args.host, port=args.port)
