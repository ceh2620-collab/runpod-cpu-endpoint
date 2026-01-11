import runpod

def handler(event):
    return {"status": "OK", "message": "CPU endpoint running"}

runpod.serverless.start({"handler": handler})
