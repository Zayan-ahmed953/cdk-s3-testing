#!/usr/bin/env python3
import aws_cdk as cdk

from my_s3_cdk.my_s3_cdk_stack import MyS3CdkStack

app = cdk.App()
MyS3CdkStack(app, "MyS3CdkStack")

app.synth()
