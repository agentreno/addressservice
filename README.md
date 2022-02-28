# addressservice

## Setup

This project uses poetry for dependency management and virtual environment,
start with `pip install poetry` if necessary and then `poetry install` and
`poetry shell`.

To setup the local sqlite database run `python addressservice/manage.py
migrate`.

This uses
[django-cities-light](https://github.com/yourlabs/django-cities-light) to
source some standardised country, city and region data.

Run `python addressservice/manage.py cities_light --progress
--force-import-all` to populate the database with that data.

Depending on your connection, that could take 5-10 minutes, so the API is
usable without it since the foreign key fields are nullable, but it requires
leaving city null, or pre-populating it via the admin console.

Finally run `python addressservice/manage.py runserver` and navigate to
`http://localhost:8000/`.

## API

There is an address endpoint at `http://localhost:8000/address/` which follows
the usual conventions around HTTP verbs and accepts JSON and form-encoded data.
The HTML presentation built-in to DRF is available if you point your browser at
the API. See this and the [tests](addressservice/api/tests.py) to understand
data formats.

Tests can be run with `python addressservice/manage.py test api`.

## Authentication

I chose to use Istio's end-user request authentication to abstract this task
from the service. Using a service mesh for this allows for a common
authentication system across multiple services, avoiding the need to maintain
multiple implementations across different web frameworks.

https://istio.io/latest/docs/concepts/security/#authentication

The API should be usable locally without it but if you want to try this out,
run a minikube cluster locally and apply all of the manifests by running
`kubectl apply -f manifests/` a few times.

Then obtain the ingress URL with:
```
export INGRESS_HOST=$(minikube ip)
export INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="http2")].nodePort}')
```

Making requests without authentication will fail:
```
curl "$INGRESS_HOST:$INGRESS_PORT/address/" -v
```

Making requests using the Istio test token should succeed:
```
export TOKEN=$(curl https://raw.githubusercontent.com/istio/istio/release-1.13/security/tools/jwt/samples/demo.jwt -s)
curl "$INGRESS_HOST:$INGRESS_PORT/address/" --header "Authorization: Bearer $TOKEN" --header "Accept: application/json" -v
```
