from .context import src

import unittest


class DatabaseConnectorTestSuite(unittest.TestCase):
    ''' Testing the databaseConnector component in the databaseAPI module
    '''

    def setUp(self):
        self.connector = src.databaseAPI.databaseConnector.Connector

    def testGetConnectionForRealConnection(self):
        ''' Assumes that connection parameters are correct
        '''
        self.assertIsNotNone(self.connector.getConnection())


if __name__ == '__main__':
    unittest.main()