from fileinput import filename
from diagrams import Diagram
from diagrams.aws.security import KMS
from diagrams.aws.storage import S3

with Diagram("Deployment Bucket Pattern Overview", show=False, direction="TB", filename='res/overview', outformat='png'):
    KMS("Encryption Key (CMK)") >> S3("Deployment S3 Bucket")