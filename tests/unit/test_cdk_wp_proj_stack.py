import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_wp_proj.cdk_wp_proj_stack import CdkWpProjStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_wp_proj/cdk_wp_proj_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkWpProjStack(app, "cdk-wp-proj")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
