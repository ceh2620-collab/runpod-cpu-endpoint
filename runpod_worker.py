import runpod

def handler(event):
    return { "message": "CPU endpoint OK" }

runpod.serverless.start({"handler": handler})
