pyregistrator
=============

This client uses a yml file to config paths and commands. 

A sample yml is listed below:

```
---
paths:
    etcd:
        "/servers/temp/path":
            port: 69
            config: option  
commands:
    - cmd: "ls"
      expected: 0
```

There are two main sections, `paths` and `commands`.

Currently under paths is `etcd`. This describes the path that will be updated on a successful run of commands. Under a path you can have one or more optional configuration options. By default host will be updated on etcd to reflect the hostname passed in from the cli. In the example above, I am also adding a configuration for port and config, so in total if the below command succeeds, we would be able to get the following three options from etcd: host, port, and config. 

Under `commands` is a yaml array of commands to execute, you must at a minimum specify a `cmd` key. An optional parameter is `expected` which is the expected command returncode. By default, we expect commands to exit with a `0`. 

If run from the source project:
`pyregistrator --config-file sample.yaml --host=host01.example.com --ttl=120`

Possible options:
```
--host: hostname to update `host` key in path with, default is localhost 
--config-file: Path to the yaml config file, default is /etc/pyconfigurator/default.yml
--etcd-ip: IP address of etcd server default is 127.0.0.1
--etcd-port: Port of etcd server default is 4001
--ttl: Time to live value for the key, default is 60
--noop: Run without modifying anything
```