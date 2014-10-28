import etcd

class EtcdBackend(object):
    def __init__(self, host, port, hostname, ttl):
        self.host = host
        self.port = port
        self.hostname = hostname
        self.ttl = ttl

    def put_values(self, etcd_paths):
        client = etcd.Client(host=self.host, port=self.port)
    
        for path in etcd_paths.keys():
            try:
                data = etcd_paths[path]
                data["host"] = self.hostname
                result = client.write(path, data, self.ttl)
            except KeyError, e:
                raise RuntimeError("Key not found: %s" % (path))
            except:
                raise