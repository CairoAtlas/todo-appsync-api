import json

from lambda_functions import reminders_dynamo_to_firehose as function_code

INSERT_RECORD = {
    'eventID': 'c4ca4238a0b923820dcc509a6f75849b',
    'eventName': 'INSERT',
    'eventVersion': '1.1',
    'eventSource': 'aws:dynamodb',
    'awsRegion': 'us-east-1',
    'dynamodb': {
        'Keys': {
            'title': {
                'S': 'Reminder 1'
            },
            'createdTimestamp': {
                'N': '1563140810'
            }
        },
        'NewImage': {
            'title': {
                'S': 'Reminder 1'
            },
            'createdTimestamp': {
                'N': '1563140810'
            }
        },
        'ApproximateCreationDateTime': 1428537600,
        'SequenceNumber': '4421584500000000017450439091',
        'SizeBytes': 26,
        'StreamViewType': 'NEW_AND_OLD_IMAGES'
    },
    'eventSourceARN': 'arn:aws:dynamodb:us-east-1:123456789012:table/ExampleTableWithStream/stream/2015-06-27T00:48:05.899'
}
MODIFY_RECORD = {
    'eventID': 'c81e728d9d4c2f636f067f89cc14862c',
    'eventName': 'MODIFY',
    'eventVersion': '1.1',
    'eventSource': 'aws:dynamodb',
    'awsRegion': 'us-east-1',
    'dynamodb': {
        'Keys': {
            'title': {
                'S': 'Reminder 1'
            },
            'createdTimestamp': {
                'N': '1563140810'
            }
        },
        'NewImage': {
            'title': {
                'S': 'Reminder 1'
            },
            'createdTimestamp': {
                'N': '1563140810'
            },
            'notes': {
                'S': 'new notes'
            }
        },
        'OldImage': {
            'title': {
                'S': 'Reminder 1'
            },
            'createdTimestamp': {
                'N': '1563140810'
            }
        },
        'ApproximateCreationDateTime': 1428537600,
        'SequenceNumber': '4421584500000000017450439092',
        'SizeBytes': 59,
        'StreamViewType': 'NEW_AND_OLD_IMAGES'
    },
    'eventSourceARN': 'arn:aws:dynamodb:us-east-1:123456789012:table/ExampleTableWithStream/stream/2015-06-27T00:48:05.899'
}
REMOVE_RECORD = {
    'eventID': 'eccbc87e4b5ce2fe28308fd9f2a7baf3',
    'eventName': 'REMOVE',
    'eventVersion': '1.1',
    'eventSource': 'aws:dynamodb',
    'awsRegion': 'us-east-1',
    'dynamodb': {
        'Keys': {
            'title': {
                'S': 'Reminder 1'
            },
            'createdTimestamp': {
                'N': '1563140810'
            }
        },
        'OldImage': {
            'title': {
                'S': 'Reminder 1'
            },
            'createdTimestamp': {
                'N': '1563140810'
            }
        },
        'ApproximateCreationDateTime': 1428537600,
        'SequenceNumber': '4421584500000000017450439093',
        'SizeBytes': 38,
        'StreamViewType': 'NEW_AND_OLD_IMAGES'
    },
    'eventSourceARN': 'arn:aws:dynamodb:us-east-1:123456789012:table/ExampleTableWithStream/stream/2015-06-27T00:48:05.899'
}


def test_build_firehose_record_insert():
    assert True


def test_build_firehose_record_modify():
    assert True


def test_build_firehose_record_remove():
    assert True
