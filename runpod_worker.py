import runpod

def handler(event):
    return {"message": "hello"}

runpod.serverless.start({"handler": handler})
