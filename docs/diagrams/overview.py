from fileinput import filename
from diagrams import Diagram
from diagrams.aws.security import IAMRole
from diagrams.aws.compute import Fargate
from diagrams.aws.database import Dynamodb

with Diagram("Fargate DynamoDB Pattern Overview", show=False, direction="TB", filename='docs/diagrams/res/overview', outformat='png'):
    IAMRole("DynamoDB Access Role") >> Fargate("Service")>> Dynamodb("Dynamodb Table")