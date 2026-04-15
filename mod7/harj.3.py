#heitetään noppaa monikon avulla

import random

def heitto():
    eka = random.randint(1,6)
    toka = random.randint(1,6)
    return (eka, toka)

noppa1, noppa2 = heitto()

print(f"Saatiin luvut {noppa1} ja {noppa2}. Liikutaan eteenpäin yhteensä {noppa1 + noppa2} askelta.")
      