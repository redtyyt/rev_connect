# Encrypta il file cryptocode.py per offuscare il code.

import base64, os

code = open("cryptocode.py", "r")
new_code = open("encrypted.pyw", "w")

cc = code.read().encode()
encoded = base64.b64encode(cc)

print(f"[-] MID-UPDATE: \n", encoded)

print(f"\nWrote file {new_code}")
newcode_str = f"import base64;exec(base64.b64decode(b'{encoded.decode()}'))"

new_code.write(newcode_str)

print(f"\n[-] Working on easycython to convert it to .pyd...")

out = os.system("easycython *.pyx")

if out != 0:
    print("[!] Error while trying to use easycython.")

print("[-] Finalizing...")

code.close()
new_code.close()

print("[!] Process ended.")