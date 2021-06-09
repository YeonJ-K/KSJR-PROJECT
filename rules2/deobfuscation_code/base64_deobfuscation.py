import sys
import os
import base64


def deobfus_code(deobfuscation) :
    base64_str = deobfuscation
    base64_bytes = base64.b64decode(base64_str)
    result_deobfuscation = base64_bytes.decode('ascii')
    print(f"deobfuscation_result : " + result_deobfuscation)
