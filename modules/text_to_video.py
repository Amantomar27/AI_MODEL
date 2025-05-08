import requests

def generate_video(prompt):
    # Placeholder: Replace with actual model/API request (like Runway Gen-2)
    video_url = "https://api.runwayml.com/v1/gen2"
    response = requests.post(video_url, json={"prompt": prompt})
    video_path = response.json().get("video_url")
    return video_path
