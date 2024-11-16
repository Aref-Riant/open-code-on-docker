import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import sys

torch.set_num_threads(8)
torch.set_num_interop_threads(8)

model_name = "infly/OpenCoder-8B-Instruct"
model = AutoModelForCausalLM.from_pretrained(model_name,
                                             torch_dtype=torch.bfloat16,
                                             device_map="auto",
                                             trust_remote_code=True)

if len(sys.argv) > 1:
  tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)

  messages=[
      { 'role': 'user', 'content': " ".join(sys.argv[1:]) }
  ]

  inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt")

  outputs = model.generate(inputs, max_new_tokens=512, do_sample=False)

  result = tokenizer.decode(outputs[0][len(inputs[0]):], skip_special_tokens=True)
  print(result)
