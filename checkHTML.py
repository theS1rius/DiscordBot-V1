import requests

url = "https://tw.tradingview.com/symbols/TVC-DXY/"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    html_content = response.text
    if "last-JWoJqCpY js-symbol-last" in html_content:
        print("✅ 目標 class 存在於 HTML！")
    else:
        print("❌ 目標 class 不在 HTML，可能是 JavaScript 動態生成的")
else:
    print(f"❌ 無法獲取網頁，HTTP 狀態碼: {response.status_code}")
