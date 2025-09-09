from datetime import datetime
from datetime import timedelta
def add(moment):
    print(moment)
    GIGA_SECONDS = 1_000_000_000
    dt = moment
    new_dt= dt + timedelta(seconds= GIGA_SECONDS)
    print(new_dt)
    return new_dt
