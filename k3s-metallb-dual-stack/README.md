# 1. k3s dual stack, why?

- ipv4
- ipv6

# 2. starting k3s using dual stack.

```
curl -sfL https://get.k3s.io | sh -s - server \
  --cluster-cidr "10.42.0.0/16,2a01:4f8:13a:850::/64" \
  --service-cidr "10.43.0.0/16,2a01:4f8:13a:850::/64" \
  --cluster-dns "10.43.0.10,2a01:4f8:13a:850::10" \
```
