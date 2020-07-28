import boto3
import configparser
from create_redshift import user_feedback

config = configparser.ConfigParser()
config.read_file(open('dwh.cfg'))

KEY                         = config.get('AWS','KEY')
SECRET                      = config.get('AWS','SECRET')
DWH_CLUSTER_IDENTIFIER      = config.get("DWH","DWH_CLUSTER_IDENTIFIER")

user_feedback(f'Getting redshift cluster {DWH_CLUSTER_IDENTIFIER}')

redshift = boto3.client('redshift',
                        region_name="us-west-2",
                        aws_access_key_id=KEY,
                        aws_secret_access_key=SECRET
                        )

redshift.delete_cluster( ClusterIdentifier=DWH_CLUSTER_IDENTIFIER,  SkipFinalClusterSnapshot=True)

user_feedback(f'Deleted redshift cluster {DWH_CLUSTER_IDENTIFIER}')