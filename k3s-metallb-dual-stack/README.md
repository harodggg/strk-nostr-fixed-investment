# 1. k3s dual stack, why?

- ipv4
- ipv6

# 2. starting k3s using dual stack.

```
curl -sfL https://get.k3s.io | sh -s - server \
  --cluster-cidr "10.42.0.0/16,2a01:4f8:13a:850::/64" \
  --service-cidr "10.43.0.0/16,2a01:4f8:13a:850::/64" \
  --cluster-dns "10.43.0.10,2a01:4f8:13a:850::10" \
  --disable=servicelb
```

# 3. install metallb using dual stack for k3s

```
kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.15.2/config/manifests/metallb-native.yaml
```

```
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  name: ipv4-pool
  namespace: metallb-system
spec:
  addresses:
    - 2a01:4f8:13a:850::/64
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  name: ipv6-pool
  namespace: metallb-system
spec:
  addresses:
    - 195.201.160.55 - 195.201.160.55
---
apiVersion: metallb.io/v1beta1
kind: L2Advertisement
metadata:
  name: l2advertisement
  namespace: metallb-system
spec:
  ipAddressPools:
  - ipv4-pool
  - ipv6-pool
```
