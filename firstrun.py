import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import sys

model_name = "infly/OpenCoder-8B-Instruct"
model = AutoModelForCausalLM.from_pretrained(model_name,
                                             torch_dtype=torch.bfloat16,
                                             device_map="auto",
                                             trust_remote_code=True)
