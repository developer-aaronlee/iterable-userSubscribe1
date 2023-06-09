import pandas as pd
import numpy as np
import requests

email_channel_id = "39601"
email_type_id = "47276"
sms_channel_id = "40240"
sms_type_id = "79715"
channel_name = "messageChannel"
type_name = "messageType"

iterable_subscribe = "https://api.iterable.com/api/subscriptions"

api_headers = {
    "Content-Type": "application/json",
    "Api-Key": "f435988be541463fb59da3e9d16d0925"
}

df = pd.read_csv("iterable_sms_unsub.csv")
# print(df.values)

nan_values = df.isna()
# print(nan_values)

df.fillna("", inplace=True)
# print(df.values)


def subscription_url(link, kind, kind_id, email):
    url = f"{link}/{kind}/{kind_id}/user/{email}"

    return url


n = 0
for x in df.values[::]:
    n += 1
    # if x[1] != "":
    #     if x[1].lower() == "subscribed":
    #         email_channel_url = subscription_url(iterable_subscribe, channel_name, email_channel_id, x[0])
    #         email_channel_response = requests.patch(url=email_channel_url, headers=api_headers)
    #         print(f"Row {n}: email channel: {x[1]} Response: ", email_channel_response.json())
    #
    #         email_type_url = subscription_url(iterable_subscribe, type_name, email_type_id, x[0])
    #         email_type_response = requests.patch(url=email_type_url, headers=api_headers)
    #         print(f"Row {n}: email type: {x[1]} Response: ", email_type_response.json())
    #
    #         # print(f"Row {n}: Email Subscribe - {email_channel_url}; {email_type_url}")
    #
    #     else:
    #         email_type_url = subscription_url(iterable_subscribe, type_name, email_type_id, x[0])
    #         email_unsub_response = requests.delete(url=email_type_url, headers=api_headers)
    #         print(f"Row {n}: email type: {x[1]} Response: ", email_unsub_response.json())
    #
    #         # print(f"Row {n}: Email Unsubscribe - {email_type_url}")

    if x[1] != "":
        if x[1].lower() == "subscribed":
            sms_channel_url = subscription_url(iterable_subscribe, channel_name, sms_channel_id, x[0])
            sms_channel_response = requests.patch(url=sms_channel_url, headers=api_headers)
            print(f"Row {n}: sms channel: {x[1]} Response: ", sms_channel_response.json())

            sms_type_url = subscription_url(iterable_subscribe, type_name, sms_type_id, x[0])
            sms_type_response = requests.patch(url=sms_type_url, headers=api_headers)
            print(f"Row {n}: sms type: {x[1]} Response: ", sms_type_response.json())

            # print(f"Row {n}: SMS Subscribe - {sms_channel_url}; {sms_type_url}")

        elif x[1].lower() == "pending":
            sms_channel_url = subscription_url(iterable_subscribe, channel_name, sms_channel_id, x[0])
            sms_channel_response = requests.patch(url=sms_channel_url, headers=api_headers)
            print(f"Row {n}: sms channel: {x[1]} Response: ", sms_channel_response.json())

            # print(f"Row {n}: SMS Pending - {sms_channel_url}")

        else:
            sms_type_url = subscription_url(iterable_subscribe, type_name, sms_type_id, x[0])
            sms_unsub_response = requests.delete(url=sms_type_url, headers=api_headers)
            print(f"Row {n}: sms type: {x[1]} Response: ", sms_unsub_response.json())

            # print(f"Row {n}: SMS Unsubscribe - {sms_type_url}")

