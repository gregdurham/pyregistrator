import etcd

class EtcdBackend(object):
    def __init__(self, host, port, hostname, ttl):
        self.host = host
        self.port = port
        self.hostname = hostname
        self.ttl = ttl

    def put_values(self, etcd_paths, noop):
        client = etcd.Client(host=self.host, port=self.port)
    
        for path in etcd_paths.keys():
            try:
                data = etcd_paths[path]
                data["host"] = self.hostname
                if noop:
                    print "Would have updated '%s' with a ttl of %s and data of:\n%s" % (path, self.ttl, data)
                else:
                    result = client.write(path, data, self.ttl)
            except KeyError, e:
                raise RuntimeError("Key not found: %s" % (path))
            except:
                raise