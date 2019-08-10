# Faas API

```sh
faas-cli deploy -f https://raw.githubusercontent.com/openfaas/faas/master/stack.yml -g http://OPENFAAS_IP:8080

faas-cli template pull https://github.com/openfaas-incubator/python3-debian
faas-cli new noticias --lang python3-debian
```
