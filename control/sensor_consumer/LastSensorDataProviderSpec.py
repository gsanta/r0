import unittest
from LastSensorDataProvider import LastSensorDataProvider

class LastSensorDataProviderSpec(unittest.TestCase):
    
    def testAddData(self):
        provider = LastSensorDataProvider()
        provider.addData(5)
        self.assertTrue(provider.popData() == 5)

    def testPopDataSetsDataToNone(self):
        provider = LastSensorDataProvider()
        provider.addData(5)

        provider.popData()
        data = provider.popData()
        self.assertTrue(data == None)

if __name__ == '__main__':
    unittest.main()
