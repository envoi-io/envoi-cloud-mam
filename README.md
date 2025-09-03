### Envoi MAM

Envoi MAM is a powerful tool for deploying **Codemill Cantemo Portal**, a leading Media Asset Management (MAM) system, on a single Amazon EC2 instance. This solution is designed for media companies and content creators to manage their digital assets efficiently. The deployment is handled automatically through an **AWS CloudFormation stack**, which simplifies the process of provisioning the necessary AWS resources. Cantemo Portal integrates with **Vidispine**, a robust media management platform, to handle complex media workflows, including asset ingestion, metadata tagging, search, and distribution.

-----

### Usage

The `envoi-mam cantemo deploy-to-aws` command is your primary tool for launching a Cantemo Portal instance. It takes a variety of arguments to configure the deployment, from basic setup parameters to advanced customizations. The command uses a CloudFormation template to define the infrastructure, which includes creating a dedicated EC2 instance and configuring it with all the required software and licenses.

#### Command-Line Arguments Explained

  * `--stack-name STACK_NAME` (Required): This is the name for your CloudFormation stack. It must be unique within your AWS account and region, and it's what you'll use to identify and manage the Cantemo deployment in the AWS console.
  * `--template-url TEMPLATE_URL`: Specifies the S3 URL of the CloudFormation template. This template is a YAML file that contains a blueprint of all the AWS resources needed for the deployment (e.g., the EC2 instance, security groups, IAM roles). The default URL points to a pre-configured template provided by Envoi.
  * `--region REGION`: Defines the AWS region where the resources will be deployed (e.g., `us-east-1`). If not specified, the command will use the region configured in your AWS CLI profile.
  * `--profile PROFILE`: The name of the AWS CLI profile to use for credentials. This is useful for managing multiple AWS accounts.
  * `--vidispine-admin-password VIDISPINE_ADMIN_PASSWORD` (Required): Sets the password for the Vidispine administrator account. Vidispine is the underlying engine for Cantemo Portal, and this password is a critical security parameter for your deployment.
  * `--cantemo-license-key CANTEMO_LICENSE_KEY`: This is a direct, in-line method for providing your Cantemo Portal license key. It's a string of characters that authenticates and activates your software. Use this option if you don't want to store your license file on S3.
  * `--cantemo-license-key-s3-url CANTEMO_LICENSE_KEY_S3_URL`: This provides a more secure way to handle your license key. Instead of passing the key directly in the command, you upload the license file to an S3 bucket and provide the URL. This is a recommended practice as it avoids exposing the sensitive key in your command history. The format for this URL is `s3://<bucket-name>/<key-path>`.
  * `--ami-id AMI_ID`: Specifies the Amazon Machine Image (AMI) to use for the EC2 instance. An AMI is a pre-configured virtual machine template that includes the operating system and any pre-installed software, like the Cantemo Portal application. If you have a custom AMI, you can use this parameter.
  * `--instance-type INSTANCE_TYPE`: Defines the size and configuration of the EC2 instance (e.g., `m5.2xlarge`). This determines the amount of CPU, memory, and storage available to your Cantemo Portal.
  * `--elastic-network-interface-id ELASTIC_NETWORK_INTERFACE_ID`: An Elastic Network Interface (ENI) is a virtual network card for your EC2 instance. This optional parameter allows you to attach a pre-existing ENI to the instance, which is useful for maintaining a fixed IP address or integrating into an existing network infrastructure.
  * `--vpc-id VPC_ID` (Required): The ID of the Virtual Private Cloud (VPC) where the instance will be launched. A VPC is a logically isolated section of the AWS cloud where you can launch AWS resources.
  * `--ssh-key-name SSH_KEY_NAME` (Required): The name of an existing EC2 Key Pair. This is a crucial security measure that allows you to securely connect to the EC2 instance via SSH for administrative tasks.

-----

### Examples

The following examples illustrate how to use the `deploy-to-aws` command with different configurations, showing both basic and more detailed deployments.

#### 1\. Basic Example Using a License Key S3 URL

This is the most common and recommended method for deployment. It uses the default CloudFormation template and a license key stored in an S3 bucket.

```shell
envoi-mam cantemo deploy-to-aws \
--stack-name cantemo-portal-prod \
--vidispine-admin-password mySecureP@ssw0rd \
--cantemo-license-key-s3-url "s3://envoi-licenses-private/cantemo/license.key" \
--vpc-id "vpc-0a1b2c3d4e5f6g7h8" \
--ssh-key-name "my-prod-key-pair"
```

**Breakdown:**

  * `--stack-name cantemo-portal-prod`: The stack will be named `cantemo-portal-prod` in the CloudFormation console.
  * `--vidispine-admin-password mySecureP@ssw0rd`: Sets a strong, secure password for the Vidispine backend.
  * `--cantemo-license-key-s3-url "s3://envoi-licenses-private/cantemo/license.key"`: The license key is fetched from a private S3 bucket named `envoi-licenses-private`. This is a best practice for security.
  * `--vpc-id "vpc-0a1b2c3d4e5f6g7h8"`: The Cantemo Portal instance will be deployed into this specific VPC.
  * `--ssh-key-name "my-prod-key-pair"`: The instance can be accessed securely using the `my-prod-key-pair` SSH key.

#### 2\. Full Example Using an In-line License Key

This command provides a more comprehensive deployment, specifying parameters like the instance type, AMI, region, and AWS profile. This is useful for customizing the deployment to meet specific performance or security requirements.

```shell
envoi-mam cantemo deploy-to-aws \
--stack-name cantemo-portal-custom \
--template-url "https://envoi-prod-files-public.s3.amazonaws.com/aws/cloud-formation/templates/cantemo.template.yaml" \
--region us-east-1 \
--profile default \
--vidispine-admin-password mySecureP@ssw0rd \
--cantemo-license-key "YOUR_ACTUAL_LICENSE_KEY_STRING" \
--ami-id "ami-0b2f23e8c6c5e3a0a" \
--instance-type "m5.2xlarge" \
--vpc-id "vpc-0a1b2c3d4e5f6g7h8" \
--ssh-key-name "my-key-pair"
```

**Breakdown:**

  * `--stack-name cantemo-portal-custom`: A custom stack name is used.
  * `--template-url ...`: The explicit template URL is provided, even though it's the default.
  * `--region us-east-1`: The deployment is explicitly set for the `us-east-1` (N. Virginia) region.
  * `--profile default`: The `default` AWS profile is used for authentication.
  * `--vidispine-admin-password ...`: The Vidispine password is set.
  * `--cantemo-license-key "YOUR_ACTUAL_LICENSE_KEY_STRING"`: The license key is passed directly as a string.
  * `--ami-id "ami-0b2f23e8c6c5e3a0a"`: A specific AMI is chosen, perhaps a custom one with additional configurations.
  * `--instance-type "m5.2xlarge"`: The instance is scaled up to an `m5.2xlarge` for improved performance.
  * `--vpc-id ...`: The VPC is specified.
  * `--ssh-key-name ...`: The key pair for SSH access is provided.
