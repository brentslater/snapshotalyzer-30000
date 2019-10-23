# snapshotalyzer-30000
Demo project to manage AWS instance snapshots


## About

This project is a demo, and uses boto3 to manage AWS EC2 instnace snapshots.

## Configuring

shotty uses the configuration file created by the AWS cli. e.g.

`aws confgiure --profile shotty`

## Running

`pipenv run python shotty/shotty.py <command> <--project=PROJECT>`

*command* is list, start or stop
*project* is optional
