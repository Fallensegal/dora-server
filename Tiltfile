# Deploy: tell Tilt what YAML to deploy
k8s_yaml(listdir('deploy', True))

# Build: tell Tilt what images to build from which directories
docker_build('example', '.', dockerfile='./projects/dora-server/Dockerfile')

k8s_resource(workload='dora-deployment', port_forwards=8000)
