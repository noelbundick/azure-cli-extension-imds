# azure-cli-extension-imds

## Usage

Install bleeding edge from a [build artifact](https://github.com/noelbundick/azure-cli-extension-imds/actions)

```shell
az extension add --source '<build-artifacts-url>/imds-0.1.0-py2.py3-none-any.whl'
```

Launch with the defaults - currently [App Service api-version=2017-09-01](https://docs.microsoft.com/en-us/azure/app-service/overview-managed-identity?tabs=dotnet#using-the-rest-protocol)

```shell
az imds start
```

```text
Command group 'imds' is in preview. It may be changed/removed in a future release.
{
  "localIdentityEndpoint": "http://127.0.0.1:44421/MSI/token",
  "dockerIdentityEndpoint": "http://host.docker.internal:44421/MSI/token",
  "identityHeader": "1038546b-736e-43fd-bf36-bf970c7bc236"
}
```

Get tokens as if you were hitting a live identity endpoint

```shell
export MSI_ENDPOINT=http://127.0.0.1:44421/MSI/token
export MSI_SECRET=1038546b-736e-43fd-bf36-bf970c7bc236
curl -H "secret: $MSI_SECRET" "$MSI_ENDPOINT?api-version=2017-09-01&resource=https://management.azure.com/"
```

You can also get tokens inside containers using the Azure SDK

```shell
docker build -t tokenwriter ./samples/js
docker run --rm -it -e MSI_ENDPOINT=http://host.docker.internal:44421/MSI/token -e MSI_SECRET=1038546b-736e-43fd-bf36-bf970c7bc236 tokenwriter
```


## Development

One-time configuration

```shell
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
azdev setup -r .
```

Day-to-day development

```shell
source .venv/bin/activate

# linting
pylint src
flake8 src

# run commands
az imds start
```
