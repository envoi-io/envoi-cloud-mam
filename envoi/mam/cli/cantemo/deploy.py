from envoi.aws_cloud_formation_helper import AwsCloudFormationHelper
from envoi.cli import CliCommand

cfn_param_names = {
    'vidispine_admin_password': 'VidispineAdminPassword',
    'cantemo_license_key': 'CantemoLicenseKey',
    'cantemo_license_key_s3_url': 'CantemoLicenseKeyS3Url',
    'ami_id': 'AmiId',
    'instance_type': 'InstanceType',
    'elastic_network_interface_id': 'ElasticNetworkInterfaceId',
    'setup_url': 'SetupUrl',
    'cantemo_stack_name': 'CantemoStackName',
    'vpc_id': 'VpcId',
    'ssh_key_name': 'SSHKeyName'
}


class DeployToAwsCommand(CliCommand):
    DESCRIPTION = "Deploy Cantemo"
    PARAMS = {
        'stack-name': {
            'help': 'Name of the CloudFormation stack',
            'required': True
        },
        'template_url': {
            'help': 'Path to the CloudFormation template',
            'required': False,
            'default': 'https://envoi-prod-files-public.s3.amazonaws.com/aws/cloud-formation/templates/'
                       'cantemo.template.yaml'
        },
        # 'parameters': {
        #     'help': 'Path to the CloudFormation parameters file',
        #     'required': False
        # },
        # 'tags': {
        #     'help': 'Path to the CloudFormation tags file',
        #     'required': False
        # },
        'region': {
            'help': 'AWS region',
            'required': False
        },
        'profile': {
            'help': 'AWS profile',
            'required': False
        },
        # 'wait': {
        #     'help': 'Wait for the stack to complete',
        #     'required': False
        # }
        
        'vidispine-admin-password': {
            'help': 'Vidispine admin password',
            'required': True
        },
        'cantemo_license_key': {
            'help': 'Cantemo license key',
            'required': False
        },
        'cantemo_license_key_s3_url': {
            'help': 'Cantemo license key S3 URL',
            'required': False
        },
        'ami_id': {
            'help': 'AMI ID',
            'required': False
        },
        'instance_type': {
            'help': 'Instance type',
            'required': False
        },
        'elastic_network_interface_id': {
            'help': 'Elastic network interface ID',
            'required': False
        },
        'setup_url': {
            'help': 'Setup URL',
            'required': False
        },
        'cantemo_stack_name': {
            'help': 'Cantemo stack name',
            'required': False
        },
        'vpc_id': {
            'help': 'VPC ID',
            'required': True
        },
        'ssh_key_name': {
            'help': 'SSH key name',
            'required': True
        }
    }

    def run(self, opts=None, template_url=None):
        if opts is None:
            opts = self.opts

        response = self.__class__.create_stack(opts=opts, template_url=template_url)
        stack_id = response['StackId']
        if stack_id is not None:
            response = f"Stack ID {stack_id}"
            print(response)

        return response

    @classmethod
    def create_stack(cls, opts, template_url=None):
        template_parameters = []

        template_parameters_to_check = cfn_param_names

        template_parameters = AwsCloudFormationHelper.populate_template_parameters_from_opts(
            template_parameters, opts, template_parameters_to_check)

        cfn_create_stack_args = {
            'StackName': opts.stack_name,
            'Parameters': template_parameters,
            'Capabilities': ['CAPABILITY_IAM']
        }

        if template_url is not None:
            cfn_create_stack_args['TemplateURL'] = template_url
        elif hasattr(opts, 'template_url'):
            cfn_create_stack_args['TemplateURL'] = opts.template_url
        else:
            raise ValueError("Missing required parameter template_url")

        if hasattr(opts, 'cfn_role_arn') and opts.cfn_role_arn is not None:
            cfn_create_stack_args['RoleARN'] = opts.cfn_role_arn

        client = AwsCloudFormationHelper.client_from_opts(opts=opts)

        response = client.create_stack(**cfn_create_stack_args)
        return response
