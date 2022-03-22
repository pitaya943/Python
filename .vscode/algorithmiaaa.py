# coding:utf-8
import Algorithmia
import os
import sys
sys.path.append('./myEnv/lib/python3.9/site-packages')

input = {
    "image": "data://pitaya943/pic/pic.jpg"
}
client = Algorithmia.client('simalbFfCl800PlcCXwIOcmmRuL1')
algo = client.algo('deeplearning/ColorfulImageColorization/1.1.14')
algo.set_options(timeout=300)  # optional
print(algo.pipe(input).result)
