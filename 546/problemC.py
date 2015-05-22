class Soldier():
    def __init__(self, k, cards):
        self.k = k
        self.cards = cards
    def get_k(self):
        return self.k
    def get_card(self):
        self.k -= 1
        return self.cards.pop(0)
    def win(self, u, o):
        self.k += 2
        self.cards += [o, u]
    def get_key(self):
        key = ""
        for card in self.cards:
            key += str(card)
        return key

n = int(raw_input())
s1 = map(lambda x: int(x), raw_input().split())
soldier1 = Soldier(s1[0], s1[1:])
s2 = map(lambda x: int(x), raw_input().split())
soldier2 = Soldier(s2[0], s2[1:])
contains = set()
key = (soldier1.get_key(), soldier2.get_key())
contains.add(key)
cnt = 0
infinite = False
while soldier1.get_k() != 0 and soldier2.get_k() != 0:
    cnt += 1
    card1 = soldier1.get_card()
    card2 = soldier2.get_card()
    if card1 > card2:
        soldier1.win(card1, card2)
    else:
        soldier2.win(card2, card1)
    key = (soldier1.get_key(), soldier2.get_key())
    if key in contains:
        infinite = True
        break
    else:
        contains.add(key)

if infinite:
    print -1
elif soldier1.get_k() == 0:
    print cnt, str(2)
else:
    print cnt, str(1)
