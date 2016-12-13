import elasticsearch

class Es():
    def __init__(self, es_hosts):
        self.es_hosts = es_hosts
        self.es = elasticsearch.Elasticsearch(self.es_hosts)
        self.q = {
            "from": 0,
            "size": 0,
            "query": {
                "bool": {
                    "must": {
                        "query_string": {
                            "query": "http_host:api.invest.ppdai.com"
                        }
                    }
                }
            }
        }


    def get_pv(self, query, index):
        q = {
            "from" : 0,
            "size" : 0,
            "query" : {
                "bool" : {
                    "must" : {
                        "query_string" : {
                            "query" : query
                        }
                    }
                }
            }
        }
        if self.es:
            result=self.es.search(index=index,body=q,analyze_wildcard=True)
            return result.get(u"hits").get(u"total")
        else:
            print("can't connect to {0}".format(self.es_hosts))

    def snap(self, repos, snapname):
        s=self.es.snapshot.create(repository=repos,snapshot=snapname,body=self.q, wait_for_completion=True)
        print s




if __name__ == '__main__':
    es=Es("172.17.43.122:9200")
    # f=es.snap("weekly","api_test")
    f=es.get_pv("http_host:api.invest.ppdai.com", "api-nginx-access-2016.11.06")
    print f
#




