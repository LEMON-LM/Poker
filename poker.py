import random

def all_hands(numhands,numcards,deck = [r+s for r in '23456789TJQKA' for s in 'SHDC']):
	random.shuffle(deck)
	return [deck[numhands*i:numhands*(i+1)] for i in range(numcards)]

def card_ranks(hand):
	ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
	ranks.sort(reverse = True)
	return [5,4,3,2,1] if ranks == [14,5,4,3,2] else ranks

def hand_rank(hand):
	ranks = card_ranks(hand)
	if straight(ranks) and flush(hand):
		return(8,max(ranks))
	elif kind(4,ranks):
		return(7,kind(4,ranks),kind(1,ranks))
	elif kind(3,ranks) and kind(2,ranks):
		return(6,kind(3,ranks),kind(2,ranks))
	elif flush(hand):
		return(5,ranks)
	elif straight(ranks):
		return(4,max(ranks))
	elif kind(3,ranks):
		return(3,kind(3,ranks),ranks)
	elif two_pairs(ranks):
		return(2,two_pairs(ranks),ranks)
	elif kind(2,ranks):
		return(1,kind(2,ranks),ranks)
	else:
		return (0,ranks)		

def straight(ranks):
	return(max(ranks) - min(ranks) == 4) and (len(set(ranks))==5)

def flush(hand):
	suits = [s for r,s in hand]
	return len(set(suits))==1

def kind(n,ranks):
	for r in ranks:
		if ranks.count(r) == n:
			return r
	return None
def two_pairs(ranks):
	pair = kind(2,ranks)
	lowpair = kind(2,list(reversed(ranks)))
	if pair and lowpair != pair:
		return(pair,lowpair)
	else:
		return None

def poker(hands):
	return allmax(hands,key = hand_rank)
	
def allmax(hands,key=None):
	result,maxval = [],None
	key = key or (lambda x:x)
	for x in hands:
		xval = key (x)
		print(xval)
		if not result or xval > maxval:
			result,maxval = [x],xval
		elif xval == maxval:
			result.append(x)
	print(result)
	return result



numhands = 5
numcards = 5
allhands = all_hands(numhands,numcards)
for hand in allhands:
	print(hand)
print(poker(allhands))