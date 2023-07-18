detect_trigger = {
    "inside": lambda x, m: x in m,
    "start": lambda x, m: m.startswith(x),
    "only": lambda x, m: x == m,
}


