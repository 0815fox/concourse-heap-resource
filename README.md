# concourse-heap-resource
Takes build artefacts, stores them locally and returns them on request.

Actually this resource is very simple.
On out operations, it increments the internal version number and stores your data inside the docker container.
On in operations it retrieves the data.

The intended use is to pass data between jobs without having to push it to any kind of registry, versioning system, etc, pp.
Just local.

If you would want to make your data persistent you will have to mount a volume on the docker container.
(I still have to find out how, though)

## Source Configuration

* `heap`: *Required.* A unique name which is used for reference. This should be characters, dashes and names only.

## Behavior

### `check`: Fetch versions of data

Returns a list of newer versions for the data.

### `in`: Download the data for the version.

This provides you with the given version of your data.

#### Parameters

*None.*

### `out`: Upload a new version of data

This takes your data for later retrieval

#### Parameters

*None.*

## Example

Adding the resource to your project:

``` yaml
resource_types:
- name: heap
  type: docker-image
  source:
    repository: 0815fox/concourse-heap-resource
```

Resource configuration:

``` yaml
resources:
- name: heap1
  type: heap
  source:
    heap: heap1
```

Using in job configuration:

``` yaml
jobs:
- name: job1
  ... produce some cool data
  - put: heap1
- name: job2
  get: heap1
  trigger: true
  ... do something cool with the data.
```
