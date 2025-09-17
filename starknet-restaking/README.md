# 1. Deploy k3s cluster

```
curl -sfL https://get.k3s.io | sh -
```

# 2. Run a cronjob

```
kubectl apply -f cronjob-k8s.yaml
```
