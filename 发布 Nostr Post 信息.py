import json
import ssl
import time
import uuid
from pynostr.event import Event
from pynostr.relay_manager import RelayManager
from pynostr.filters import FiltersList, Filters
from pynostr.message_type import ClientMessageType
from pynostr.key import PrivateKey

relay_manager = RelayManager(timeout=6)
relay_manager.add_relay("wss://nostr-pub.wellorder.net")
relay_manager.add_relay("wss://relay.damus.io")
private_key = PrivateKey.from_nsec("你的私钥")

filters = FiltersList([Filters(authors=[private_key.public_key.hex()], limit=100)])
subscription_id = uuid.uuid1().hex
relay_manager.add_subscription_on_all_relays(subscription_id, filters)

event = Event("字符串消息")
event.sign(private_key.hex())

relay_manager.publish_event(event)
relay_manager.run_sync()
time.sleep(5)
while relay_manager.message_pool.has_ok_notices():
    ok_msg = relay_manager.message_pool.get_ok_notice()
    print(ok_msg)
while relay_manager.message_pool.has_events():
    event_msg = relay_manager.message_pool.get_event()
    print(event_msg.event.to_dict())
