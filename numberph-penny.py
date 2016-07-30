
import unittest
import random
import sys
import parser

def getCoinFlips(numberOfFlips):
	coinflips = ''
	outcomes = ['T', 'H']
	
	for i in range(numberOfFlips):
		coinflips += random.choice(outcomes)
	
	return coinflips


class baseTest(unittest.TestCase):

    def testGetCoinFlips_Trivial(self):
    	result = getCoinFlips(0)
    	self.assertEqual('', result)

    def testGetCoinFlips_ReturnsCorrectLength(self):
    	result = getCoinFlips(1)
    	self.assertEqual(1, len(result))

    	result = getCoinFlips(2)
    	self.assertEqual(2, len(result))

    	result = getCoinFlips(495)
    	self.assertEqual(495, len(result))


    def testGetCoinFlips_DifferentResults(self):
    	coinFlips1 = getCoinFlips(3)
    	coinFlips2 = getCoinFlips(3)
    	coinFlips3 = getCoinFlips(3)
    	
    	# 1/64 chance they will all match
    	self.assertFalse( coinFlips1 == coinFlips2 == coinFlips3)





DEBUG = False
if DEBUG:
	unittest.main()


print('Flipping 3 coins...')    
print(getCoinFlips(3))







