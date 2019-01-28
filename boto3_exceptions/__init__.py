import os

import boto3
import botocore


def generate_service_exceptions(service_name):
    client = boto3.client(service_name)

    print('generating {} exceptions ...'.format(service_name))
    with open('{}.py'.format(service_name), 'w') as file:
        print('import boto3\n', file=file)
        print(
            "exceptions = boto3.client('{}').exceptions\n".format(service_name, service_name),
            file=file)
        for key, val in client.exceptions._code_to_exception.items():
            print('{} = exceptions.{}'.format(key, key), file=file)


def list_service_names():
    boto_path = botocore.__path__[0]
    data_path = os.path.join(boto_path, 'data')
    return [f for f in os.listdir(data_path) if os.path.isdir(os.path.join(data_path, f))]


def generate_all_exceptions(service_names=None):
    if not service_names:
        service_names = list_service_names()

    for service_name in service_names:
        generate_service_exceptions(service_name)


if __name__ == '__main__':
    generate_all_exceptions()
