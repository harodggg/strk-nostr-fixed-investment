# Install docker

```bash
sudo rm /etc/apt/sources.list.d/docker.list
sudo apt update

curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

# Install kuboard v4

```bash
docker compose up -d -f kuboard.yaml
```
