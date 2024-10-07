import httpx
import json

# Request parameters
url = "https://poe.com/api/gql_POST"
method = "POST"
data = {"queryName":"settingsPageQuery","variables":{},"extensions":{"hash":"6f7d1678f00307984e742d8de7bfdf7d70f4a02dfb7a5c697c7e260be0b24966"}}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0', 'Accept': '*/*', 'Accept-Encoding': 'gzip', 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'Cookie': 'p-b=lCrD4cd42LIFPIRzWHyV8Q%3D%3D; p-lat=jqOOkzRTw57O%2FEG4umguDzwu54GWEFUah05oLBxMGw%3D%3D', 'Origin': 'https://poe.com', 'Poe-Formkey': '6cb9a92f96daa769dc2cfa2ac714edde', 'priority': 'u=1, i', 'Referer': 'https://poe.com/', 'Sec-Ch-Ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"', 'Sec-Ch-Ua-Mobile': '?0', 'Sec-Ch-Ua-Platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'Upgrade-Insecure-Requests': '1', 'content-type': 'application/json', 'Poe-Queryname': 'settingsPageQuery', 'poe-tag-id': '40c0342439a73779a14b004f57bc5084'}

timeout = httpx.Timeout(60)

# Create an httpx client
with httpx.Client() as client:
    try:
        # Send the request
        response = client.request(
            method=method,
            url=url,
            json=data,
            headers=headers,
            timeout=timeout
        )

        # Check if the request was successful
        response.raise_for_status()

        # Print the response
        print(f"Status Code: {response.status_code}")
        print(f"Response Content: {response.text}")

    except httpx.RequestError as e:
        print(f"An error occurred while sending the request: {e}")
    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred: {e}")