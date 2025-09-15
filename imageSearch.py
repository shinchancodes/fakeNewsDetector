import requests
import base64

def get_base64_of_file(file):
    return base64.b64encode(file.read()).decode()

def get_image_labels(uploadedImageFile):
    if uploadedImageFile is None:
        return None

    VISION_API_KEY = "AIzaSyBDSld31LYta1jb28sXG2rJda5bthvSUnA"
    
    content = get_base64_of_file(uploadedImageFile)
    
    url = f"https://vision.googleapis.com/v1/images:annotate?key={VISION_API_KEY}"
    payload = {
        "requests": [{
            "image": {"content": content},
            "features": [{"type": "TEXT_DETECTION", "maxResults": 5}]
        }]
    }

    response = requests.post(url, json=payload)
    data = response.json()

    labels = []
    try:
        annotations = data["responses"][0]["labelAnnotations"]
        for label in annotations:
            labels.append(label["description"])
    except Exception as e:
        print(f"Error extracting labels: {e}")

    return labels

if __name__ == "__main__":
    imgPath = "crash.jpg"
    labels = get_image_labels(imgPath)
    print(labels)