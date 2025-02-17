from aws_cdk import App
from src.vpc_stack import VpcStack

app = App()
VpcStack(app, "VpcStack")
app.synth()
