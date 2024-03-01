# Envoi MAM

## Usage

```
envoi-mam cantemo deploy-to-aws -h
usage: envoi-mam cantemo deploy-to-aws [-h] --stack-name STACK_NAME [--template-url TEMPLATE_URL] [--region REGION] [--profile PROFILE] --vidispine-admin-password VIDISPINE_ADMIN_PASSWORD
                                       [--cantemo-license-key CANTEMO_LICENSE_KEY] [--cantemo-license-key-s3-url CANTEMO_LICENSE_KEY_S3_URL] [--ami-id AMI_ID] [--instance-type INSTANCE_TYPE]
                                       [--elastic-network-interface-id ELASTIC_NETWORK_INTERFACE_ID] [--setup-url SETUP_URL] [--cantemo-stack-name CANTEMO_STACK_NAME] --vpc-id VPC_ID --ssh-key-name SSH_KEY_NAME

options:
  -h, --help            show this help message and exit
  --stack-name STACK_NAME
                        Name of the CloudFormation stack (default: None)
  --template-url TEMPLATE_URL
                        Path to the CloudFormation template (default: https://envoi-prod-files-public.s3.amazonaws.com/aws/cloud-formation/templates/cantemo.template.yaml)
  --region REGION       AWS region (default: None)
  --profile PROFILE     AWS profile (default: None)
  --vidispine-admin-password VIDISPINE_ADMIN_PASSWORD
                        Vidispine admin password (default: None)
  --cantemo-license-key CANTEMO_LICENSE_KEY
                        Cantemo license key (default: None)
  --cantemo-license-key-s3-url CANTEMO_LICENSE_KEY_S3_URL
                        Cantemo license key S3 URL (default: None)
  --ami-id AMI_ID       AMI ID (default: None)
  --instance-type INSTANCE_TYPE
                        Instance type (default: None)
```

## Examples

### Deploy Cantemo Portal to AWS

Basic example using Cantemo license key:
```shell
envoi-mam cantemo deploy-to-aws \
--stack-name cantemo-portal \
--template-url "https://envoi-prod-files-public.s3.amazonaws.com/aws/cloud-formation/templates/cantemo.template.yaml" \
--vidispine-admin-password admin \
--cantemo-license-key-s3-url "s3://envoi-prod-files-public/aws/cantemo/license.key" \
--vpc-id "vpc-0a1b2c3d4e5f6g7h8" \
--ssh-key-name "my-key-pair"
```

Basic example using Cantemo license key S3 URL:
```shell
envoi-mam cantemo deploy-to-aws \
--stack-name cantemo-portal \
--vidispine-admin-password admin \
--cantemo-license-key-s3-url "s3://envoi-prod-files-public/aws/cantemo/license.key" \
--vpc-id "vpc-0a1b2c3d4e5f6g7h8" \
--ssh-key-name "my-key-pair"
```

Full example using Cantemo license key:
```shell
envoi-mam cantemo deploy-to-aws \
--stack-name cantemo-portal \
--template-url "https://envoi-prod-files-public.s3.amazonaws.com/aws/cloud-formation/templates/cantemo.template.yaml" \
--region us-east-1 \
--profile default \
--vidispine-admin-password admin \
--cantemo-license-key "LICENSE_KEY" \
--ami-id "ami-0b2f23e8c6c5e3a0a" \
--instance-type "m5.2xlarge" \
--vpc-id "vpc-0a1b2c3d4e5f6g7h8" \
--ssh-key-name "my-key-pair"
```

Full example using Cantemo license key S3 URL:
```shell
```shell
envoi-mam cantemo deploy-to-aws \
--stack-name cantemo-portal \
--template-url "https://envoi-prod-files-public.s3.amazonaws.com/aws/cloud-formation/templates/cantemo.template.yaml" \
--region us-east-1 \
--profile default \
--vidispine-admin-password admin \
--cantemo-license-key-s3-url "s3://envoi-prod-files-public/aws/cantemo/license.key" \
--ami-id "ami-0b2f23e8c6c5e3a0a" \
--instance-type "m5.2xlarge" \
--vpc-id "vpc-0a1b2c3d4e5f6g7h8" \
--ssh-key-name "my-key-pair"
```