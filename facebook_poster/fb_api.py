import requests

def post_facebook(content: str, access_token: str, page_id: str, image_path: str):
    url = f"https://graph.facebook.com/v22.0/{page_id}/photos"

    files = {
        'source': open(image_path, 'rb')
    }

    payload = {
        'caption': content,
        'access_token': access_token
    }

    response = requests.post(url, files=files, data=payload)

    if response.status_code == 200:
        print("✅ Đăng thành công!")
    else:
        print(f"❌ Đăng thất bại! {response.status_code} - {response.text}")