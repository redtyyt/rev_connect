# Encrypta il file cryptocode.py per offuscare il code.

import base64, os, argparse

parser = argparse.ArgumentParser()
parser.add_argument("--debug", dest="debug", type=bool)
args = parser.parse_args()

debug = args.debug

code = open("cryptocode.py", "r")
new_code = open("encrypted.pyw", "w")
nn = open("encrypted.py", "w")

cc = code.read().encode()
encoded = base64.b64encode(cc)

print(f"[-] MID-UPDATE: \n", encoded)

print(f"\nWrote file {new_code}")
newcode_str = f"import base64;exec(base64.b64decode(b'{encoded.decode()}'))"

new_code.write(newcode_str)
nn.write(newcode_str)

print(f"\n[-] Working on nuitka to convert it to .exe...")

if debug:
    out = os.system("nuitka --onefile --standalone encrypted.py")
else:
    out = os.system("nuitka --onefile --standalone --windows-console-mode=disable encrypted.pyw")
if out != 0:
    print("[!] Error while trying to use NUITKA.")

print("[-] Finalizing...")

code.close()
new_code.close()

print("[!] Process ended.")