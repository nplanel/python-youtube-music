from .is_float import is_float

__all__ = __name__.split('.')[-1:]

def parse_fflags(fflags: dict) -> dict:
    new_fflags = {}

    for fflag_key, fflag_val in fflags.items():
        js_types = \
        {
            'true': True,
            'false': False,
            'null': None,
        }

        if fflag_val in js_types:
            fflag_val = js_types[fflag_val]
        elif fflag_val.isdigit():
            fflag_val = int(fflag_val)
        elif is_float(fflag_val):
            fflag_val = float(fflag_val)

        new_fflags[fflag_key] = fflag_val

    return new_fflags
