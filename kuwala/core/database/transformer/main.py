import os
import subprocess
from sshtunnel import SSHTunnelForwarder


if __name__ == '__main__':
    ssh_host = os.getenv('SSH_HOST')
    ssh_user = os.getenv('SSH_USER')
    ssh_pkey = os.getenv('SSH_PKEY')
    dbt_host = os.getenv('DBT_HOST') or 'localhost'

    os.chdir('transformer_dbt/')

    if ssh_host and ssh_user and ssh_pkey:
        ssh_tunnel = SSHTunnelForwarder(ssh_host, ssh_username=ssh_user, ssh_pkey=ssh_pkey,
                                        remote_bind_address=('127.0.0.1', 5432))

        ssh_tunnel.start()
        subprocess.call('dbt run --profiles-dir .', shell=True,
                        env=dict(os.environ, DBT_PORT=str(ssh_tunnel.local_bind_port), DBT_HOST=dbt_host))
    else:
        subprocess.call('dbt run --profiles-dir .', shell=True, env=dict(os.environ, DBT_HOST=dbt_host))
