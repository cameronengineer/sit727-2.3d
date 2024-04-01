# Build Django container image.
podman build . -t quay.io/camo1995/ontrack
echo " "

# Clean Up
podman stop -a
podman rm -a
echo " "

# Create Network
podman network create ontrack
echo " "

# Deploy database pods and let them boot.
podman run --name ontrackdb -d -p 5432:5432 --network ontrack -e POSTGRES_PASSWORD=mysecretpassword -e POSTGRES_USER=ontrack   docker.io/library/postgres:latest
sleep 5

# Deploy Django container
podman run --name ontrack   -d -p 8000:8000 --network ontrack -e POSTGRES_PASSWORD=mysecretpassword -e POSTGRES_HOST=ontrackdb quay.io/camo1995/ontrack

# Wait a sec
sleep 1

# Veiw the django logs
podman logs ontrack
