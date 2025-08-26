# Encrypta il file cryptocode.py per offuscare il code.

import base64

code = open("cryptocode.py", "r")
new_code = open("encrypted.py", "w")

cc = code.read().encode()
encoded = base64.b64encode(cc)

print(f"[-] Applicazione criptata: \n", encoded)

newcode_str = f"import base64;exec(base64.b64decode(b'{encoded.decode()}'))"

new_code.write(newcode_str)