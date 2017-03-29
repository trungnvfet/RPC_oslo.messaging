from oslo_config import cfg
import oslo_messaging as msg


class TestClient(object):
    def __init__(self, transport, target):
        self.transport = transport
        self.target = target
        self._client = msg.RPCClient(self.transport, self.target)

    def test(self):
        cctxt = self._client.prepare(namespace='control', version='2.0')
        # Call
        cctxt.call(ctxt={}, method='test', arg='alo. My name is Trung')
        # Cast an fanout
        cctxt.cast(ctxt={}, method='test', arg='Just for Fun')

# Create Messaging Transport
transport = msg.get_transport(cfg.CONF)
# Create Target
target = msg.Target(topic='trungnv')

# Create Target and set fanout=True
target = msg.Target(topic='trungnv', fanout=True)

# Create RPC client
client = TestClient(transport, target)

# Call function
client.test()