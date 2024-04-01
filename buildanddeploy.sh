podman build . -t ontrack
podman stop -a
podman rm -a
podman run -d -p 8000:8000 --name ontrack ontrack