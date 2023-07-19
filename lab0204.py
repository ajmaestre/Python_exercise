
import numpy as np
import pandas as pd
import itertools


def create_deck(n_heaps, cards_per_heap, shuffle=False):
    n_cards = n_heaps * cards_per_heap
    
    chars = [chr(i) for i in np.arange(26)+65]
    names = [i+j for i,j in itertools.product(chars, chars)]    

    assert n_cards < len(names), "cannot have more than %d cards"%len(name)
    
    c = np.r_[names[:n_cards]]
    if shuffle:
        c = np.random.permutation(c)
    return c

print()

def pick_card(c):
    return np.random.choice(c)

c = create_deck(n_heaps=3, cards_per_heap=7, shuffle=True)
n = pick_card(c)
print(n)
print()

# ------------------------------------------------ TASK 1 -----------------------------------------

def make_heaps(c, n_heaps=3):
    assert n_heaps%2==1, "must have an odd number of heaps"
    assert len(c)%n_heaps==0, "the length of the deck must be a multiple of the number of heaps"
    h = np.transpose(c.reshape(len(c)//n_heaps, -n_heaps))
    return h.tolist()

n_heaps = 3
c = create_deck(n_heaps=n_heaps, cards_per_heap=7)

h = make_heaps(c, n_heaps)

print("deck", c)
print("heaps", h)


# ------------------------------------------------------------ TASK 2 --------------------------------------

def collect_heaps(h, n):
    print()
    [a] = np.where(np.array(h) == n)[0]
    b = h[len(h)//2]
    h[len(h)//2] = h[a]
    h[a] = b
    h = np.array(h)
    r = h.flatten()
    
    return r.tolist()


n_heaps = 3
c = create_deck(n_heaps=n_heaps, cards_per_heap=7, shuffle=True)
n = pick_card(c)
print ("card picked", n)
h = make_heaps(c, n_heaps)
print(h)

new_c = collect_heaps(h, n)
print (new_c)


# --------------------------------------------------------- TASK 3 ---------------------------------------------

def run(c, n, n_heaps=3):
    print()
    for i in range(3):
        h = make_heaps(c, n_heaps)
        c = np.array(collect_heaps(h, n))
    print()

    [r] = np.where(c == n)[0]

    return r

n_heaps = 3
c = create_deck(n_heaps=n_heaps, cards_per_heap=7)
picked = "AA"
print ("desk", c)
pos = run(c, picked, n_heaps=n_heaps)
print ("position of card %s is %d"%(picked, pos))


# ------------------------------------------------- TASK 4 -----------------------------------------

def mrun(c, picked_card, n_heaps=3):
    assert len(c)%n_heaps==0, "the number of heaps must be a divisor of the deck length"
    
    ch = len(c)//n_heaps # cards per heap
    nh = n_heaps
    
    i = np.where(c == picked_card)[0][0] # initial position of the card on the deck c
    p1 = (ch*(nh//2)) + (i//nh)  # the position of the card after the first round
    p2 = (ch*(nh//2)) + (p1//nh)  # the position of the card after the second round
    p3 = (ch*(nh//2)) + (p2//nh)  # the position of the card after the last round
    
    return p3

n_heaps = 3
c = create_deck(n_heaps=n_heaps, cards_per_heap=4)
picked = "AI"
print ("deck", c)
pos = mrun(c, picked, n_heaps=n_heaps)
print ("position of card %s is %d"%(picked, pos))