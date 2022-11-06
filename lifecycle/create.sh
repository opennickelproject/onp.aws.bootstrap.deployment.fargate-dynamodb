#! /bin/bash

aws cloudformation deploy --template-file app/stack.yml --stack-name onp-fargate-dynamodb --capabilities CAPABILITY_IAM