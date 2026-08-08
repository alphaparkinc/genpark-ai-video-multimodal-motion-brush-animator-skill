class AiVideoMultimodalMotionBrushAnimatorClient:
    def animate_motion_brush(self, input_image_path: str, camera_motion: str = "ZOOM_IN_PAN_RIGHT", motion_brush_mask: str = None) -> dict:
        return {
            "rendered_video_url": "https://cdn.example.com/video/motion_render_902.mp4",
            "frame_rate": 60,
            "motion_score": 0.96
        }
