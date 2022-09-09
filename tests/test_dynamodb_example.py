from msilib import Table
import unittest
import boto3
from moto import mock_dynamodb
from botocore.exceptions import ParamValidationError
from src.boto3_example import DynamodBExample

model_instance = DynamodBExample()

@mock_dynamodb
class TestDBFunctions(unittest.TestCase):

    def test_create_dynamo_table(self):
        '''
            Implement the test logic here for testing create_dynamo_table method
        '''
        self.conn = boto3.resource('dynamodb', region_name='us-east-1')
        self.table = self.conn.Table('Movies')
        self.assertIn('Movies', self.table.name)
        

    def test_add_dynamo_record_table(self):
        '''
            Implement the test logic here for testing add_dynamo_record_table method
        '''
        self.conn = boto3.resource('dynamodb', region_name='us-east-1')
        result = model_instance.add_dynamo_record('Movies', {'S':'The Big New Movie'})
        self.assertEqual(200, result['HTTPStatusCode'])



    def test_add_dynamo_record_table_failure(self):
        '''
            Implement the test logic here test_add_dynamo_record_table method for failures
        '''
        self.conn = boto3.resource('dynamodb', region_name = 'us-east-1')
        with self.assertRaises(ParamValidationError) as excep:
            model_instance.add_dynamo_record('Movies', "The Big New Movie")

if __name__ == '__main__':
    unittest.main()

