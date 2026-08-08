from client import AiVideoMultimodalMotionBrushAnimatorClient

def main():
    client = AiVideoMultimodalMotionBrushAnimatorClient()
    res = client.animate_motion_brush("landscape.jpg", "ZOOM_IN_PAN_RIGHT")
    print(f"Frame Rate: {res['frame_rate']} fps")
    print(f"Rendered Video URL: {res['rendered_video_url']}")

if __name__ == "__main__":
    main()
