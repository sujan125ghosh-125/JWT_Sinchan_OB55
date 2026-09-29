###Hey baby 🍼 If you leak this file under your own name and claim the credit, I'll fuck you with salt. 🥱


import time
import json
import base64
import os
import hashlib
import hmac
import threading
import time
from datetime import datetime, timezone

import httpx
from flask import Flask, request, jsonify
from flask_cors import CORS
from Crypto.Cipher import AES


from google.protobuf import json_format
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
from google.protobuf.message import Message


# ============================================================
#  PART 1 — FreeFire_pb2 (inlined)
# ============================================================

_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC, 6, 30, 0, "", "FreeFire.proto",
)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0e\x46reeFire.proto"c\n\x08LoginReq\x12\x0f\n\x07open_id\x18\x16 \x01(\t'
    b'\x12\x14\n\x0copen_id_type\x18\x17 \x01(\t\x12\x13\n\x0blogin_token\x18\x1d '
    b'\x01(\t\x12\x1b\n\x13orign_platform_type\x18\x63 \x01(\t"]\n\x10\x42lacklist'
    b'InfoRes\x12\x1e\n\nban_reason\x18\x01 \x01(\x0e\x32\n.BanReason\x12\x17\n'
    b'\x0f\x65xpire_duration\x18\x02 \x01(\r\x12\x10\n\x08\x62\x61n_time\x18\x03 '
    b'\x01(\r"f\n\x0eLoginQueueInfo\x12\r\n\x05\x61llow\x18\x01 \x01(\x08\x12'
    b'\x16\n\x0equeue_position\x18\x02 \x01(\r\x12\x16\n\x0eneed_wait_secs\x18'
    b'\x03 \x01(\r\x12\x15\n\rqueue_is_full\x18\x04 \x01(\x08"\xa0\x03\n\x08'
    b'LoginRes\x12\x12\n\naccount_id\x18\x01 \x01(\x04\x12\x13\n\x0block_region'
    b'\x18\x02 \x01(\t\x12\x13\n\x0bnoti_region\x18\x03 \x01(\t\x12\x11\n\tip_'
    b'region\x18\x04 \x01(\t\x12\x19\n\x11\x61gora_environment\x18\x05 \x01(\t'
    b'\x12\x19\n\x11new_active_region\x18\x06 \x01(\t\x12\x19\n\x11recommend_'
    b'regions\x18\x07 \x03(\t\x12\r\n\x05token\x18\x08 \x01(\t\x12\x0b\n\x03ttl'
    b'\x18\t \x01(\r\x12\x12\n\nserver_url\x18\n \x01(\t\x12\x16\n\x0e\x65mul'
    b'ator_score\x18\x0b \x01(\r\x12$\n\tblacklist\x18\x0c \x01(\x0b\x32\x11.'
    b'BlacklistInfoRes\x12#\n\nqueue_info\x18\r \x01(\x0b\x32\x0f.LoginQueue'
    b'Info\x12\x0e\n\x06tp_url\x18\x0e \x01(\t\x12\x15\n\rapp_server_id\x18'
    b'\x0f \x01(\r\x12\x0f\n\x07\x61no_url\x18\x10 \x01(\t\x12\x0f\n\x07ip_city'
    b'\x18\x11 \x01(\t\x12\x16\n\x0eip_subdivision\x18\x12 \x01(\t*\xa8\x01\n'
    b'\tBanReason\x12\x16\n\x12\x42\x41N_REASON_UNKNOWN\x10\x00\x12\x1b\n\x17'
    b'\x42\x41N_REASON_IN_GAME_AUTO\x10\x01\x12\x15\n\x11\x42\x41N_REASON_'
    b'REFUND\x10\x02\x12\x15\n\x11\x42\x41N_REASON_OTHERS\x10\x03\x12\x16\n'
    b'\x12\x42\x41N_REASON_SKINMOD\x10\x04\x12 \n\x1b\x42\x41N_REASON_IN_GAME'
    b'_AUTO_NEW\x10\xf6\x07\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "FreeFire_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals["_BANREASON"]._serialized_start = 738
    _globals["_BANREASON"]._serialized_end = 906
    _globals["_LOGINREQ"]._serialized_start = 18
    _globals["_LOGINREQ"]._serialized_end = 117
    _globals["_BLACKLISTINFORES"]._serialized_start = 119
    _globals["_BLACKLISTINFORES"]._serialized_end = 212
    _globals["_LOGINQUEUEINFO"]._serialized_start = 214
    _globals["_LOGINQUEUEINFO"]._serialized_end = 316
    _globals["_LOGINRES"]._serialized_start = 319
    _globals["_LOGINRES"]._serialized_end = 735

LoginReq = _globals["LoginReq"]
LoginRes = _globals["LoginRes"]


# ============================================================
#  PART 2 — Settings
# ============================================================

MAIN_KEY = base64.b64decode("WWcmdGMlREV1aDYlWmNeOA==")
MAIN_IV = base64.b64decode("Nm95WkRyMjJFM3ljaGpNJQ==")
RELEASEVERSION = "OB55"
USERAGENT = "UnityPlayer/2018.4.12f1 (UnityWebRequest/1.0, libcurl/8.5.0-DEV)"
LOGIN_URL = "https://loginbp.ppmainecoonghj.com/"

# Fast HTTP client (connection pooling + keep-alive)
HTTP_LIMITS = httpx.Limits(max_keepalive_connections=20, max_connections=50)
HTTP_TIMEOUT = httpx.Timeout(15.0, connect=5.0)
_http_client = httpx.Client(limits=HTTP_LIMITS, timeout=HTTP_TIMEOUT)


# ============================================================
#  PART 3 — Flask App
# ============================================================

app = Flask(__name__)
CORS(app)


# ============================================================
#  PART 3A — UID request log storage
# ============================================================
# Never store the supplied password in plaintext. We keep a
# deterministic HMAC fingerprint so the same uid+password pair
# can be detected without putting the actual password in GitHub.
#
# Termux: if UID_LOG_SECRET is not set, a local .uid_secret file
# is created automatically.
# Vercel: set UID_LOG_SECRET in Environment Variables.

LOCAL_UID_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "uid.json")
LOCAL_SECRET_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".uid_secret")
UID_LOG_PATH = os.getenv("UID_LOG_PATH", "uid.json").strip("/") or "uid.json"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "").strip()
GITHUB_REPO = os.getenv("GITHUB_REPO", "").strip()  # owner/repository
GITHUB_BRANCH = os.getenv("GITHUB_BRANCH", "main").strip() or "main"
GITHUB_API_VERSION = "2026-03-10"
_uid_file_lock = threading.Lock()


def _get_log_secret() -> bytes:
    secret = os.getenv("UID_LOG_SECRET", "").strip()
    if secret:
        return secret.encode("utf-8")

    # Local/Termux fallback. This file must NOT be committed to GitHub.
    if os.path.exists(LOCAL_SECRET_FILE):
        value = open(LOCAL_SECRET_FILE, "r", encoding="utf-8").read().strip()
        if value:
            return value.encode("utf-8")

    value = base64.urlsafe_b64encode(os.urandom(32)).decode("ascii")
    try:
        with open(LOCAL_SECRET_FILE, "w", encoding="utf-8") as f:
            f.write(value)
        try:
            os.chmod(LOCAL_SECRET_FILE, 0o600)
        except OSError:
            pass
    except OSError:
        # Vercel without UID_LOG_SECRET cannot reliably fingerprint data.
        raise RuntimeError("UID_LOG_SECRET is required when persistent local storage is unavailable")
    return value.encode("utf-8")


def _credential_fingerprint(uid: str, password: str) -> str:
    value = f"{uid}\0{password}".encode("utf-8")
    return hmac.new(_get_log_secret(), value, hashlib.sha256).hexdigest()


def _read_local_uid_file():
    if not os.path.exists(LOCAL_UID_FILE):
        return []
    try:
        with open(LOCAL_UID_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, list) else []
    except (OSError, json.JSONDecodeError):
        return []


def _write_local_uid_file(entries):
    tmp = LOCAL_UID_FILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(entries, f, indent=2, ensure_ascii=False)
    os.replace(tmp, LOCAL_UID_FILE)


def _github_configured() -> bool:
    return bool(GITHUB_TOKEN and GITHUB_REPO and "/" in GITHUB_REPO)


def _github_headers():
    return {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "X-GitHub-Api-Version": GITHUB_API_VERSION,
        "User-Agent": "uid-token-api",
    }


def _github_get_uid_file():
    url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{UID_LOG_PATH}"
    resp = _http_client.get(url, headers=_github_headers(), params={"ref": GITHUB_BRANCH})
    if resp.status_code == 404:
        return [], None
    resp.raise_for_status()
    payload = resp.json()
    encoded = payload.get("content", "").replace("\n", "")
    if not encoded:
        return [], payload.get("sha")
    raw = base64.b64decode(encoded).decode("utf-8")
    data = json.loads(raw)
    return (data if isinstance(data, list) else []), payload.get("sha")


def _github_write_uid_file(entries, sha=None):
    url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{UID_LOG_PATH}"
    raw = json.dumps(entries, indent=2, ensure_ascii=False).encode("utf-8")
    body = {
        "message": "Update uid.json",
        "content": base64.b64encode(raw).decode("ascii"),
        "branch": GITHUB_BRANCH,
    }
    if sha:
        body["sha"] = sha
    resp = _http_client.put(url, headers=_github_headers(), json=body)
    if resp.status_code == 409:
        return False
    resp.raise_for_status()
    return True


def save_uid_request(uid: str, password: str):
    fingerprint = _credential_fingerprint(uid, password)

    with _uid_file_lock:
        # Vercel/GitHub mode. GitHub Contents API supports create/update
        # with the current file SHA.
        if _github_configured():
            for _ in range(3):
                entries, sha = _github_get_uid_file()
                if any(
                    item.get("uid") == uid and
                    item.get("password_fingerprint") == fingerprint
                    for item in entries if isinstance(item, dict)
                ):
                    return {"saved": False, "duplicate": True}

                now = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
                entries.append({
                    "uid": str(uid),
                    "password_fingerprint": fingerprint,
                    "created_at": now,
                })
                try:
                    if _github_write_uid_file(entries, sha):
                        return {"saved": True, "duplicate": False}
                except Exception:
                    raise
            raise RuntimeError("GitHub uid.json update conflict; please retry")

        # Termux/local mode.
        entries = _read_local_uid_file()
        if any(
            item.get("uid") == uid and
            item.get("password_fingerprint") == fingerprint
            for item in entries if isinstance(item, dict)
        ):
            return {"saved": False, "duplicate": True}

        now = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
        entries.append({
            "uid": str(uid),
            "password_fingerprint": fingerprint,
            "created_at": now,
        })
        _write_local_uid_file(entries)
        return {"saved": True, "duplicate": False}


# ============================================================
#  PART 4 — Helpers
# ============================================================

def pad(text: bytes) -> bytes:
    padding_length = AES.block_size - (len(text) % AES.block_size)
    return text + bytes([padding_length] * padding_length)


def aes_cbc_encrypt(key: bytes, iv: bytes, plaintext: bytes) -> bytes:
    return AES.new(key, AES.MODE_CBC, iv).encrypt(pad(plaintext))


def json_to_proto(json_data: str, proto_message: Message) -> bytes:
    json_format.ParseDict(json.loads(json_data), proto_message)
    return proto_message.SerializeToString()


def try_parse_login_res(data: bytes):
    try:
        msg = LoginRes()
        msg.ParseFromString(data)
        if msg.account_id and msg.account_id > 0:
            return json.loads(json_format.MessageToJson(msg))
    except Exception:
        pass
    return None


def extract_login_res(raw: bytes) -> dict:
    # Attempt 1: from index 0
    parsed = try_parse_login_res(raw)
    if parsed:
        return parsed

    # Attempt 2: scan each \x08
    idx = 0
    while True:
        idx = raw.find(b"\x08", idx)
        if idx == -1:
            break
        parsed = try_parse_login_res(raw[idx:])
        if parsed:
            return parsed
        idx += 1

    # Attempt 3: JWT marker prefix
    jwt_marker = raw.find(b"eyJhbGciOiJIUzI1NiIs")
    if jwt_marker != -1:
        for i in range(jwt_marker - 1, max(jwt_marker - 300, -1), -1):
            if raw[i] == 0x42:
                parsed = try_parse_login_res(raw[i:])
                if parsed:
                    return parsed
                break

    raise Exception(f"Could not parse LoginRes. Raw: {raw[:200]}")


def get_access_token(account: str):
    url = "https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant"
    payload = (
        account
        + "&response_type=token&client_type=2"
        + "&client_secret=2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3"
        + "&client_id=100067"
    )
    headers = {
        "User-Agent": USERAGENT,
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    resp = _http_client.post(url, data=payload, headers=headers)
    data = resp.json()
    return data.get("access_token", "0"), data.get("open_id", "0")


def generate_jwt_token(uid: str, password: str):
    start_time = time.time()

    token_val, open_id = get_access_token(f"uid={uid}&password={password}")
    if token_val == "0" or open_id == "0":
        raise Exception("Invalid UID or Password — access token not received")

    body = json.dumps({
        "open_id": open_id,
        "open_id_type": "4",
        "login_token": token_val,
        "orign_platform_type": "4",
    })
    proto_bytes = json_to_proto(body, LoginReq())
    payload = aes_cbc_encrypt(MAIN_KEY, MAIN_IV, proto_bytes)

    headers = {
        "User-Agent": USERAGENT,
        "Accept": "*/*",
        "Accept-Encoding": "deflate, gzip",
        "X-Ga-Sv": "1789534056",
        "Authorization": "Bearer",
        "X-Ga": "v1 1",
        "Releaseversion": RELEASEVERSION,
        "Content-Type": "application/x-www-form-urlencoded",
        "X-Unity-Version": "2018.4.12f1",
        "PlAy_VeR": "1.132.1",
        "Ob_VeR": RELEASEVERSION,
    }

    resp = _http_client.post(f"{LOGIN_URL}MajorLogin", data=payload, headers=headers)
    msg = extract_login_res(resp.content)

    elapsed = time.time() - start_time
    now = datetime.now(timezone.utc)
    create_time = now.isoformat(timespec="seconds").replace("+00:00", "Z")
    timestamp = int(now.timestamp())


    return {
        "access_token": token_val,
        "open_id": open_id,
        "real_uid": str(msg.get("accountId", "")),
        "status": "success",
        "time": f"{elapsed:.2f}s",
        "timestamp":    create_time,       
        "create_time":  timestamp,
        "token": f"{msg.get('token', '')}",
    }


# ============================================================
#  PART 5 — Routes
# ============================================================

@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "status": "ok",
        "endpoint": "/token?uid=UID&password=PASS",
        "example": "/token?uid=18097039025&password=yourpass",
    }), 200


@app.route("/token", methods=["GET"])
def get_jwt_token():
    uid = request.args.get("uid")
    password = request.args.get("password")

    if not uid or not password:
        return jsonify({
            "status": "error",
            "error": "Both uid and password parameters are required"
        }), 400

    try:
        token_data = generate_jwt_token(uid, password)

        # Save only after successful token generation. The password itself
        # is never written to uid.json; only a keyed fingerprint is stored.
        try:
            token_data["credential_log"] = save_uid_request(uid, password)
        except Exception as log_error:
            # Do not expose credentials or GitHub secrets in the API response.
            token_data["credential_log"] = {
                "saved": False,
                "error": "Credential log storage failed"
            }
            app.logger.error("UID log storage failed: %s", log_error)

        return jsonify(token_data), 200
    except Exception as e:
        return jsonify({
            "status": "error",
            "error": f"Failed to generate token: {str(e)}"
        }), 500


# ============================================================
#  ENTRY POINT
# ============================================================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=False)
    
    
### Hey baby 🍼 If you leak this file under your own name and claim the credit, I'll fuck you with salt. 🥱
