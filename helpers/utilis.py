import uuid


def generate_code():
    code = uuid.uuid4()
    code_mod = str(code).replace("-", "")[:12].upper()
    print(code_mod)
    return code_mod
