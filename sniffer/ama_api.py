import subprocess

__dll = 'tools/CCSniff.exe'

def run_command(args):
    result = subprocess.run(
        [__dll] + args,
        capture_output=True,
        text=False
    )

    output = result.stdout.decode('latin-1')    
    return output.strip()

def get_info():
    return run_command(["info"])

def get_address_info(code: str):
    return run_command(["address", "--code", code])

def sign_document(code: str, path: str, out: str):
    return run_command(["sign", "--code", code, "--path", path, "--out", out])