def flatten_metrics(raw_section):
    flat = {}
    for item in raw_section:
        flat.update(item)
    return flat
