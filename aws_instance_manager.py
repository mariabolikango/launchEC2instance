import boto3
import time

def launch_instance():
    """Lance une instance EC2 et retourne son ID."""
    ec2 = boto3.client('ec2', region_name='us-west-2')  # Remplacez par votre région AWS
    try:
        # Lancer une instance EC2
        response = ec2.run_instances(
            ImageId='ami-0b4a21432a0c9c1ab',  # Remplacez par une AMI valide
            InstanceType='t1.micro',          # Type d'instance (gratuit avec t2.micro)
            MinCount=1,
            MaxCount=1,
            KeyName='key-pair-tp',           # Nom de votre clé SSH préconfigurée sur AWS
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [{'Key': 'Name', 'Value': 'tp'}]
                }
            ]
        )
        instance_id = response['Instances'][0]['InstanceId']
        print(f"Instance lancée avec succès. ID : {instance_id}")
        return instance_id
    except Exception as e:
        print(f"Erreur lors du lancement de l'instance : {e}")
        return None

def terminate_instance(instance_id):
    """Résilie une instance EC2 spécifiée."""
    ec2 = boto3.client('ec2', region_name='us-west-2')
    try:
        ec2.terminate_instances(InstanceIds=[instance_id])
        print(f"Instance {instance_id} résiliée avec succès.")
    except Exception as e:
        print(f"Erreur lors de la résiliation de l'instance : {e}")

if __name__ == "__main__":
    # Étape 1 : Lancer une instance
    instance_id = launch_instance()
    if instance_id:
        print("Attente de 5 minutes avant la résiliation...")
        time.sleep(300)  # Pause de 5 minutes
        # Étape 2 : Résilier l'instance
        terminate_instance(instance_id)
