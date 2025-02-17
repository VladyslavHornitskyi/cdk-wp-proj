from aws_cdk import App, Stack
from aws_cdk import aws_ec2 as ec2
import aws_cdk.aws_codestar_alpha as codestar
from constructs import Construct

class VpcStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        self.vpc = ec2.Vpc(self, "CustomVpc",
                           max_azs=2,
                           subnet_configuration=[
                               ec2.SubnetConfiguration(
                                   name="Public",
                                   subnet_type=ec2.SubnetType.PUBLIC
                               ),
                               ec2.SubnetConfiguration(
                                   name="Private",
                                   subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS
                               )
                           ])