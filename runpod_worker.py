import runpod
from main import handler

runpod.serverless.start({"handler": handler})
