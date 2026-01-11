from runpod.serverless import start

def handler(event):
    return {"message": "CPU endpoint OK"}

start({"handler": handler})
