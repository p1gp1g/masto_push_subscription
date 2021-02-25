#!/usr/bin/env python3
from mastodon import Mastodon

instance_url = input("Mastodon instance: ")
username = input("Mastodon username: ")
password = input("Mastodon password: ")
endpoint = input("Endpoint (has printed by the app MastodonPush): ")

Mastodon.create_app("NoProvider2Push",
    api_base_url=instance_url, 
    to_file="/tmp/app_token")

masto = Mastodon(
    client_id = "/tmp/app_token",
    api_base_url = instance_url
)

masto.log_in(
    username=username,
    password=password
)

priv, pub = masto.push_subscription_generate_keys()
print(masto.push_subscription_set(
    endpoint=endpoint,
    encrypt_params=pub,
    follow_events = True,
    favourite_events = True,
    reblog_events = True,
    mention_events = True,
    poll_events = True,
    follow_request_events = True
))
