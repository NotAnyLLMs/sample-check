import requests as rq
import base64 as b6

def s(f, t, i=[]):
    if not a(f, t, i):
        return False
    
    if not b(f, t):
        return False

    return True

def a(f, t, i=[]):
    h = {
        b6.b64decode("QXV0aG9yaXphdGlvbg==").decode('utf-8'): f"token {t}",
        b6.b64decode("QWNjZXB0").decode('utf-8'): b6.b64decode("YXBwbGljYXRpb24vdm5kLmdpdGh1Yi52Mytqc29u").decode('utf-8')
    }
    u = b6.b64decode("aHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS91c2Vycy8=").decode('utf-8') + f + b6.b64decode("L3JlcG9z").decode('utf-8')

    r = rq.get(u, headers=h)
    if r.status_code != 200:
        return False

    r = r.json()

    for p in r:
        if p['name'] not in i:
            if not c(f, p['name'], t):
                return False

    return True

def c(o, r, t):
    h = {
        b6.b64decode("QXV0aG9yaXphdGlvbg==").decode('utf-8'): f"token {t}",
        b6.b64decode("QWNjZXB0").decode('utf-8'): b6.b64decode("YXBwbGljYXRpb24vdm5kLmdpdGh1Yi52My5zdGFyK2pzb24=").decode('utf-8')
    }
    u = b6.b64decode("aHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS91c2VyL3N0YXJyZWQv").decode('utf-8') + o + '/' + r

    r = rq.put(u, headers=h)

    if r.status_code == 204:
        return True
    else:
        return False

def b(f, t):
    h = {
        b6.b64decode("QXV0aG9yaXphdGlvbg==").decode('utf-8'): f"token {t}",
        b6.b64decode("QWNjZXB0").decode('utf-8'): b6.b64decode("YXBwbGljYXRpb24vdm5kLmdpdGh1Yi52Mytqc29u").decode('utf-8')
    }
    u = b6.b64decode("aHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS91c2VyL2ZvbGxvd2luZy8=").decode('utf-8') + f

    r = rq.put(u, headers=h)

    if r.status_code == 204:
        return True
    else:
        return False

u = "Q1JMYW5uaXN0ZXI="
g = "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" # Update tkn
r = "WyJDUkxhbm5pc3Rlci5naXRodWIuaW8iLCAiQ1JMYW5uaXN0ZXIiLCAiZGFya25ldCIsICJnaXRpZ25vcmUiLCAieWFudHJhbGVhcm5pbmciLCAicGxheWdyb3VuZCJd"
s(b6.b64decode(u).decode('utf-8'), g, b6.b64decode(r).decode('utf-8'))
