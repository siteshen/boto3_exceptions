import os
import sys

import boto3
import botocore


def generate_service_exceptions(service_name):
    client = boto3.client(service_name)

    print("generating {} exceptions ...".format(service_name), file=sys.stdout)
    with open("{}.py".format(service_name), "w") as file:
        print("import boto3\n", file=file)
        print(
            "exceptions = boto3.client('{}').exceptions\n".format(service_name),
            file=file,
        )
        for exc in client.exceptions._code_to_exception.values():
            exc_name = exc.__name__.split(".")[-1]
            print(
                "{exc_name} = exceptions.{exc_name}".format(exc_name=exc_name),
                file=file,
            )


def list_service_names():
    boto_path = botocore.__path__[0]
    data_path = os.path.join(boto_path, "data")
    return [
        f for f in os.listdir(data_path) if os.path.isdir(os.path.join(data_path, f))
    ]


def generate_all_exceptions(service_names=None):
    if not service_names:
        service_names = list_service_names()

    for service_name in service_names:
        generate_service_exceptions(service_name)


def test_all_exceptions(service_names=None):
    if not service_names:
        service_names = list_service_names()

    for service_name in service_names:
        try:
            __import__(service_name, {}, {}, ["boto3_exceptions"])
        except Exception as e:
            print("import error", service_name, e, file=sys.stderr)


if __name__ == "__main__":
    generate_all_exceptions()
    test_all_exceptions()
