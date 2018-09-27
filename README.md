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

``` yaml
resource_types:
- name: heap
  type: docker-image
  source:
    repository: 0815fox/concourse-heap-resource
resources:
- name: heap1
  type: heap
  source:
    heap: heap1
jobs:
- name: put-hello-world-job
  plan:
  - task: put-hello-world
    config:
      platform: linux
      image_resource:
        type: docker-image
        source: {repository: alpine}
      outputs:
      - name: heap1
      run:
        path: touch
        args: 
        - heap1/hello-world
  - put: heap1
- name: get-hello-world-job
  plan:
  - get: heap1
    trigger: true
    passed: [put-hello-world-job]
  - task: get-hello-world
    config:
      platform: linux
      inputs:
      - name: heap1
      image_resource:
        type: docker-image
        source: {repository: alpine}
      run:
        path: ls
        args: 
        - heap1
```
